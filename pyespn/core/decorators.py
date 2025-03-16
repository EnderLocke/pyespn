from pyespn.data.betting import BETTING_AVAILABLE
from pyespn.data.leagues import PRO_LEAGUES, COLLEGE_LEAGUES
from pyespn.data.standings import STANDINGS_TYPE_MAP
from pyespn.exceptions import (LeagueNotSupportedError, LeagueNotAvailableError,
                               InvalidLeagueError)
from functools import wraps
import warnings


def requires_standings_available(func):
    """Decorator to check if betting is available before executing a method."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.league_abbv not in STANDINGS_TYPE_MAP:
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
