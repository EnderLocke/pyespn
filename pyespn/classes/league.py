from pyespn.core.decorators import validate_json
from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.exceptions import API400Error
from pyespn.classes.betting import Betting
from pyespn.classes.stat import LeaderCategory
from concurrent.futures import ThreadPoolExecutor, as_completed


@validate_json("league_json")
class League:
    """
    Represents a sports league with associated data such as teams, events, rankings,
    betting futures, and statistical leaders.

    This class provides methods for loading and managing league-level data retrieved
    from the ESPN API, including season-specific information, betting data, and
    statistical leaderboards.

    Attributes:
        espn_instance (PyESPN): The main interface for interacting with ESPN's API.
        league_json (dict): The raw JSON data representing the league.
        ref (str): Reference URL for the league.
        id (str): The unique identifier for the league.
        name (str): Full name of the league.
        display_name (str): Human-readable display name for the league.
        abbreviation (str): Abbreviated name of the league.
        short_name (str): Shortened name version of the league.
        slug (str): URL-friendly version of the league's name.
        is_tournament (bool): Whether the league is a tournament format.
        season (dict): Details for the current season.
        seasons (list): A list of past and present seasons.
        franchises (list): Franchises associated with the league.
        teams (list): List of teams in the league.
        group (dict): Group metadata the league is associated with.
        groups (list): Collection of groups within the league.
        events (list): Events related to the league.
        notes (str): Additional notes or commentary on the league.
        rankings (list): Ranking data for the league.
        draft (dict): Draft data associated with the league.
        links (list): External or internal links related to the league.
        league_leaders (dict): Cached leader category objects per season.
        betting_futures (dict): Cached betting futures data per season.

    Methods:
        __repr__(): Returns a formatted string representation of the league.
        _set_league_json(): Internal method to populate league attributes from JSON.
        load_season_free_agents(season): Placeholder for loading free agent data for a season.
        get_all_seasons_futures(season): Loads and processes all betting futures for the given season.
        _process_bet(bet, season): Internal helper to create a Betting object from a bet JSON.
        fetch_leader_category(category, season): Loads and returns a LeaderCategory object.
        load_season_league_leaders(season): Loads statistical leaders for a given season.
    """

    def __init__(self, espn_instance, league_json: dict):
        """
        Initializes a League instance using the provided ESPN API instance and league JSON data.

        Args:
            espn_instance (PyESPN): The ESPN API instance.
            league_json (dict): The raw JSON data representing the league.
        """
        self.league_json = league_json
        self.espn_instance = espn_instance
        self.league_leaders = {}
        self.betting_futures = {}
        self._set_league_json()

    def __repr__(self) -> str:
        """
        Returns a string representation of the betting Provider instance.

        Returns:
            str: A formatted string with the Providers information .
        """
        return f"<League | {self.display_name}>"

    def _set_league_json(self):
        """
        Extracts and sets the attributes of the League instance from the provided JSON data.
        """
        self.ref = self.league_json.get("$ref")
        self.id = self.league_json.get("id")
        self.name = self.league_json.get("name")
        self.display_name = self.league_json.get("displayName")
        self.abbreviation = self.league_json.get("abbreviation")
        self.short_name = self.league_json.get("shortName")
        self.slug = self.league_json.get("slug")
        self.is_tournament = self.league_json.get("isTournament")
        self.season = self.league_json.get("season", {})
        self.seasons = self.league_json.get("seasons")
        self.franchises = self.league_json.get("franchises")
        self.teams = self.league_json.get("teams")
        self.group = self.league_json.get("group")
        self.groups = self.league_json.get("groups")
        self.events = self.league_json.get("events")
        self.notes = self.league_json.get("notes")
        self.rankings = self.league_json.get("rankings")
        self.draft = self.league_json.get("draft")
        self.links = self.league_json.get("links", [])

    def load_season_free_agents(self, season):
        # todo this seems to always return nothing
        url = f''

    def get_all_seasons_futures(self, season):
        """
        Loads and processes betting futures for a given season.

        This method retrieves betting futures data for the specified season using the ESPN API.
        It handles pagination and concurrent data fetching using thread pools for improved performance.
        Each betting item is processed individually through `_process_bet` and collected into a list.

        The processed futures are stored in `self.betting_futures` under the specified season key.

        Args:
            season (int or str): The season year to fetch futures data for.

        Raises:
            API400Error: If the ESPN API returns a 400-level error during data fetching, an error message
                         will be printed including the season, team name, and team ID.
        """
        for team in self.espn_instance.teams:
            if season not in team.roster:
                team.load_season_roster(season=season)

        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)
        betting_futures = []
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/futures'

        try:
            season_content = fetch_espn_data(url)
            pages = season_content.get('pageCount', 0)

            with ThreadPoolExecutor() as executor:
                future_to_page = {
                    executor.submit(fetch_espn_data, f'{url}?page={page}'): page
                    for page in range(1, pages + 1)
                }

                for future in as_completed(future_to_page):
                    page_data = future.result()

                    with ThreadPoolExecutor() as bet_executor:
                        bet_futures = {
                            bet_executor.submit(self._process_bet, bet, season): bet
                            for bet in page_data.get('items', [])
                        }

                        # Process each bet as its future completes
                        for bet_future in as_completed(bet_futures):
                            betting_futures.append(bet_future.result())

            self.betting_futures[season] = betting_futures

        except API400Error as e:
            print(f"Failed to fetch oddsbetting data for season {season} | team {self.name} | id {self.team_id}: {e}")

    def _process_bet(self, bet, season):
        """
        Processes an individual bet and returns a Betting object.

        Args:
            bet (dict): The betting data for an individual bet.

        Returns:
            Betting: The Betting object corresponding to the provided data.
        """
        return Betting(betting_json=bet, espn_instance=self.espn_instance, season=season)

    def fetch_leader_category(self, category, season) -> LeaderCategory:
        """
        Fetches leader category data for a specific category in the given season.

        Args:
            category (dict): The category data to be processed.
            season (str): The season for which the leader data is fetched.

        Returns:
            LeaderCategory: The LeaderCategory object created for this category.
        """
        return LeaderCategory(leader_cat_json=category,
                              espn_instance=self.espn_instance,
                              season=season)

    def load_season_league_leaders(self, season):
        """
        Fetches the league leaders for the given season using futures to process categories concurrently.

        Args:
            season (str): The season for which the league leaders are fetched.
        """

        for team in self.espn_instance.teams:
            if season not in team.roster:
                team.load_season_roster(season=season)

        api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/leaders'

        try:
            leaders_content = fetch_espn_data(url)
            leaders = []

            with ThreadPoolExecutor() as executor:
                # Submit a task for each category to fetch leader data concurrently
                future_to_category = {
                    executor.submit(self.fetch_leader_category, category, season): category
                    for category in leaders_content.get('categories', [])
                }

                # Collect results as they complete
                for future in as_completed(future_to_category):
                    try:
                        category_data = future.result()
                        leaders.append(category_data)
                    except Exception as e:
                        print(f"Error fetching leader category: {e}")

            self.league_leaders[season] = leaders

        except API400Error as e:
            print(f"Failed to fetch league leaders for season {season}: {e}")
