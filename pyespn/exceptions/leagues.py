
class LeagueNotSupportedError(Exception):
    """Exception raised when a league is not supported for a certain operation."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)


class LeagueNotAvailableError(Exception):
    """Exception raised when a league is not supported for a certain operation."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)


class InvalidLeagueError(Exception):
    """Exception raised when a league is not supported for a certain operation."""
    def __init__(self, league_abbv, message="This league does not support this operation."):
        self.league_abbv = league_abbv
        self.message = f"{message} (League: {league_abbv})"
        super().__init__(self.message)