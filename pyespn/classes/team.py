from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.classes.venue import Venue
from pyespn.classes.player import Player
from pyespn.classes.image import Image
from pyespn.classes.stat import Record, Stat
from pyespn.data.version import espn_api_version as v
from pyespn.core.decorators import validate_json
from concurrent.futures import ThreadPoolExecutor, as_completed


@validate_json("team_json")
class Team:
    """
    Represents a sports team within the ESPN API framework.

    This class stores team-related information and maintains a reference
    to a `PYESPN` instance, allowing access to league-specific details.

    Attributes:
        espn_instance (PYESPN): The parent `PYESPN` instance providing access to league details.
        team_json (dict): The raw team data retrieved from the ESPN API.
        team_id (str | None): The unique identifier for the team.
        guid (str | None): The GUID associated with the team.
        uid (str | None): The UID of the team.
        location (str | None): The geographical location or city of the team.
        name (str | None): The official name of the team.
        nickname (str | None): The team's nickname.
        abbreviation (str | None): The team's short abbreviation (e.g., 'NYG', 'LAL').
        display_name (str | None): The full display name of the team.
        short_display_name (str | None): A shorter version of the display name.
        primary_color (str | None): The team's primary color (hex code).
        alternate_color (str | None): The team's alternate color (hex code).
        is_active (bool | None): Indicates whether the team is currently active.
        is_all_star (bool | None): Indicates if the team is an all-star team.
        logos (list[str]): A list of URLs to the team’s logos.
        venue_json (dict): The raw venue data associated with the team.
        home_venue (Venue): The `Venue` instance representing the team's home venue.
        links (dict): A dictionary mapping link types (e.g., 'official site') to their URLs.

    Methods:
        get_logo_img() -> list[str]:
            Returns the list of team logo URLs.

        get_team_colors() -> dict:
            Returns the team's primary and alternate colors.

        get_home_venue() -> Venue:
            Retrieves the home venue of the team as a `Venue` instance.

        get_league() -> str:
            Retrieves the league abbreviation associated with the team.

        to_dict() -> dict:
            Returns the raw team JSON data as a dictionary.
    """

    def __init__(self, espn_instance, team_json):
        """
        Initializes a Team instance.

        Args:
            espn_instance (PYESPN): The parent `PYESPN` instance, providing access to league details.
            team_json (dict): The raw team data retrieved from the ESPN API.

        """
        self.espn_instance = espn_instance
        self.records = {}
        self.stats = {}
        self.coaches = {}
        if team_json:
            self.team_json = team_json
        else:
            self.team_json = {}
        self.roster = {}
        self._load_team_data()
        self.home_venue = Venue(venue_json=self.venue_json,
                                espn_instance=self.espn_instance)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the team's location, name, abbreviation, and league.
        """
        return f"<Team | {self.location} {self.name} ({self.abbreviation}) - {self.get_league()}>"

    def _load_team_data(self):
        """
        Extracts and sets team data from the provided JSON.
        """
        self.ref = self.team_json.get('$ref')
        self.team_id = self.team_json.get("id")
        self.guid = self.team_json.get("guid")
        self.uid = self.team_json.get("uid")
        self.location = self.team_json.get("location")
        self.name = self.team_json.get("name")
        self.nickname = self.team_json.get("nickname")
        self.abbreviation = self.team_json.get("abbreviation")
        self.display_name = self.team_json.get("displayName")
        self.short_display_name = self.team_json.get("shortDisplayName")
        self.primary_color = self.team_json.get("color")
        self.alternate_color = self.team_json.get("alternateColor")
        self.is_active = self.team_json.get("isActive")
        self.is_all_star = self.team_json.get("isAllStar")

        self.logos = [Image(image_json=logo, espn_instance=self.espn_instance) for logo in self.team_json.get("logos", [])]
        self.venue_json = self.team_json.get("venue", {})

        self.links = {link["rel"][0]: link["href"] for link in self.team_json.get("links", []) if "rel" in link}

    def load_team_season_stats(self, season):
        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)

        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{self.team_id}/statistics?lang=en&region=us'
        stats_content = fetch_espn_data(url)
        all_stats = []
        for stat in stats_content.get('splits', []):
            all_stats.append(Stat(stat_json=stat,
                                  espn_instance=self.espn_instance))
        self.stats[season] = {}

    def get_team_colors(self) -> dict:
        """
        Retrieves the team's primary and alternate colors.

        Returns:
            dict: A dictionary containing 'primary_color' and 'alt_color' keys with their respective hex values.
        """
        return {
            'primary_color': self.primary_color,
            'alt_color': self.alternate_color
        }

    def get_home_venue(self) -> Venue:
        """
        Retrieves the home venue of the team.

        Returns:
            Venue: The `Venue` instance representing the team's home venue.
        """
        return self.home_venue

    def get_league(self) -> str:
        """
        Retrieves the league abbreviation from the associated `PYESPN` instance.

        Returns:
            str: The league abbreviation (e.g., 'nfl', 'nba', 'cfb').
        """
        return self.espn_instance.league_abbv

    def load_season_roster(self, season) -> None:
        """
        Loads the team roster for a given season using ESPN API data.

        This function retrieves the roster for the specified season by:
        - Fetching paginated lists of athletes.
        - Concurrently retrieving detailed athlete data using multiple API requests.
        - Storing the roster data in the `self.roster` dictionary.

        Args:
            season (int): The season year for which to load the roster.

        Returns:
            None: The function updates `self.roster` with the retrieved players.

        Raises:
            Exception: Logs any errors encountered when fetching player data.

        Example:
            >>> team.load_season_roster(2023)
            >>> print(team.roster[2023])
            [<Player | John Doe>, <Player | Jane Smith>, ...]

        Note:
            - Uses `ThreadPoolExecutor` for concurrent fetching of athlete data to improve performance.
            - The number of worker threads (`max_workers=10`) can be adjusted based on API rate limits.
        """

        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)

        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info.get("sport")}/leagues/{api_info.get("league")}/seasons/{season}/teams/{self.team_id}/athletes'
        content = fetch_espn_data(url)
        page_count = content.get('pageCount', 1)

        athletes = []
        athlete_urls = []

        # Collect all athlete URLs first
        for page in range(1, page_count + 1):
            page_url = f'{url}?page={page}'
            page_content = fetch_espn_data(page_url)
            for athlete in page_content.get('items', []):
                athlete_urls.append(athlete.get('$ref'))

        # Fetch athlete data in parallel
        with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust workers as needed
            future_to_url = {executor.submit(fetch_espn_data, url): url for url in athlete_urls}

            for future in as_completed(future_to_url):
                try:
                    athlete_content = future.result()
                    athletes.append(Player(player_json=athlete_content, espn_instance=self.espn_instance))
                except Exception as e:
                    print(f"Failed to fetch athlete data: {e}")

        self.roster[season] = athletes

    def load_season_results(self, season):
        """
        Retrieves and stores seasonal game records for the team.

        This method constructs a URL to the ESPN API using the team’s league and sport information,
        then fetches and parses the game results (win/loss record) for the specified season.
        Each result is wrapped in a `Record` object, which is stored in the team's `records`
        dictionary under the given season key.

        Args:
            season (int): The season year for which the team’s game records should be retrieved.

        Side Effects:
            Updates the `self.records` dictionary with a list of `Record` instances representing
            seasonal game results.

        """

        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{self.team_id}/record?lang=en&region=us'
        results_content = fetch_espn_data(url)
        season_records = []
        for result in results_content.get('items', []):
            season_records.append(Record(record_json=result,
                                         espn_instance=self.espn_instance))
        self.records[season] = season_records

    def load_season_coaches(self, season):
        """
        Loads the coaching staff for the team in the specified season.

        This method retrieves a list of coach references for the team from the ESPN API,
        then performs follow-up requests to fetch detailed information for each coach.
        Each coach is instantiated as a `Player` object (representing coaching personnel)
        and added to the `coaches` dictionary under the corresponding season.

        Args:
            season (int): The season year for which coaching data should be loaded.

        Side Effects:
            Updates the `self.coaches` dictionary with a list of `Player` instances
            representing the coaching staff.

        Notes:
            Coach data is retrieved in two stages: first a summary list with URLs,
            then a second pass to fetch detailed info for each coach using those URLs.
        """
        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/teams/{self.team_id}/coaches?lang=en&region=us'
        coach_content = fetch_espn_data(url)
        coach_records = []
        coach_urls = []
        for coach in coach_content.get('items', []):
            coach_urls.append(coach.get('$ref'))

        for coach_url in coach_urls:
            coach_url_response = fetch_espn_data(coach_url)
            coach_records.append(Player(player_json=coach_url_response,
                                        espn_instance=self.espn_instance))

        self.coaches[season] = coach_records

    def to_dict(self) -> dict:
        """
        Returns the raw team JSON data as a dictionary.

        Returns:
            dict: The original team data retrieved from the ESPN API.
        """
        return self.team_json


class Manufacturer:
    """
    Represents a manufacturer in the racing league, encapsulating information about the manufacturer
    including its name, abbreviation, color, and associated event log.

    Attributes:
        manufacturer_json (dict): The raw JSON data representing the manufacturer.
        espn_instance (object): An instance of the ESPN API handler used for making requests.
        api_ref (str): The API reference URL for the manufacturer.
        id (str): The unique identifier of the manufacturer.
        name (str): The full name of the manufacturer.
        display_name (str): The display name of the manufacturer.
        short_display_name (str): The short display name of the manufacturer.
        abbreviation (str): The abbreviation of the manufacturer's name.
        color (str): The color associated with the manufacturer.
        event_log_ref (str): The reference to the manufacturer's event log.

    Methods:
        __repr__: Returns a string representation of the Manufacturer instance.
    """

    def __init__(self, manufacturer_json, espn_instance):
        """
        Initializes a Manufacturer object with the provided JSON data and ESPN instance.

        Args:
            manufacturer_json (dict): The raw JSON data for the manufacturer.
            espn_instance (object): An instance of the ESPN API handler.
        """
        self.manufacturer_json = manufacturer_json
        self.espn_instance = espn_instance
        self._load_manufacturer_data()

    def _load_manufacturer_data(self):
        """
        Sets each attribute from the manu_json to its own attribute.
        """
        self.api_ref = self.manufacturer_json.get('$ref')
        self.id = self.manufacturer_json.get('id')
        self.name = self.manufacturer_json.get('name')
        self.display_name = self.manufacturer_json.get('displayName')
        self.short_display_name = self.manufacturer_json.get('shortDisplayName')
        self.abbreviation = self.manufacturer_json.get('abbreviation')
        self.color = self.manufacturer_json.get('color')

        # Event log reference
        self.event_log_ref = self.manufacturer_json.get('eventLog', {}).get('$ref')

    def __repr__(self):
        """
        Returns a string representation of the Manufacturer instance.
        """
        return f"<Manufacturer | {self.name}, {self.abbreviation}>"

