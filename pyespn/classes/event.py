from pyespn.core.decorators import validate_json
from pyespn.classes.betting import GameOdds
from pyespn.classes.gamelog import Drive, Play
from pyespn.utilities import fetch_espn_data
from concurrent.futures import ThreadPoolExecutor, as_completed


@validate_json("event_json")
class Event:
    """
    Represents a sports event within the ESPN API framework.

    This class acts as a central unit for encapsulating all relevant data associated with
    a sporting event, including participating teams, venue details, drives (football),
    play-by-play actions (basketball), competition metadata, and betting odds.

    Attributes:
        event_json (dict): The raw JSON data from ESPN describing the event.
        espn_instance (PYESPN): The active ESPN API interface used for data lookups.
        url_ref (str): ESPN API reference URL to this event.
        event_id (int): Unique identifier for the event.
        date (str): Date and time of the event in ISO format.
        event_name (str): Full name of the event.
        short_name (str): Abbreviated name of the event.
        competition_type (str): Type of competition (e.g. "regular", "postseason").
        venue_json (dict): Raw JSON data representing the venue.
        event_venue (Venue): Venue object built from the venue JSON.
        event_notes (list): Optional notes or metadata about the event.
        home_team (Team): Team object representing the home team.
        away_team (Team): Team object representing the away team.
        api_info (dict): League-specific metadata used to construct ESPN URLs.
        competition (Competition): An object containing metadata about the specific competition.
        odds (list[GameOdds]): List of betting odds (if available).
        drives (list[Drive] or None): A list of `Drive` instances for football games.
        plays (list[Play] or None): A list of `Play` instances for basketball games.

    Methods:
        load_betting_odds():
            Fetches and parses multi-page betting odds data.

        load_play_by_play():
            Routes to appropriate play-by-play loader depending on sport type.

        _load_competition_data():
            Loads metadata about the specific competition instance.

        _load_teams():
            Populates home_team and away_team attributes from competitors JSON.

        _load_basketball_plays():
            Loads all basketball plays as `Play` objects.

        _load_drive_data():
            Loads all football drives as `Drive` objects.

        to_dict() -> dict:
            Returns the original raw JSON for this event.

        __repr__() -> str:
            A readable string representation showing the event short name and date.
    """

    def __init__(self, event_json: dict, espn_instance,
                 load_game_odds: bool = False,
                 load_play_by_play: bool = False):
        """
        Initializes an Event instance with the provided JSON data.

        This constructor optionally loads betting odds and play-by-play data based on
        the supplied flags. By default, those are not loaded unless explicitly enabled.

        Args:
            event_json (dict): The JSON data containing event details.
            espn_instance (PYESPN): The parent `PYESPN` instance for API interaction.
            load_game_odds (bool, optional): If True, fetch and load the betting odds
                                             for the event. Defaults to False.
            load_play_by_play (bool, optional): If True, fetch and load the play-by-play
                                                data (either drives or plays depending
                                                on sport). Defaults to False.
        """
        from pyespn.classes.venue import Venue
        self.competition = None
        self.event_json = event_json
        self._espn_instance = espn_instance
        self.url_ref = self.event_json.get('$ref')
        self._event_id = self.event_json.get('id')
        self.date = self.event_json.get('date')
        self.event_name = self.event_json.get('name')
        self.short_name = self.event_json.get('shortName')
        self.competition_type = self.event_json.get('competitions', [])[0].get('type', {}).get('type')
        self.venue_json = self.event_json.get('competitions', [])[0].get('venue', {})
        self.event_venue = Venue(venue_json=self.venue_json,
                                 espn_instance=self._espn_instance)
        self.event_notes = self.event_json.get('competitions', [])[0].get('notes', [])
        self._home_team = None
        self._away_team = None
        self._odds = None
        self._drives = None
        self._plays = None
        self.api_info = self._espn_instance.api_mapping
        self._load_teams()
        self._load_competition_data()
        if load_game_odds:
            self.load_betting_odds()
        if load_play_by_play:
            self.load_play_by_play()

    @property
    def event_id(self):
        """
            str: the id for the event
        """
        return self._event_id

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance
    
    @property
    def drives(self):
        """
            list[Drive]: a list of drives for the given event
        """
        return self._drives

    @property
    def plays(self):
        """
            list[Play]: a list of drives for the given event
        """
        return self._plays

    @property
    def odds(self):
        """
            list[Betting]: a list of Odds for the given game
        """
        return self._odds

    @property
    def away_team(self):
        """
            Team: the away team as a Team object
        """
        return self._away_team

    @property
    def home_team(self):
        """
            Team: the home team as a Team object
        """
        return self._home_team

    def _load_teams(self):
        """
        Private method to fetch and assign the competing teams for the event.

        This method retrieves the teams' JSON data using their API references and
        initializes `Team` instances for `team1` and `team2`.
        """
        team1 = self.event_json.get('competitions', [])[0].get('competitors')[0]
        team2 = self.event_json.get('competitions', [])[0].get('competitors')[1]
        team1_id = team1.get('id')
        team2_id = team2.get('id')

        if team1.get('homeAway') == 'home':
            self._home_team = self._espn_instance.get_team_by_id(team1_id)

            self._away_team = self._espn_instance.get_team_by_id(team2_id)
        else:
            self._home_team = self._espn_instance.get_team_by_id(team2_id)

            self._away_team = self._espn_instance.get_team_by_id(team1_id)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the events data.
        """
        return f"<Event | {self.short_name} {self.date}>"

    def load_betting_odds(self):
        """
        method to fetch and assign betting odds for the event.

        This method constructs the appropriate URL using event and league data, then retrieves
        and parses odds data from each available page. The results are stored in the `self.odds` list
        as `GameOdds` instances.
        """

        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_id}/competitions/{self._event_id}/odds'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        def fetch_and_parse_odds(page):
            page_url = url + f'?page={page}'
            odds_content = fetch_espn_data(page_url)
            return [
                GameOdds(odds_json=odd,
                         espn_instance=self._espn_instance,
                         event_instance=self)
                for odd in odds_content.get('items', [])
            ]

        event_odds = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_and_parse_odds, page) for page in range(1, pages + 1)]
            for future in as_completed(futures):
                try:
                    event_odds.extend(future.result())
                except Exception as e:
                    print(f"Error fetching betting odds page: {e}")

        self._odds = event_odds

    def _load_competition_data(self):
        """
        Private method to fetch and assign competition details for the event.

        This method retrieves the competition data for the event and initializes a `Competition`
        object using the JSON data, storing it in the `self.competition` attribute.
        """
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_id}/competitions/{self._event_id}'
        competition_content = fetch_espn_data(url)

        self.competition = Competition(competition_json=competition_content,
                                       espn_instance=self._espn_instance,
                                       event_instance=self)

    def load_play_by_play(self):
        """
        Private method to load play-by-play data for the event.

        This method routes the data fetching logic based on the sport type—calling
        `_load_basketball_plays()` for basketball and `_load_drive_data()` for football.
        """
        if self.api_info['sport'] == 'basketball':
            self._load_basketball_plays()
        elif self.api_info['sport'] == 'football':
            self._load_drive_data()

    def _load_basketball_plays(self):
        """
        Private method to fetch and assign play-by-play data for a basketball game.

        Uses multi-threaded requests to efficiently load all play pages and converts each play
        item into a `Play` object. The complete list is assigned to `self.plays`.
        """
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_id}/competitions/{self._event_id}/plays'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        def fetch_and_parse_plays(page):
            page_url = url + f'?page={page}'
            play_content = fetch_espn_data(page_url)
            return [
                Play(play_json=play,
                     espn_instance=self._espn_instance,
                     event_instance=self,
                     drive_instance=None)
                for play in play_content.get('items', [])
            ]

        plays = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_and_parse_plays, page) for page in range(1, pages + 1)]
            for future in as_completed(futures):
                try:
                    plays.extend(future.result())
                except Exception as e:
                    print(f"Error fetching plays page: {e}")

        self._plays = plays

    def _load_drive_data(self):
        """
        Private method to fetch and assign drive data for a football game.

        Retrieves all drives associated with the competition and converts each drive item
        into a `Drive` object. The resulting list is stored in `self.drives`.
        """
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_id}/competitions/{self._event_id}/drives'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        def fetch_and_parse_drives(page):
            page_url = url + f'?page={page}'
            drive_content = fetch_espn_data(page_url)
            return [
                Drive(drive_json=drive,
                      espn_instance=self._espn_instance,
                      event_instance=self)
                for drive in drive_content.get('items', [])
            ]

        drives = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_and_parse_drives, page) for page in range(1, pages + 1)]
            for future in as_completed(futures):
                try:
                    drives.extend(future.result())
                except Exception as e:
                    print(f"Error fetching drive data page: {e}")

        self._drives = drives

    def to_dict(self) -> dict:
        """
        Converts the Event instance to its original JSON dictionary.

        Returns:
            dict: The event's raw JSON data.
        """
        return self.event_json


@validate_json('competition_json')
class Competition:

    def __init__(self, competition_json, espn_instance, event_instance):
        self.competition_json = competition_json
        self._espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_competition_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Competition instance.

        Returns:
            str: A formatted string with the events/competition data.
        """
        return f"<Competition | {self.start_date}>"

    def _load_competition_data(self):
        self._id = self.competition_json.get("id")
        self.uid = self.competition_json.get("uid")
        self.date = self.competition_json.get("date")
        self.attendance = self.competition_json.get("attendance")
        self.type = self.competition_json.get("type")  # This might itself be a dict
        self.time_valid = self.competition_json.get("timeValid")
        self.geo_broadcast = self.competition_json.get("geoBroadcast")  # Might be a list of dicts
        self.play_by_play_available = self.competition_json.get("playByPlayAvailable")
        self.play_by_play_source = self.competition_json.get("playByPlaySource")
        self.boxscore_available = self.competition_json.get("boxscoreAvailable")
        self.roster_available = self.competition_json.get("rosterAvailable")
        self.broadcasts = self.competition_json.get("broadcasts")  # Likely a list of dicts
        self.status = self.competition_json.get("status")  # A dict with displayClock, period, etc.
        self.venue = self.event_instance.event_venue
        self.competitors = self.competition_json.get("competitors")  # A list of team info
        self.notes = self.competition_json.get("notes")  # Might be optional
        self.start_date = self.competition_json.get("startDate")
        self.neutral_site = self.competition_json.get("neutralSite")
        self.conference_competition = self.competition_json.get("conferenceCompetition")
        self.recent = self.competition_json.get("recent")
        self.location = self.competition_json.get("location")
        self.weather = self.competition_json.get("weather")  # Optional dict
        self.format = self.competition_json.get("format")
        self.leaders = self.competition_json.get("leaders")  # Usually a list of stats leaders
        self.headlines = self.competition_json.get("headlines")
        self.odds = self.competition_json.get("odds")  # List of betting odds
        self.notes = self.competition_json.get("notes")
        self.tickets = self.competition_json.get("tickets")
        self.group = self.competition_json.get("group")
        self.start_time_tbd = self.competition_json.get("startTimeTBD")
        self.targeting_data = self.competition_json.get("targetingData")
        self.qualifiers = self.competition_json.get("qualifiers")
        self.timeout_format = self.competition_json.get("timeoutFormat")
        self.game_package = self.competition_json.get("gamePackage")
        self.officials = self.competition_json.get('officials')
        self.predictions_available = self.competition_json.get("predictionsAvailable")
        self.clock = self.competition_json.get("clock")
        # nba has series
        self.series = self.competition_json.get('series')

    @property
    def id(self):
        """
            str: the id for the event
        """
        return self._id

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def to_dict(self) -> dict:
        """
        Converts the Competition instance to its original JSON dictionary.

        Returns:
            dict: The competitions's raw JSON data.
        """
        return self.competition_json
