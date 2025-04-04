from pyespn.utilities import fetch_espn_data
from pyespn.classes.player import Player
from pyespn.classes.stat import Record


class Standings:

    def __init__(self, standings_json, espn_instance):
        self.standings_json = standings_json
        self.espn_instance = espn_instance
        self.standings = []
        self._load_standings_data()

    def _load_standings_data(self):
        self.standings_type_name = self.standings_json.get('displayName')
        for athlete in self.standings_json.get('standings', []):
            athlete_content = fetch_espn_data(athlete.get('athlete', {}).get('$ref'))
            this_athlete = Player(player_json=athlete_content,
                                  espn_instance=self.espn_instance)
            records = []
            for record in athlete.get('records', []):
                records.append(Record(record_json=record,
                                      espn_instance=self.espn_instance))
            full_athlete = {
                'athlete': this_athlete,
                'record': records
            }

            self.standings.append(full_athlete)
