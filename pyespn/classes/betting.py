from pyespn.utilities import fetch_espn_data, get_team_id, get_athlete_id, camel_to_snake
from pyespn.exceptions import API400Error, JSONNotProvidedError
from pyespn.core.decorators import validate_json
STANDARDIZED_BETTING_PROVIDERS = ['ESPN BET', 'ESPN Bet - Live Odds']


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
        self._espn_instance = espn_instance
        self.season = season
        self.providers = []
        self._set_betting_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Betting instance.

        Returns:
            str: A formatted string with the bettings information .
        """
        return f"<Betting | {self.display_name} - {self._espn_instance.league_abbv}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _set_betting_data(self):
        """
        Private method to parse and store betting data, including providers.
        """
        self.id = self.betting_json.get('id')
        self.ref = self.betting_json.get('$ref')
        self.name = self.betting_json.get('name')
        self.display_name = self.betting_json.get('displayName')
        for provider in self.betting_json.get('futures'):
            self.providers.append(Provider(espn_instance=self._espn_instance,
                                           betting_instance=self,
                                           line_json=provider))

    def to_dict(self) -> dict:
        """
        Converts the Betting instance to its original JSON dictionary.

        Returns:
            dict: The betting's raw JSON data.
        """
        return self.betting_json


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
        self._espn_instance = espn_instance
        self.betting_instance = betting_instance
        self._set_betting_provider_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the betting Provider instance.

        Returns:
            str: A formatted string with the Providers information .
        """
        return f"<Provider | {self.provider_name} - {self._espn_instance.league_abbv}>"

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
            self.all_lines.append(Line(espn_instance=self._espn_instance,
                                       provider_instance=self,
                                       book_json=future_line))

    def to_dict(self) -> dict:
        """
        Converts the Provider instance to its original JSON dictionary.

        Returns:
            dict: The providers's raw JSON data.
        """
        return self.line_json


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
        self._espn_instance = espn_instance
        self.provider_instance = provider_instance
        self.book_json = book_json
        self.athlete = None
        self.team = None
        self.ref = None
        self._set_line_data()

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

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
                self.athlete = self._espn_instance.check_teams_for_player_by_season(season=self.provider_instance.betting_instance.season,
                                                                                   player_id=athlete_id)
                if not self.athlete:

                    self.ref = self.book_json.get('athlete').get('$ref')
                    content = fetch_espn_data(self.ref)

                    self.athlete = Player(espn_instance=self._espn_instance,
                                          player_json=content)

            if 'team' in self.book_json:
                self.ref = self.book_json.get('team').get('$ref')
                content = fetch_espn_data(self.ref)

                self.team = Team(espn_instance=self._espn_instance,
                                 team_json=content)

            self.value = self.book_json.get('value')
        except API400Error as e:
            print(f'api error {e}')
        except JSONNotProvidedError as e:
            print(f'json error {e}')

    def to_dict(self) -> dict:
        """
        Converts the Line instance to its original JSON dictionary.

        Returns:
            dict: The lines's raw JSON data.
        """
        return self.book_json


class GameOdds:
    """
    Represents the overall betting odds for a specific game/event.

    This class handles parsing and organizing odds data from various providers, including
    standardized ones (like ESPN BET) and custom formats (like Bet365). It creates instances
    of `Odds`, `OddsBet365`, and `BetValue` to model the odds for home and away teams.

    Attributes:
        odds_json (dict): Raw JSON data containing odds information.
        espn_instance (PYESPN): The ESPN API instance used for team lookups and related methods.
        event_instance (Event): The parent event associated with these odds.
        provider (str): Name of the odds provider.
        over_under (float or None): The total points line for the game.
        details (str or None): Any extra details provided with the odds.
        spread (float or None): The point spread for the game.
        over_odds (float or None): Odds associated with the over.
        under_odds (float or None): Odds associated with the under.
        money_line_winner (str or None): The team favored in the moneyline bet.
        spread_winner (str or None): The team favored against the spread.
        home_team_odds (Odds or OddsBet365): Odds object for the home team.
        away_team_odds (Odds or OddsBet365): Odds object for the away team.
        open (BetValue, optional): Opening odds.
        current (BetValue, optional): Current odds.
        close (BetValue, optional): Closing odds (if available for provider).
    """

    def __init__(self, odds_json, espn_instance, event_instance):
        """
        Initializes a GameOdds instance with raw odds data.

        Args:
            odds_json (dict): The JSON data representing odds for the event.
            espn_instance (PYESPN): The ESPN API interface for additional data lookups.
            event_instance (Event): The associated Event instance.
        """

        self.odds_json = odds_json
        self._espn_instance = espn_instance
        self.event_instance = event_instance
        self._load_odds_data()

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def __repr__(self) -> str:
        """
        Returns a string representation of the GameOdds instance.

        Returns:
            str: A formatted string showing the odds provider name.
        """
        return f"<GameOdds | {self.provider}>"

    def _load_odds_data(self):
        """
        Parses and loads odds data from the input JSON.

        Handles both standardized providers (like ESPN BET) and
        provider-specific formats (like Bet 365). Assigns odds for
        home and away teams and loads line details such as over/under,
        spread, moneyline, and BetValue objects for open/current/close odds.
        """
        self.provider = self.odds_json.get('provider', {}).get('name', 'unknown')
        self.over_under = self.odds_json.get('overUnder')
        self.details = self.odds_json.get('details')
        self.spread = self.odds_json.get('spread')
        self.over_odds = self.odds_json.get('overOdds')
        self.under_odds = self.odds_json.get('underOdds')
        self.money_line_winner = self.odds_json.get('moneylineWinner')
        self.spread_winner = self.odds_json.get("spreadWinner")

        if self.provider not in STANDARDIZED_BETTING_PROVIDERS:
            if self.provider == 'Bet 365':
                away_dicts = {}
                home_dicts = {}
                other_dicts = {}
                home_team = self._espn_instance.get_team_by_id(get_team_id(self.odds_json.get('bettingOdds', {}).get('homeTeam', {}).get('$ref')))
                away_team = self._espn_instance.get_team_by_id(get_team_id(self.odds_json.get('bettingOdds', {}).get('awayTeam', {}).get('$ref')))

                for key, value in self.odds_json.get('bettingOdds', {}).get('teamOdds', {}).items():
                    if 'home' in str(key).lower():
                        home_dicts.setdefault(key, value)
                    elif 'away' in str(key).lower():
                        away_dicts.setdefault(key, value)
                    else:
                        other_dicts.setdefault(key,value)
                self.away_team_odds = OddsBet365(odds_json=away_dicts,
                                                 espn_instance=self._espn_instance,
                                                 event_instance=self.event_instance,
                                                 gameodds_instance=self,
                                                 team=away_team)
                self.home_team_odds = OddsBet365(odds_json=home_dicts,
                                                 espn_instance=self._espn_instance,
                                                 event_instance=self.event_instance,
                                                 gameodds_instance=self,
                                                 team=home_team)
                #print('bet 365 not fully integrated yet')
            else:
                print(f'the provider is {self.provider}')
        else:
            if self.provider == 'ESPN Bet - Live Odds':
                pass
            self.away_team_odds = Odds(odds_json=self.odds_json.get('awayTeamOdds'),
                                       espn_instance=self._espn_instance,
                                       event_instance=self.event_instance,
                                       gameodds_instance=self)
            self.home_team_odds = Odds(odds_json=self.odds_json.get('homeTeamOdds'),
                                       espn_instance=self._espn_instance,
                                       event_instance=self.event_instance,
                                       gameodds_instance=self)
            self.open = BetValue(bet_name='open',
                                 bet_json=self.odds_json.get('open'),
                                 espn_instance=self._espn_instance)
            self.current = BetValue(bet_name='current',
                                    bet_json=self.odds_json.get('current'),
                                    espn_instance=self._espn_instance)
            if self.provider == 'ESPN BET':
                self.close = BetValue(bet_name='close',
                                      bet_json=self.odds_json.get('close'),
                                      espn_instance=self._espn_instance)

    def to_dict(self) -> dict:
        """
        Converts the GameOdds instance to its original JSON dictionary.

        Returns:
            dict: The game odds's raw JSON data.
        """
        return self.odds_json


class OddsType:
    """
    Represents a specific type of betting odds (e.g., open, current, close).

    This class parses and stores detailed betting values such as point spread,
    spread, and money line. It uses the `BetValue` class to wrap individual bet types.

    Attributes:
        name (str): The name/type of the odds entry (e.g., "open", "current", "close").
        odds_type_json (dict): Raw JSON containing the odds data.
        espn_instance (PYESPN): The ESPN API instance used for constructing related data.
        favorite (str or None): The identifier for the favored team in this odds set.
        odds (dict): Dictionary mapping odds types to `BetValue` instances.
                     Keys include 'point_spread', 'spread', and 'money_line'.
    """

    def __init__(self, odds_name, odds_type_json, espn_instance):
        """
        Initializes an OddsType instance with the provided name and JSON data.

        Args:
            odds_name (str): A label for this odds set (e.g., "open", "current").
            odds_type_json (dict): JSON data containing detailed betting values.
            espn_instance (PYESPN): The parent ESPN API instance.
        """
        self.name = odds_name
        self.odds_type_json = odds_type_json
        self._espn_instance = espn_instance
        self.odds = {}
        self.favorite = self.odds_type_json.get('favorite')
        self._load_odds_type_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the OddsType instance.

        Returns:
            str: A formatted string indicating the name of the odds type.
        """
        return f"<OddsType | {self.name}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _load_odds_type_data(self):
        """
        Parses the odds_type_json to populate the `odds` dictionary with BetValue instances.

        Extracts:
            - Point spread odds
            - Spread odds
            - Money line odds
        Each is stored as a `BetValue` under a corresponding key.
        """
        self.odds['point_spread'] = BetValue(bet_name='point_spread',
                                             bet_json=self.odds_type_json.get('pointSpread', {}),
                                             espn_instance=self._espn_instance)
        self.odds['spread'] = BetValue(bet_name='spread',
                                       bet_json=self.odds_type_json.get('spread', {}),
                                       espn_instance=self._espn_instance)
        self.odds['money_line'] = BetValue(bet_name='money_line',
                                           bet_json=self.odds_type_json.get('moneyLine', {}),
                                           espn_instance=self._espn_instance)

    def to_dict(self) -> dict:
        """
        Converts the OddsType instance to its original JSON dictionary.

        Returns:
            dict: The odds type's raw JSON data.
        """
        return self.odds_type_json


class Odds:
    """
    Represents betting odds for a specific team within a sporting event.

    This class parses and stores betting-related data such as money lines,
    spreads, and associated odds types (open, current, and optionally close).

    Attributes:
        odds_json (dict): Raw JSON data for the odds entry.
        espn_instance (PYESPN): The main ESPN API instance used for lookups.
        event_instance (Event): The event this odds entry is associated with.
        gameodds_instance (GameOdds): The higher-level odds grouping instance.
        favorite (str): The name of the favorite team, if available.
        underdog (str): The name of the underdog team, if available.
        money_line (int or None): The money line value for this odds.
        spread_odds (int or None): The spread odds value.
        team (Team): The team associated with these odds.
        open (OddsType): The opening odds.
        current (OddsType): The most recent odds.
        close (OddsType or None): The closing odds, if provided (e.g., for ESPN BET).
    """

    def __init__(self, odds_json, espn_instance, event_instance, gameodds_instance):
        """
        Initializes an Odds instance from provided JSON data.

        Args:
            odds_json (dict): The raw JSON containing odds data for a team.
            espn_instance (PYESPN): The parent API instance.
            event_instance (Event): The sporting event this odds data belongs to.
            gameodds_instance (GameOdds): The containing game odds context.
        """
        self.odds_json = odds_json
        self._espn_instance = espn_instance
        self.event_instance = event_instance
        self.gameodds_instance = gameodds_instance
        self._load_odds_json()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Odds instance.

        Returns:
            str: A string identifying the associated team.
        """
        return f"<Odds | {self.team.name}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _load_odds_json(self):
        """
        Parses the JSON data and assigns odds-related attributes.

        Extracts key betting values such as favorite, underdog, money line,
        and odds type objects (open/current/close). Also resolves and assigns
        the associated team using the ESPN API.
        """

        self.favorite = self.odds_json.get('favorite')
        self.underdog = self.odds_json.get('underdog')
        self.money_line = self.odds_json.get('moneyLine')
        self.spread_odds = self.odds_json.get('spreadOdds')
        team_id = get_team_id(self.odds_json.get('team', {}).get('$ref'))
        self.team = self._espn_instance.get_team_by_id(team_id=team_id)
        self.open = OddsType(odds_name='open',
                             odds_type_json=self.odds_json.get('open'),
                             espn_instance=self._espn_instance)
        self.current = OddsType(odds_name='current',
                                odds_type_json=self.odds_json.get('current'),
                                espn_instance=self._espn_instance)
        if self.gameodds_instance.provider == 'ESPN BET':
            self.close = OddsType(odds_name='close',
                                  odds_type_json=self.odds_json.get('close'),
                                  espn_instance=self._espn_instance)

    def to_dict(self) -> dict:
        """
        Converts the Odds instance to its original JSON dictionary.

        Returns:
            dict: The odds's raw JSON data.
        """
        return self.odds_json


class OddsBet365(Odds):
    """
    Represents a specialized Odds entry sourced from Bet365 data.

    Inherits from the base `Odds` class but overrides the odds loading logic
    to handle Bet365-specific formatting for money line, spread, and teaser odds.

    Attributes:
        odds_json (dict): Raw JSON data for the odds entry.
        espn_instance (PYESPN): The ESPN API instance used for lookups.
        event_instance (Event): The event this odds entry is associated with.
        gameodds_instance (GameOdds): The parent odds grouping instance.
        team (Team): The team this odds instance is associated with.
        money_line (float or None): Bet365 money line value.
        spread_odds (float or None): Bet365 spread value.
        teaser_odds (float or None): Bet365 spread handicap value.
    """

    def __init__(self, odds_json, espn_instance, event_instance, gameodds_instance, team):
        """
        Initializes an OddsBet365 instance with Bet365-specific odds data.

        Args:
            odds_json (dict): JSON data containing Bet365 odds.
            espn_instance (PYESPN): Parent API instance.
            event_instance (Event): The event associated with these odds.
            gameodds_instance (GameOdds): The odds group this entry belongs to.
            team (Team): The team associated with this Bet365 odds entry.
        """
        super().__init__(odds_json=odds_json,
                         espn_instance=espn_instance,
                         event_instance=event_instance,
                         gameodds_instance=gameodds_instance)
        self.team = team

    def __repr__(self) -> str:
        """
        Returns a string representation of the OddsBet365 instance.

        Returns:
            str: A string identifying the team and provider.
        """
        return f"<Odds365 | {self.team.name}>"

    def _load_odds_json(self):
        """
        Parses the Bet365 odds JSON and sets betting attributes.

        Extracts values for money line, spread, and teaser (spread handicap)
        odds by identifying the appropriate keys using keyword matching.
        """
        try:
            for key, value in self.odds_json.items():
                if 'moneyline' in str(key).lower():
                    self.money_line = value.get('value')
                if 'spread' in str(key).lower() and 'spreadhandicap' not in str(key).lower():
                    self.spread_odds = value.get('value')
                if 'spreadhandicap' in str(key).lower():
                    self.teaser_odds = value.get('value')
        except AttributeError:
            pass


class BetValue:
    """
    Represents a specific betting value or option within a betting category.

    This class dynamically loads all key-value pairs from the given JSON, converting
    the keys to snake_case and setting them as attributes.

    Attributes:
        name (str): The name of the bet or betting category.
        bet_json (dict): The raw JSON data representing the individual bet value.
        espn_instance (PYESPN): The parent ESPN API wrapper instance.
        (dynamic attributes): All key-value pairs from `bet_json`, converted to snake_case.
    """

    def __init__(self, bet_name, bet_json, espn_instance):
        """
        Initializes a BetValue instance with the given name and JSON data.

        Args:
            bet_name (str): The name or label for the betting option.
            bet_json (dict): The raw JSON data for the bet value.
            espn_instance (PYESPN): The main ESPN API instance.
        """
        self.name = bet_name
        self.bet_json = bet_json
        self._espn_instance = espn_instance
        self._load_bet_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the BetValue instance.

        Returns:
            str: A formatted string identifying the betting value.
        """
        return f"<BetValue | {self.name}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _load_bet_data(self):
        """
        Parses the raw bet JSON and sets each item as an instance attribute.

        Converts each key in the JSON to snake_case before assigning it. This allows
        flexible access to all JSON properties as attributes.

        Note:
            If there's an error in setting attributes (e.g., due to invalid characters),
            the process silently fails for that key.
        """

        try:
            for key, value in self.bet_json.items():
                snake_key = camel_to_snake(key)
                setattr(self, snake_key, value)
        except AttributeError:
            pass

    def to_dict(self) -> dict:
        """
        Converts the BetValue instance to its original JSON dictionary.

        Returns:
            dict: The betvalues's raw JSON data.
        """
        return self.bet_json
