from pyespn.classes.player import Player
from pyespn.utilities import get_athlete_id, get_a_value, fetch_espn_data


class Position:
    """
    Represents a single position on a team's depth chart.

    This class handles parsing and storing player data associated with a
    specific position. It links each player to their appropriate depth
    ranking and pulls detailed player data if it's not already cached
    in the team instance.

    Attributes:
        position_json (dict): Raw JSON data representing the position and its players.
        espn_instance (PYESPN): The ESPN API instance used for data fetching and lookups.
        team_instance (Team): The team object this position belongs to.
        depth_chart (dict): A mapping of depth rank to Player instances.
        ref (str): The reference URL for the position.
        id (int): The ID of the position.
        name (str): The name of the position (e.g., "Quarterback").
        display_name (str): Display-friendly name for the position.
        abbreviation (str): Abbreviation of the position name (e.g., "QB").
        leaf (bool): Indicates whether the position is a terminal (non-group) position.
    """

    def __init__(self, position_json, espn_instance, team_instance):
        """
        Initializes a Position instance and populates the depth chart.

        Args:
            position_json (dict): JSON data representing the position and players.
            espn_instance (PYESPN): Instance of the ESPN API wrapper.
            team_instance (Team): The team this position belongs to.
        """
        self.position_json = position_json
        self._espn_instance = espn_instance
        self.team_instance = team_instance
        self.depth_chart = {}
        self._load_position_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Position instance.

        Returns:
            str: A formatted string with the positions's attributes.
        """
        return f"<Position | {self.abbreviation}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _load_position_data(self):
        """
        Parses the position JSON and builds the depth chart for the position.

        It extracts position metadata and iterates through each listed athlete,
        attempting to retrieve a cached player from the team. If not found, it
        fetches the player data from the ESPN API and instantiates a new Player.

        Players are added to the `depth_chart` dictionary with their depth rank as the key.
        """
        this_json = self.position_json.get('position', {})
        self.ref = this_json.get('$ref')
        self.id = this_json.get('id')
        self.name = this_json.get('name')
        self.display_name = this_json.get('displayName')
        self.abbreviation = this_json.get('abbreviation')
        self.leaf = this_json.get('leaf')
        self.parent_ref = this_json.get('parent', {}).get('$ref')
        rank = 1
        for athlete in self.position_json.get('athletes'):
            athlete_url = athlete.get('athlete', {}).get('$ref')
            athlete_id = get_athlete_id(athlete_url)
            season = get_a_value(url=athlete_url, slug='seasons')
            this_athlete = self.team_instance.get_player_by_season_id(player_id=athlete_id,
                                                                      season=season)
            rank_api = athlete.get('rank')
            slot = athlete.get('slot')
            if this_athlete:
                self.depth_chart[rank] = this_athlete
            else:
                athlete_content = fetch_espn_data(athlete_url)
                self.depth_chart[rank] = Player(player_json=athlete_content,
                                                espn_instance=self.espn_instance)

            rank += 1

    def to_dict(self) -> dict:
        """
        Converts the Position instance to its original JSON dictionary.

        Returns:
            dict: The positions's raw JSON data.
        """
        return self.position_json
