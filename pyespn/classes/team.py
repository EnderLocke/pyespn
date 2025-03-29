from pyespn.classes.venue import Venue
from pyespn.core.decorators import validate_json


@validate_json("team_json")
class Team:
    """
    Represents a sports team within the ESPN API framework.

    This class is designed to store team-related information while maintaining a reference 
    to a `PYESPN` instance, allowing access to league-specific details.

    Attributes:
        espn_instance (PYESPN): Reference to the parent `PYESPN` instance.
        team_id (int): Unique identifier for the team.
        name (str): Full name of the team.
        abbreviation (str): Team abbreviation (e.g., "LAL" for Los Angeles Lakers).
        location (str): Geographic location of the team (e.g., "Los Angeles").
    """

    def __init__(self, espn_instance, team_json):
        """
        Initializes a Team instance.

        Args:
            espn_instance (PYESPN): The parent `PYESPN` instance, providing access to league details.
        """
        self.espn_instance = espn_instance
        if team_json:
            self.team_json = team_json
        else:
            self.team_json = {}
        self._load_team_data()
        self.home_venue = Venue(venue_json=self.venue_json)

    def _load_team_data(self):
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

        self.logos = [logo.get("href") for logo in self.team_json.get("logos", [])]
        self.venue_json = self.team_json.get("venue", {})

        self.links = {link["rel"][0]: link["href"] for link in self.team_json.get("links", []) if "rel" in link}

    def get_logo_img(self):
        return self.home_venue.images

    def get_team_colors(self):
        return {
            'primary_color': self.primary_color,
            'alt_color': self.alternate_color
        }

    def get_home_venue(self):

        return self.home_venue

    def get_league(self):
        """
        Retrieves the league abbreviation from the associated `PYESPN` instance.

        Returns:
            str: The league abbreviation (e.g., "nfl", "nba", "cfb").
        """
        return self.espn_instance.league_abbv

    def __repr__(self):
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the team's location, name, abbreviation, and league.
        """
        return f"<Team {self.location} {self.name} ({self.abbreviation}) - {self.get_league()}>"

    def to_dict(self):
        return self.team_json
