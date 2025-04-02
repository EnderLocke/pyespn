from pyespn.utilities import get_team_id, fetch_espn_data
from pyespn.classes import Player


class DraftPick:

    def __init__(self, espn_instance, pick_json):
        self.pick_json = pick_json
        self.espn_instance = espn_instance
        self.athlete = None
        self.team = None
        self._get_pick_data()

    def _get_pick_data(self):
        self.round_number = self.pick_json.get('round')
        self.pick_number = self.pick_json.get('pick')
        self.overall_number = self.pick_number.get('overall')
        team_id = get_team_id(self.pick_json.get('team', {}).get('$ref'))
        athlete_url = self.pick_json.get('athlete', {}).get('$ref')
        self.team = self.espn_instance.get_team_by_id(team_id=team_id)

        athlete_content = fetch_espn_data(athlete_url)

        self.athlete = Player(player_json=athlete_content,
                              espn_instance=self.espn_instance)
