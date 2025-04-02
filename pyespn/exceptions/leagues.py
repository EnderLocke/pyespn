
class LeagueNotSupportedError(Exception):
    """Exception raised when a league is not supported for a certain operation/client creation."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)


class LeagueNotAvailableError(Exception):
    """Exception raised whenThe league you have used is within the espn api but has not been developed within pyespn at this point."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)


class InvalidLeagueError(Exception):
    """Exception raised when The league you have used is not a valid league abbreviation within pyespn."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)