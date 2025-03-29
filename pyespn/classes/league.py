# todo create a league version of the api that can pull a certain amount of data
from pyespn.core.decorators import validate_json


@validate_json("league_json")
class League:

    def __init__(self, espn_instance, league_json):
        self.league_json = league_json
        self.espn_instance = espn_instance
        self._set_league_json()

    def __repr__(self):
        """
        Returns a string representation of the betting Provider instance.

        Returns:
            str: A formatted string with the Providers information .
        """
        return f"<League {self.display_name}>"

    def _set_league_json(self):
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
        
        
        