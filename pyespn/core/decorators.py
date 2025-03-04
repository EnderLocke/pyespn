from functools import wraps
from pyespn.data.betting import BETTING_AVAILABLE
from pyespn.data.leagues import PRO_LEAGUES, COLLEGE_LEAGUES
from pyespn.exceptions import LeagueNotSupportedError


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
    """Decorator to ensure a method is not used for professional leagues."""
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
