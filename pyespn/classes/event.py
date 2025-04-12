from pyespn.core.decorators import validate_json
from pyespn.classes.betting import GameOdds
from pyespn.classes.gamelog import Drive, Play
from pyespn.utilities import fetch_espn_data, lookup_league_api_info, get_an_id
from pyespn.data.version import espn_api_version as v


@validate_json("event_json")
class Event:
    """
    Represents a sports event within the ESPN API framework.

    This class encapsulates event details such as the event's name, date, venue,
    and the competing teams.

    Attributes:
        event_json (dict): The raw JSON data representing the event.
        espn_instance (PYESPN): The ESPN API instance for fetching additional data.
        url_ref (str): The API reference URL for the event.
        event_id (int): The unique identifier of the event.
        date (str): The date of the event.
        event_name (str): The full name of the event.
        short_name (str): The short name or abbreviation of the event.
        competition_type (str): The type of competition (e.g., "regular", "playoff").
        venue_json (dict): The raw JSON data representing the event venue.
        event_venue (Venue): A `Venue` instance representing the event's location.
        event_notes (list): Additional notes about the event.
        home_team (Team or None): The first competing team, initialized after `_load_teams()` runs.
        away_team (Team or None): The second competing team, initialized after `_load_teams()` runs.

    Methods:
        _load_teams():
            Fetches and assigns the competing teams using API references.

        to_dict() -> dict:
            Returns the raw JSON representation of the event.

    """

    def __init__(self, event_json: dict, espn_instance):
        """
        Initializes an Event instance with the provided JSON data.

        Args:
            event_json (dict): The JSON data containing event details.
            espn_instance (PYESPN): The parent `PYESPN` instance for API interaction.
        """
        from pyespn.classes.venue import Venue
        self.competition = None
        self.event_json = event_json
        self.espn_instance = espn_instance
        self.url_ref = self.event_json.get('$ref')
        self.event_id = self.event_json.get('id')
        self.date = self.event_json.get('date')
        self.event_name = self.event_json.get('name')
        self.short_name = self.event_json.get('shortName')
        self.competition_type = self.event_json.get('competitions', [])[0].get('type', {}).get('type')
        self.venue_json = self.event_json.get('competitions', [])[0].get('venue', {})
        self.event_venue = Venue(venue_json=self.venue_json,
                                 espn_instance=self.espn_instance)
        self.event_notes = self.event_json.get('competitions', [])[0].get('notes', [])
        self.home_team = None
        self.away_team = None
        self.odds = None
        self.drives = None
        self.plays = None
        self.api_info = lookup_league_api_info(league_abbv=self.espn_instance.league_abbv)
        self._load_teams()
        self._load_competition_data()
        self._load_betting_odds()
        self._load_play_by_play()

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
            self.home_team = self.espn_instance.get_team_by_id(team1_id)

            self.away_team = self.espn_instance.get_team_by_id(team2_id)
        else:
            self.home_team = self.espn_instance.get_team_by_id(team2_id)

            self.away_team = self.espn_instance.get_team_by_id(team1_id)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the events data.
        """
        return f"<Event | {self.short_name} {self.date}>"

    def _load_betting_odds(self):
        url = f'http://sports.core.api.espn.com/{v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self.event_id}/competitions/{self.event_id}/odds'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        event_odds = []
        for page in range(1, pages + 1):
            page_url = url + f'?page={page}'
            odds_content = fetch_espn_data(page_url)
            for odd in odds_content.get('items', []):
                event_odds.append(GameOdds(odds_json=odd,
                                           espn_instance=self.espn_instance,
                                           event_instance=self))
        self.odds = event_odds

    def _load_competition_data(self):
        url = f'http://sports.core.api.espn.com/{v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self.event_id}/competitions/{self.event_id}'
        competition_content = fetch_espn_data(url)

        self.competition = Competition(competition_json=competition_content,
                                       espn_instance=self.espn_instance,
                                       event_instance=self)

    def _load_play_by_play(self):
        if self.api_info['sport'] == 'basketball':
            self._load_basketball_plays()
        elif self.api_info['sport'] == 'football':
            self._load_drive_data()

    def _load_basketball_plays(self):
        url = f'http://sports.core.api.espn.com/{v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self.event_id}/competitions/{self.event_id}/plays'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        plays = []
        for page in range(1, pages + 1):
            page_url = url + f'?page={page}'
            play_content = fetch_espn_data(page_url)
            for play in play_content.get('items', []):
                plays.append(Play(play_json=play,
                                  espn_instance=self.espn_instance,
                                  event_instance=self,
                                  drive_instance=None))

        self.plays = plays

    def _load_drive_data(self):
        url = f'http://sports.core.api.espn.com/{v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self.event_id}/competitions/{self.event_id}/drives'
        page_content = fetch_espn_data(url)
        pages = page_content.get('pageCount', 0)

        drives = []
        for page in range(1, pages + 1):
            page_url = url + f'?page={page}'
            drive_content = fetch_espn_data(page_url)
            for drive in drive_content.get('items', []):
                drives.append(Drive(drive_json=drive,
                                    espn_instance=self.espn_instance,
                                    event_instance=self))

        self.drives = drives

    def to_dict(self) -> dict:
        """
        Converts the Event instance to its original JSON dictionary.

        Returns:
            dict: The event's raw JSON data.
        """
        return self.event_json


class Competition:

    def __init__(self, competition_json, espn_instance, event_instance):
        self.competition_json = competition_json
        self.espn_instance = espn_instance
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
        self.id = self.competition_json.get("id")
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

