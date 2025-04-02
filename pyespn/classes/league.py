from pyespn.core.decorators import validate_json


@validate_json("league_json")
class League:
    """
    Represents a sports league with associated details, such as teams, events, and rankings.

    Attributes:
        espn_instance (PyESPN): The ESPN API instance used to fetch data.
        league_json (dict): The raw JSON data representing the league.
        ref (str): The reference ID of the league.
        id (str): The unique ID of the league.
        name (str): The name of the league.
        display_name (str): The display name of the league.
        abbreviation (str): The abbreviation of the league.
        short_name (str): The short name of the league.
        slug (str): A URL-friendly string for the league.
        is_tournament (bool): Flag indicating if the league is a tournament.
        season (dict): The current season details for the league.
        seasons (list): A list of seasons for the league.
        franchises (list): A list of franchises in the league.
        teams (list): A list of teams participating in the league.
        group (dict): The group associated with the league.
        groups (list): A list of groups in the league.
        events (list): A list of events related to the league.
        notes (str): Additional notes about the league.
        rankings (list): Rankings of teams or players within the league.
        draft (dict): The draft details of the league.
        links (list): Hyperlinks associated with the league's data.

    Methods:
        __repr__(): Returns a string representation of the League instance.
        _set_league_json(): Populates the attributes of the League instance from the given JSON.
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
        
        
        