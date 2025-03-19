
class Team:
    """
    Represents a sports team within the ESPN API framework.

    This class is designed to store team-related information while maintaining a reference 
    to a `PYESPN` instance, allowing access to league-specific details.

    Attributes:
        espn_instance (PYESPN): Reference to the parent `PYESPN` instance.
        team_id (int): Unique identifier for the team.
        name (str): Full name of the team.
        abbreviation (str): Team abbreviation (e.g., "LAL" for Los Angeles Lakers).
        location (str): Geographic location of the team (e.g., "Los Angeles").
    """

    def __init__(self, espn_instance, team_id, name, abbreviation, location):
        """
        Initializes a Team instance.

        Args:
            espn_instance (PYESPN): The parent `PYESPN` instance, providing access to league details.
            team_id (int): The unique identifier for the team.
            name (str): The name of the team.
            abbreviation (str): The team's abbreviation.
            location (str): The team's location (e.g., city or state).
        """
        self.espn_instance = espn_instance
        self.team_id = team_id
        self.name = name
        self.abbreviation = abbreviation
        self.location = location

    def get_league(self):
        """
        Retrieves the league abbreviation from the associated `PYESPN` instance.

        Returns:
            str: The league abbreviation (e.g., "nfl", "nba", "cfb").
        """
        return self.espn_instance.league_abbv

    def __repr__(self):
        """
        Returns a string representation of the Team instance.

        Returns:
            str: A formatted string with the team's location, name, abbreviation, and league.
        """
        return f"<Team {self.location} {self.name} ({self.abbreviation}) - {self.get_league()}>"