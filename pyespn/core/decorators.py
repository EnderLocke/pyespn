from pyespn.data.betting import BETTING_AVAILABLE
from pyespn.data.leagues import PRO_LEAGUES, COLLEGE_LEAGUES
from pyespn.data.standings import STANDINGS_AVAILABLE
from pyespn.exceptions import (LeagueNotSupportedError, LeagueNotAvailableError,
                               InvalidLeagueError, JSONNotProvidedError)
from functools import wraps
import json
import warnings


def requires_standings_available(func):
    """Decorator to check if betting is available before executing a method."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.league_abbv not in STANDINGS_AVAILABLE:
            raise LeagueNotSupportedError(
                self.league_abbv,
                f"Standings is not available for {self.league_abbv}."
            )
        return func(self, *args, **kwargs)

    return wrapper


def requires_betting_available(func):
    """Decorator to check if betting is available before executing a method."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.league_abbv not in BETTING_AVAILABLE:
            raise LeagueNotSupportedError(
                self.league_abbv,
                f"Betting is not available for {self.league_abbv}."
            )
        return func(self, *args, **kwargs)

    return wrapper


def requires_college_league(check):
    """Decorator to ensure a method is not used for college leagues."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.league_abbv not in COLLEGE_LEAGUES:
                raise LeagueNotSupportedError(
                    self.league_abbv,
                    f"{check} is not available for {self.league_abbv}."
                )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


def requires_pro_league(check):
    """Decorator to ensure a method is not used for professional leagues."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.league_abbv not in PRO_LEAGUES:
                raise LeagueNotSupportedError(
                    self.league_abbv,
                    f"{check} is not available for {self.league_abbv}."
                )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


def validate_league(cls):
    """Class decorator to validate sport_league on instantiation."""
    original_init = cls.__init__

    def new_init(self, sport_league='nfl', *args, **kwargs):
        sport_league = sport_league.lower()
        if sport_league in self.untested_leagues:
            warnings.warn(f"This league | {sport_league} | is untested, uncaught errors may occur", UserWarning)
        if sport_league in self.all_leagues:
            raise LeagueNotAvailableError(f"Sport, {sport_league} is valid and within api but not currently available within PYESPN")
        if sport_league not in self.valid_leagues:
            raise InvalidLeagueError(f"Invalid sport league: '{sport_league}'. Must be one of {self.valid_leagues}")
        original_init(self, sport_league, *args, **kwargs)

    cls.__init__ = new_init
    return cls


def validate_json(json_attr):
    """Class decorator to validate JSON input on instantiation."""
    def decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, *args, **kwargs):
            json_obj = kwargs.get(json_attr)  # Get the specific JSON argument

            if not isinstance(json_obj, dict):
                if not json_obj:
                    raise JSONNotProvidedError(error_message=f'{json_attr} is None')
                try:
                    json_obj = json.loads(json_obj)
                    if not isinstance(json_obj, dict):
                        raise JSONNotProvidedError(error_message=f'{json_attr} is not a valid JSON object')
                except json.JSONDecodeError as e:
                    raise JSONNotProvidedError(error_message=f'Error decoding {json_attr}: {e.msg}')

            # Assign validated JSON back to kwargs (in case it's modified from a string)
            kwargs[json_attr] = json_obj

            original_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls
    return decorator

