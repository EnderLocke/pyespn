from pyespn.classes.venue import Venue
from pyespn.classes.team import Team
from pyespn.core.decorators import validate_json


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
        self._load_teams()

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

    def to_dict(self) -> dict:
        """
        Converts the Event instance to its original JSON dictionary.

        Returns:
            dict: The event's raw JSON data.
        """
        return self.event_json
