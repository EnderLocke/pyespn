from pyespn.classes.player import Player
from pyespn.classes.team import Team
from pyespn.utilities import fetch_espn_data


class Betting:

    def __init__(self, espn_instance, betting_json):
        self.betting_json = betting_json
        self.espn_instance = espn_instance
        self.providers = []
        self._set_betting_data()

    def _set_betting_data(self):
        self.id = self.betting_json.get('id')
        self.ref = self.betting_json.get('$ref')
        self.name = self.betting_json.get('name')
        self.display_name = self.betting_json.get('displayName')
        for provider in self.betting_json.get('futures'):
            self.providers.append(Provider(espn_instance=self.espn_instance,
                                           line_json=provider))


class Provider:

    def __init__(self, espn_instance, line_json):
        self.line_json = line_json
        self.espn_instance = espn_instance
        self._set_betting_provider_data()

    def _set_betting_provider_data(self):
        self.provider_name = self.line_json.get('provider', {}).get('name')
        self.id = self.line_json.get('provider', {}).get('id')
        self.priority = self.line_json.get('provider', {}).get('priority')
        self.active = self.line_json.get('provider', {}).get('active')
        self.all_lines = []
        for future_line in self.line_json.get('books', []):
            self.all_lines.append(Line(espn_instance=self.espn_instance,
                                       book_json=future_line))


class Line:

    def __init__(self, espn_instance, book_json):
        self.espn_instance = espn_instance
        self.book_json = book_json
        self.athlete = None
        self.team = None
        self._set_line_data()

    def _set_line_data(self):
        if 'athlete' in self.book_json:
            content = fetch_espn_data(self.book_json.get('athlete').get('$ref'))

            self.athlete = Player(espn_instance=self.espn_instance,
                                  player_json=content)

        if 'team' in self.book_json:
            content = fetch_espn_data(self.book_json.get('team').get('$ref'))

            self.team = Team(espn_instance=self.espn_instance,
                             team_json=content)

        self.value = self.book_json.get('value')


