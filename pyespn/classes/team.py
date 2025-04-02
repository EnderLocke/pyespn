from pyespn.classes.venue import Venue
from pyespn.core.decorators import validate_json


# todo can add a load roster function etc
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
            abbreviation (str | None): The team's short abbreviation (e.g., "NYG", "LAL").
            display_name (str | None): The full display name of the team.
            short_display_name (str | None): A shorter version of the display name.
            primary_color (str | None): The team's primary color (hex code).
            alternate_color (str | None): The team's alternate color (hex code).
            is_active (bool | None): Indicates whether the team is currently active.
            is_all_star (bool | None): Indicates if the team is an all-star team.
            logos (list[str]): A list of URLs to the team’s logos.
            venue_json (dict): The raw venue data associated with the team.
            home_venue (Venue): The `Venue` instance representing the team's home venue.
            links (dict): A dictionary mapping link types (e.g., "official site") to their URLs.

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
        if team_json:
            self.team_json = team_json
        else:
            self.team_json = {}
        self._load_team_data()
        self.home_venue = Venue(venue_json=self.venue_json)

    def _load_team_data(self):
        """
        Extracts and sets team data from the provided JSON.
        """
        #self.ref = self.team_json.get('$ref')
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

    def get_logo_img(self) -> list[str]:
        """
        Retrieves the list of logo URLs associated with the team.

        Returns:
            list[str]: A list of URLs to the team's logos.
        """
        return self.home_venue.images

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
            str: The league abbreviation (e.g., "nfl", "nba", "cfb").
        """
        return self.espn_instance.league_abbv

    def __repr__(self) -> str:
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the team's location, name, abbreviation, and league.
        """
        return f"<Team | {self.location} {self.name} ({self.abbreviation}) - {self.get_league()}>"

    def to_dict(self) -> dict:
        """
        Returns the raw team JSON data as a dictionary.

        Returns:
            dict: The original team data retrieved from the ESPN API.
        """
        return self.team_json
