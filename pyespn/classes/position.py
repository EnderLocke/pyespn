from pyespn.classes.player import Player
from pyespn.utilities import get_athlete_id, get_a_value, fetch_espn_data


class Position:

    def __init__(self, position_json, espn_instance, team_instance):
        self.position_json = position_json
        self.espn_instance = espn_instance
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

    def _load_position_data(self):
        this_json = self.position_json.get('position', {})
        self.ref = this_json.get('$ref')
        self.id = this_json.get('id')
        self.name = this_json.get('name')
        self.display_name = this_json.get('displayName')
        self.abbreviation = this_json.get('abbreviation')
        self.leaf = this_json.get('leaf')
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

