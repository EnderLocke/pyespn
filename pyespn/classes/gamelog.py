from pyespn.utilities import fetch_espn_data, get_team_id


class Drive:

    def __init__(self, drive_json, espn_instance, event_instance):
        self.drive_json = drive_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self.plays = None
        self._load_drive_data()

    def __repr__(self):
        """
        Returns a string representation of the Drive instance.
        """
        return f"<Drive | {self.team.name} | {self.result_display}>"

    def _load_drive_data(self):
        self.description = self.drive_json.get('description')
        self.id = self.drive_json.get('id')
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
        self.plays_ref = self.drive_json.get('plays', {}).get('$ref')
        plays = []
        for play in self.drive_json.get('plays', {}).get('items'):
            plays.append(Play(play_json=play,
                              espn_instance=self.espn_instance,
                              event_instance=self.event_instance,
                              drive_instance=self))
        self.plays = plays


class Play:

    def __init__(self, play_json, espn_instance, event_instance,
                 drive_instance):
        self.play_json = play_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self.drive_instance = drive_instance
        self._load_play_data()

    def __repr__(self):
        """
        Returns a string representation of the Play instance.
        """
        return f"<Play | {self.team.name} | {self.short_text}>"

    def _load_play_data(self):
        self.ref = self.play_json.get('$ref')
        self.id = self.play_json.get('id')
        self.text = self.play_json.get('text')
        self.alt_text = self.play_json.get('alternativeText')
        self.short_text = self.play_json.get('shortText')
        self.home_score = self.play_json.get('homeScore')
        self.away_score = self.play_json.get('awayScore')
        self.sequence_number = self.play_json.get('sequenceNumber')
        self.type = self.play_json.get('type')
        self.short_alt_text = self.play_json.get('shortAlternativeText')
        self.period = self.play_json.get('period')
        self.clock = self.play_json.get('clock')
        self.scoring_play = self.play_json.get('scoringPlay')
        self.priority = self.play_json.get('priority')
        self.score_value = self.play_json.get('scoreValue')
        self.start = self.play_json.get('start')
        self.end = self.play_json.get('end')
        self.wallclock = self.play_json.get('wallclock')
        self.modified = self.play_json.get('modified')
        # todo this is probably its own class
        self.probability = self.play_json.get('probability')
        self.stat_yardage = self.play_json.get('statYardage')
        team_id = get_team_id(self.play_json.get('team', {}).get('$ref'))
        self.team = self.espn_instance.get_team_by_id(team_id=team_id)
        # todo these look like a list of athletes
        self.participants = self.play_json.get('participants')



class PlayType:

    def __init__(self):
        pass



