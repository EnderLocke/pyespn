

class Stat:
    """
    Represents a statistical record for a player within a given season.

    Attributes:
        stat_json (dict): The raw JSON data containing the statistical information.
        espn_instance: The ESPN API instance used for retrieving additional data.
    """

    def __init__(self, stat_json, espn_isntance):
        """
        Initializes a Stat instance.

        Args:
            stat_json (dict): The JSON object containing the stat data.
            espn_instance: An instance of the ESPN API client.
        """
        self.stat_json = stat_json
        self.espn_instance = espn_isntance

    def __repr__(self):
        """
        Returns a string representation of the Stat instance.

        Returns:
            str: A formatted string with the stat name, value, and season.
        """
        return f"<Stat | {self.season}-{self.name}: {self.stat_value}>"

    def _set_stats_data(self):
        """
        Extracts and sets the statistical attributes from the provided JSON data.
        """
        self.category = self.stat_json.get('category')
        self.season = self.stat_json.get('season')
        self.player_id = self.stat_json.get('player_id')
        self.stat_value = self.stat_json.get('stat_value')
        self.stat_type_abbreviation = self.stat_json.get('stat_type_abbreviation')
        self.description = self.stat_json.get('description')
        self.name = self.stat_json.get('name')
