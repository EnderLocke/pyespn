from pyespn.classes.player import Player
from pyespn.classes.team import Team


class Betting:

    def __init__(self, betting_json):
        self.betting_json = betting_json
        self.providers = []
        self._set_betting_data()

    def _set_betting_data(self):
        self.id = self.betting_json.get('id')
        self.ref = self.betting_json.get('$ref')
        self.name = self.betting_json.get('name')
        self.display_name = self.betting_json.get('displayName')
        for provider in self.betting_json.get('futures'):
            self.providers.append(Provider(provider))


class Provider:

    def __init__(self, line_json):
        self.line_json = line_json
        self._set_betting_provider_data()

    def _set_betting_provider_data(self):
        self.provider_name = self.line_json.get('provider', {}).get('name')
        self.id = self.line_json.get('provider', {}).get('id')
        self.priority = self.line_json.get('provider', {}).get('priority')
        self.active = self.line_json.get('provider', {}).get('active')
        self.all_lines = []
        for future_line in self.line_json.get('books', []):
            self.all_lines.append(Line(future_line))


class Line:

    def __init__(self, book_json):
        self.book_json = book_json
        self.athlete = None
        self.team = None
        self._set_line_data()

    def _set_line_data(self):
        if 'athlete' in self.book_json:
            self.athlete = None
            pass
        if 'team' in self.book_json:
            self.team = None
            pass
        self.value = self.book_json.get('value')


