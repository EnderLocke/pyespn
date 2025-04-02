

class ScheduleTypeUnknownError(Exception):
    """Exception raised when a there is not a schedule type avaiable witin pyespn"""
    def __init__(self, league_abbv, message="Unknown schedule type for: "):
        self.league_abbv = league_abbv
        self.message = f"{message}{self.league_abbv})"
        super().__init__(self.message)
