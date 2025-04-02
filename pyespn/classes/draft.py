from pyespn.utilities import get_team_id, fetch_espn_data
from pyespn.classes import Player


class DraftPick:
    """
    Represents a draft pick in a sports league draft.

    Attributes:
        pick_json (dict): The raw JSON data representing the draft pick.
        espn_instance (PyESPN): The ESPN API instance for fetching related data.
        athlete (Player or None): The Player instance representing the drafted athlete.
        team (Team or None): The Team instance representing the team that made the pick.
        round_number (int or None): The round in which the pick was made.
        pick_number (int or None): The pick number within the round.
        overall_number (int or None): The overall pick number in the draft.

    Methods:
        __repr__(): Returns a string representation of the DraftPick instance.
        _get_pick_data(): Extracts and sets relevant data from the draft pick JSON.
    """

    def __init__(self, espn_instance, pick_json):
        """
        Initializes a DraftPick instance with data from the provided JSON.

        Args:
            espn_instance (PyESPN): The ESPN API instance.
            pick_json (dict): The raw JSON data representing the draft pick.
        """

        self.pick_json = pick_json
        self.espn_instance = espn_instance
        self.athlete = None
        self.team = None
        self._get_pick_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the draftpick instance.

        Returns:
            str: A formatted string with class details
        """
        return f"<DraftPick | Round {self.round_number} - Pick {self.pick_number}>"

    def _get_pick_data(self):
        """
        Extracts and sets relevant data from the draft pick JSON.
        """
        self.round_number = self.pick_json.get('round')
        self.pick_number = self.pick_json.get('pick')
        self.overall_number = self.pick_json.get('overall')
        team_id = get_team_id(self.pick_json.get('team', {}).get('$ref'))
        athlete_url = self.pick_json.get('athlete', {}).get('$ref')
        self.team = self.espn_instance.get_team_by_id(team_id=team_id)

        athlete_content = fetch_espn_data(athlete_url)

        self.athlete = Player(player_json=athlete_content,
                              espn_instance=self.espn_instance)
