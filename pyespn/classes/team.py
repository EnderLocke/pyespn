
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

    def __init__(self, espn_instance, team_id=None, name=None,
                 abbreviation=None, location=None, team_json=None):
        """
        Initializes a Team instance.

        Args:
            espn_instance (PYESPN): The parent `PYESPN` instance, providing access to league details.
            team_id (int): The unique identifier for the team.
            name (str): The name of the team.
            abbreviation (str): The team's abbreviation.
            location (str): The team's location (e.g., city or state).
        """
        self.espn_instance = espn_instance
        self.team_id = team_id
        self.name = name
        self.abbreviation = abbreviation
        self.location = location
        if team_json:
            self.team_json = team_json
        else:
            self.team_json = None

        if self.team_json:
            self._load_team_data()

    def _load_team_data(self):
        self.id = self.team_json.get("id")
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
        self.venue_name = self.team_json.get("venue", {}).get("fullName", "Unknown Venue")
        self.venue_city = self.team_json.get("venue", {}).get("address", {}).get("city", "Unknown")
        self.venue_state = self.team_json.get("venue", {}).get("address", {}).get("state", "Unknown")
        self.venue_grass = self.team_json.get("venue", {}).get("grass", "Unknown")
        self.venue_indoors = self.team_json.get("venue", {}).get("indoor", "Unknown")
        self.venue_imgs = self.team_json.get("venue", {}).get("images", [])

        self.links = {link["rel"][0]: link["href"] for link in self.team_json.get("links", []) if "rel" in link}

    def get_team_colors(self):
        return {
            'primary_color': self.primary_color,
            'alt_color': self.alternate_color
        }

    def get_home_venue(self):

        return {
            'name': self.venue_name,
            'state': self.venue_state,
            'city': self.venue_city,
            'grass': self.venue_grass,
            'indoor': self.venue_indoors,
            'img_url': self.venue_imgs
        }

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