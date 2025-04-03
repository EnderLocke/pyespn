

class Stat:

    def __init__(self, stat_json, espn_isntance):
        self.stat_json = stat_json
        self.espn_instance = espn_isntance

    def _set_stats_data(self):
        self.category = self.stat_json.get('category')
        self.season = self.stat_json.get('season')
        self.player_id = self.stat_json.get('player_id')
        self.stat_value = self.stat_json.get('stat_value')
        self.stat_type_abbreviation = self.stat_json.get('stat_type_abbreviation')
        self.description = self.stat_json.get('description')
        self.name = self.stat_json.get('name')
