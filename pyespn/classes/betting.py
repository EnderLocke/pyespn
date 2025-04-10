from pyespn.utilities import fetch_espn_data, get_team_id, get_athlete_id, camel_to_snake
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

    def __init__(self, espn_instance, season, betting_json: dict):
        """
        Initializes a Betting instance.

        Args:
            espn_instance (PYESPN): The ESPN API instance for API interaction.
            betting_json (dict): The JSON data containing betting information.
        """
        self.betting_json = betting_json
        self.espn_instance = espn_instance
        self.season = season
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
                                           betting_instance=self,
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

    def __init__(self, espn_instance, betting_instance, line_json):
        """
        Initializes a Provider instance.

        Args:
            espn_instance (PYESPN): The ESPN API instance for API interaction.
            line_json (dict): The JSON data containing provider information.
        """
        self.line_json = line_json
        self.espn_instance = espn_instance
        self.betting_instance = betting_instance
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
            msg += f'{self.athlete.full_name} | {self.value}'

        return f"<Betting Line: {msg}>"

    def _set_line_data(self):
        """
        Private method to parse and store betting line details, including associated teams or athletes.
        """
        from pyespn.classes.player import Player
        from pyespn.classes.team import Team
        try:
            if 'athlete' in self.book_json:
                athlete_id = get_athlete_id(self.book_json.get('athlete', {}).get('$ref'))
                self.athlete = self.espn_instance.check_teams_for_player_by_season(season=self.provider_instance.betting_instance.season,
                                                                                   player_id=athlete_id)
                if not self.athlete:

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
        except API400Error as e:
            print(f'api error {e}')
        except JSONNotProvidedError as e:
            print(f'json error {e}')


class GameOdds:

    def __init__(self, odds_json, espn_instance, event_instance):
        self.odds_json = odds_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_odds_data()

    def __repr__(self):
        """
        Returns a string representation of the GameOdds instance.
        """
        return f"<GameOdds | {self.provider}>"

    def _load_odds_data(self):
        self.provider = self.odds_json.get('provider', {}).get('name', 'unknown')
        self.over_under = self.odds_json.get('overUnder')
        self.details = self.odds_json.get('details')
        self.spread = self.odds_json.get('spread')
        self.over_odds = self.odds_json.get('overOdds')
        self.under_odds = self.odds_json.get('underOdds')
        self.money_line_winner = self.odds_json.get('moneylineWinner')
        self.spread_winner = self.odds_json.get("spreadWinner")
        self.away_team_odds = Odds(odds_json=self.odds_json.get('awayTeamOdds'),
                                   espn_instance=self.espn_instance,
                                   event_instance=self.event_instance)
        self.home_team_odds = Odds(odds_json=self.odds_json.get('homeTeamOdds'),
                                   espn_instance=self.espn_instance,
                                   event_instance=self.event_instance)
        # todo do i need this
        self.open = BetValue(bet_name='open',
                             bet_json=self.odds_json.get('open'),
                             espn_instance=self.espn_instance)
        self.close = BetValue(bet_name='close',
                              bet_json=self.odds_json.get('close'),
                              espn_instance=self.espn_instance)
        self.current = BetValue(bet_name='current',
                                bet_json=self.odds_json.get('close'),
                                espn_instance=self.espn_instance)

class OddsType:

    def __init__(self, odds_name, odds_type_json, espn_instance):
        self.name = odds_name
        self.odds_type_json = odds_type_json
        self.espn_instance = espn_instance
        self.odds = {}
        self._load_odds_type_data()

    def __repr__(self):
        """
        Returns a string representation of the OddsType instance.
        """
        return f"<OddsType | {self.name}>"

    def _load_odds_type_data(self):
        self.odds['point_spread'] = BetValue(bet_name='point_spread',
                                             bet_json=self.odds_type_json.get('pointSpread', {}),
                                             espn_instance=self.espn_instance)
        self.odds['spread'] = BetValue(bet_name='spread',
                                       bet_json=self.odds_type_json.get('spread', {}),
                                       espn_instance=self.espn_instance)
        self.odds['money_line'] = BetValue(bet_name='money_line',
                                           bet_json=self.odds_type_json.get('moneyLine', {}),
                                           espn_instance=self.espn_instance)


class Odds:

    def __init__(self, odds_json, espn_instance, event_instance):
        self.odds_json = odds_json
        self.espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_odds_json()

    def __repr__(self):
        """
        Returns a string representation of the Odds instance.
        """
        return f"<Odds | {self.team.name}>"

    def _load_odds_json(self):
        self.favorite = self.odds_json.get('favorite')
        self.underdog = self.odds_json.get('underdog')
        self.money_line = self.odds_json.get('moneyLine')
        self.spread_odds = self.odds_json.get('spreadOdds')
        team_id = get_team_id(self.odds_json.get('team', {}).get('$ref'))
        self.team = self.espn_instance.get_team_by_id(team_id=team_id)
        self.open = OddsType(odds_name='open',
                             odds_type_json=self.odds_json.get('open'),
                             espn_instance=self.espn_instance)
        self.close = OddsType(odds_name='close',
                              odds_type_json=self.odds_json.get('close'),
                              espn_instance=self.espn_instance)
        self.current = OddsType(odds_name='current',
                                odds_type_json=self.odds_json.get('current'),
                                espn_instance=self.espn_instance)


class BetValue:

    def __init__(self, bet_name, bet_json, espn_instance):
        self.name = bet_name
        self.bet_json = bet_json
        self.espn_instance = espn_instance
        self._load_bet_data()

    def __repr__(self):
        """
        Returns a string representation of the BetValue instance.
        """
        return f"<BetValue | {self.name}>"

    def _load_bet_data(self):
        for key, value in self.bet_json.items():
            snake_key = camel_to_snake(key)
            setattr(self, snake_key, value)

