from pyespn.classes.player import Player
from pyespn.classes.team import Team
from pyespn.utilities import fetch_espn_data
from pyespn.exceptions import API400Error, JSONNotProvidedError
from pyespn.core.decorators import validate_json


@validate_json("betting_json")
class Betting:
    """
    Represents betting data within the ESPN API framework.

    This class encapsulates details about betting providers and their odds.

    Attributes:
        betting_json (dict): The raw JSON data representing the betting details.
        espn_instance (PYESPN): The ESPN API instance for fetching additional data.
        providers (list): A list of `Provider` instances offering betting lines.

    Methods:
        _set_betting_data():
            Parses and stores betting data, including providers.

        __repr__() -> str:
            Returns a string representation of the Betting instance.
    """

    def __init__(self, espn_instance, betting_json: dict):
        """
        Initializes a Betting instance.

        Args:
            espn_instance (PYESPN): The ESPN API instance for API interaction.
            betting_json (dict): The JSON data containing betting information.
        """
        self.betting_json = betting_json
        self.espn_instance = espn_instance
        self.providers = []
        self._set_betting_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Betting instance.

        Returns:
            str: A formatted string with the bettings information .
        """
        return f"<Betting | {self.display_name} - {self.espn_instance.league_abbv}>"

    def _set_betting_data(self):
        """
        Private method to parse and store betting data, including providers.
        """
        self.id = self.betting_json.get('id')
        self.ref = self.betting_json.get('$ref')
        self.name = self.betting_json.get('name')
        self.display_name = self.betting_json.get('displayName')
        for provider in self.betting_json.get('futures'):
            self.providers.append(Provider(espn_instance=self.espn_instance,
                                           line_json=provider))


@validate_json("line_json")
class Provider:
    """
        Represents a betting provider within the ESPN API framework.

        This class stores details about a provider offering betting lines.

        Attributes:
            line_json (dict): The raw JSON data representing the provider.
            espn_instance (PYESPN): The ESPN API instance for fetching additional data.
            provider_name (str): The name of the betting provider.
            id (int): The provider's unique identifier.
            priority (int): The priority level assigned to the provider.
            active (bool): Indicates if the provider is active.
            all_lines (list): A list of `Line` instances representing available bets.

        Methods:
            _set_betting_provider_data():
                Parses and stores provider details, including betting lines.

            __repr__() -> str:
                Returns a string representation of the Provider instance.
        """

    def __init__(self, espn_instance, line_json):
        """
        Initializes a Provider instance.

        Args:
            espn_instance (PYESPN): The ESPN API instance for API interaction.
            line_json (dict): The JSON data containing provider information.
        """
        self.line_json = line_json
        self.espn_instance = espn_instance
        self._set_betting_provider_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the betting Provider instance.

        Returns:
            str: A formatted string with the Providers information .
        """
        return f"<Provider | {self.provider_name} - {self.espn_instance.league_abbv}>"

    def _set_betting_provider_data(self):
        """
        Private method to parse and store provider details, including betting lines.
        """
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
    """
    Represents a betting line within the ESPN API framework.

    This class stores details about a specific betting line, including the associated team
    or athlete.

    Attributes:
        espn_instance (PYESPN): The ESPN API instance for fetching additional data.
        provider_instance (Provider): The provider offering this betting line.
        book_json (dict): The raw JSON data representing the betting line.
        athlete (Player or None): The athlete associated with the betting line, if applicable.
        team (Team or None): The team associated with the betting line, if applicable.
        ref (str): The API reference URL for the athlete or team.
        value (float or None): The betting odds or value.

    Methods:
        _set_line_data():
            Parses and stores betting line details.

        __repr__() -> str:
            Returns a string representation of the Betting Line instance.
    """

    def __init__(self, espn_instance, provider_instance: Provider, book_json: dict):
        """
        Initializes a Line instance.

        Args:
            espn_instance (PYESPN): The ESPN API instance for API interaction.
            provider_instance (Provider): The betting provider for this line.
            book_json (dict): The JSON data containing betting line details.
        """
        self.espn_instance = espn_instance
        self.provider_instance = provider_instance
        self.book_json = book_json
        self.athlete = None
        self.team = None
        self.ref = None
        self._set_line_data()

    def __repr__(self) -> str:
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
        """
        Private method to parse and store betting line details, including associated teams or athletes.
        """
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

