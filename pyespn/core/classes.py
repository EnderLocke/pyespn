
class Team:
    """Standalone Team class with reference to PYESPN."""
    def __init__(self, espn_instance, team_id, name, abbreviation, location):
        self.espn_instance = espn_instance
        self.team_id = team_id
        self.name = name
        self.abbreviation = abbreviation
        self.location = location

    def get_league(self):
        """Access league_abbv from the parent PYESPN instance."""
        return self.espn_instance.league_abbv

    def __repr__(self):
        return f"<Team {self.location} {self.name} ({self.abbreviation}) - {self.get_league()}>"
