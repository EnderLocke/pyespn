from pyespn.classes.player import Player
from pyespn.classes.team import Team
from pyespn.utilities import fetch_espn_data
from pyespn.exceptions import API400Error, JSONNotProvidedError
from pyespn.core.decorators import validate_json


@validate_json("betting_json")
class Betting:

    def __init__(self, espn_instance, betting_json):
        self.betting_json = betting_json
        self.espn_instance = espn_instance
        self.providers = []
        self._set_betting_data()

    def __repr__(self):
        """
        Returns a string representation of the Betting instance.

        Returns:
            str: A formatted string with the bettings information .
        """
        return f"<Betting {self.display_name} - {self.espn_instance.league_abbv}>"

    def _set_betting_data(self):
        self.id = self.betting_json.get('id')
        self.ref = self.betting_json.get('$ref')
        self.name = self.betting_json.get('name')
        self.display_name = self.betting_json.get('displayName')
        for provider in self.betting_json.get('futures'):
            self.providers.append(Provider(espn_instance=self.espn_instance,
                                           line_json=provider))


@validate_json("line_json")
class Provider:

    def __init__(self, espn_instance, line_json):
        self.line_json = line_json
        self.espn_instance = espn_instance
        self._set_betting_provider_data()

    def __repr__(self):
        """
        Returns a string representation of the betting Provider instance.

        Returns:
            str: A formatted string with the Providers information .
        """
        return f"<Provider {self.provider_name} - {self.espn_instance.league_abbv}>"

    def _set_betting_provider_data(self):
        self.provider_name = self.line_json.get('provider', {}).get('name')
        self.id = self.line_json.get('provider', {}).get('id')
        self.priority = self.line_json.get('provider', {}).get('priority')
        self.active = self.line_json.get('provider', {}).get('active')
        self.all_lines = []
        for future_line in self.line_json.get('books', []):
            self.all_lines.append(Line(espn_instance=self.espn_instance,
                                       provider_instance=self,
                                       book_json=future_line))


@validate_json("book_json")
class Line:

    def __init__(self, espn_instance, provider_instance, book_json):
        self.espn_instance = espn_instance
        self.provider_instance = provider_instance
        self.book_json = book_json
        self.athlete = None
        self.team = None
        self.ref = None
        self._set_line_data()

    def __repr__(self):
        """
        Returns a string representation of the Betting Line instance.

        Returns:
            str: A formatted string with the bettings line information .
        """

        msg = ''

        if self.team:
            msg += f'{self.team.name} | {self.value}'

        if self.athlete:
            msg += f'{self.athlete.name} | {self.value}'

        return f"<Betting Line: {msg}>"

    def _set_line_data(self):
        try:
            if 'athlete' in self.book_json:
                self.ref = self.book_json.get('athlete').get('$ref')
                content = fetch_espn_data(self.ref)

                self.athlete = Player(espn_instance=self.espn_instance,
                                      player_json=content)

            if 'team' in self.book_json:
                self.ref = self.book_json.get('team').get('$ref')
                content = fetch_espn_data(self.ref)

                self.team = Team(espn_instance=self.espn_instance,
                                 team_json=content)

            self.value = self.book_json.get('value')
        except (API400Error, JSONNotProvidedError) as e:
            pass

