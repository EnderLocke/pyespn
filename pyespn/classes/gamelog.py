from pyespn.utilities import fetch_espn_data, get_team_id


class Drive:

    def __init__(self, drive_json, espn_instance, event_instance):
        self.drive_json = drive_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_drive_data()

    def _load_drive_data(self):
        self.description = self.drive_json.get('description')
        self.drive_id = self.drive_json.get('id')
        self.sequence_number = self.drive_json.get('sequence_number')
        self.ref = self.drive_json.get('$ref')
        self.start = self.drive_json.get('start')
        self.end = self.drive_json.get('end')
        self.time_elapsed = self.drive_json.get('timeElapsed')
        self.yards = self.drive_json.get('yards')
        self.is_score = self.drive_json.get('isScore')
        self.offensive_plays = self.drive_json.get('offensivePlays')
        self.result = self.drive_json.get('result')
        self.result_display = self.drive_json.get('displayResult')
        team_id = get_team_id(self.drive_json.get('team', {}).get('$ref'))
        self.team = self.espn_instance.get_team_by_id(team_id=team_id)
        end_team_id = get_team_id(self.drive_json.get('endTeam', {}).get('$ref'))
        self.end_team = self.espn_instance.get_team_by_id(team_id=end_team_id)

    def load_plays(self):
       pass


class Play:

    def __init__(self, play_json, espn_instance, event_instance):
        self.play_json = play_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_play_data()

    def _load_play_data(self):
        pass


