

class Stat:
    """
    Represents a statistical record for a player within a given season.

    Attributes:
        stat_json (dict): The raw JSON data containing the statistical information.
        espn_instance: The ESPN API instance used for retrieving additional data.
    """

    def __init__(self, stat_json, espn_instance):
        """
        Initializes a Stat instance.

        Args:
            stat_json (dict): The JSON object containing the stat data.
            espn_instance (PYESPN): An instance of the ESPN API client.
        """
        self.stat_json = stat_json
        self.espn_instance = espn_instance
        self._set_stats_data()

    def __repr__(self) -> str:
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


class Record:
    """
    Represents a statistical record for a player, team, or manufacturer in ESPN's data.

    This class extracts and organizes record-related information from the provided JSON data,
    including general details and associated statistics.

    Attributes:
        espn_instance (object): An instance of the ESPN API client.
        record_json (dict): The raw JSON data containing record details.
        stats (list): A list of Stat objects representing individual statistical entries.
        id (str or None): The unique identifier for the record.
        ref (str or None): The API reference URL for the record.
        name (str or None): The full name of the record.
        abbreviation (str or None): The abbreviated form of the record name.
        display_name (str or None): The display name for the record.
        short_display_name (str or None): The short display name for the record.
        description (str or None): A brief description of the record.
        type (str or None): The type of record (e.g., season record, career record).

    Methods:
        _load_record_data(): Extracts and assigns values from record_json to class attributes.
    """

    def __init__(self, record_json, espn_instance):
        """
        Initializes a Record object.

        Args:
            record_json (dict): The JSON data representing the record.
            espn_instance (object): An instance of the ESPN API client.
        """
        self.espn_instance = espn_instance
        self.record_json = record_json
        self.stats = []
        self._load_record_data()

    def __repr__(self):
        """
        Returns a string representation of the Record instance.

        The representation includes the record's display name and abbreviation
        for easy identification.
        """
        return f"<Record | {self.display_name} ({self.abbreviation})>"

    def _load_record_data(self):
        """
        Parses and assigns values from record_json to class attributes.

        This method extracts record details such as names, abbreviations, descriptions, and stats.
        It also initializes Stat objects for each statistical entry found in the record.
        """
        self.id = self.record_json.get('id')
        self.ref = self.record_json.get('$ref')
        self.name = self.record_json.get('name')
        self.summary = self.record_json.get('summary')
        self.display_value = self.record_json.get('displayValue')
        self.value = self.record_json.get('value')
        self.abbreviation = self.record_json.get('abbreviation')
        self.display_name = self.record_json.get('displayName')
        self.short_display_name = self.record_json.get('shortDisplayName')
        self.description = self.record_json.get('description')
        self.type = self.record_json.get('type')
        self.name = self.record_json.get('name')
        for stat in self.record_json.get('stats'):
            self.stats.append(Stat(stat_json=stat,
                                   espn_instance=self.espn_instance))
