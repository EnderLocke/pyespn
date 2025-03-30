from pyespn.classes.venue import Venue
from pyespn.classes.team import Team
from pyespn.utilities import fetch_espn_data
from pyespn.core.decorators import validate_json


@validate_json("event_json")
class Event:

    def __init__(self, event_json, espn_instance):
        self.event_json = event_json
        self.espn_instance = espn_instance
        self.url_ref = self.event_json.get('$ref')
        self.event_id = self.event_json.get('id')
        self.date = self.event_json.get('date')
        self.event_name = self.event_json.get('name')
        self.short_name = self.event_json.get('shortName')
        self.competition_type = self.event_json.get('competitions', [])[0].get('type', {}).get('type')
        self.venue_json = self.event_json.get('competitions', [])[0].get('venue', {})
        self.event_venue = Venue(venue_json=self.venue_json)
        self.event_notes = self.event_json.get('competitions', [])[0].get('notes', [])
        self.team1 = None
        self.team2 = None
        self._load_teams()

    def _load_teams(self):
        self.team1 = Team(espn_instance=self.espn_instance,
                          team_json=fetch_espn_data(self.event_json.get('competitions', [])[0].get('competitors')[0].get('team', {}).get('$ref')))

        self.team2 = Team(espn_instance=self.espn_instance,
                          team_json=fetch_espn_data(self.event_json.get('competitions', [])[0].get('competitors')[1].get('team', {}).get('$ref')))


    def __repr__(self):
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the events data.
        """
        return f"<Event | {self.short_name} {self.date}>"

    def to_dict(self):
        return self.event_json
