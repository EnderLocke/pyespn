from pyespn.utilities import fetch_espn_data, get_an_id
from pyespn.classes.player import Player
from pyespn.classes.team import Manufacturer
from pyespn.classes.stat import Record


class Standings:
    """
    Represents the standings for a racing league, including athletes, manufacturers, and records.

    This class initializes and processes standings data from a given JSON structure, fetching
    additional details for athletes and manufacturers as needed.

    Attributes:
        standings_json (dict): Stores the raw standings JSON data.
        espn_instance (object): Reference to the ESPN API instance.
        standings (list): A list of dictionaries containing athlete, manufacturer, and record data.
        standings_type_name (str): The display name for the standings category.
    """

    def __init__(self, standings_json, espn_instance):
        """
        Initializes the Standings instance and loads standings data.

        Args:
            standings_json (dict): The JSON data containing standings information.
            espn_instance (object): An instance of the ESPN API handler.
        """

        self.standings_json = standings_json
        self.espn_instance = espn_instance
        self.standings = []
        self._load_standings_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Standings instance.

        The representation includes the standings type and the number of entries in the standings list.

        Returns:
            str: A formatted string representing the standings.
        """
        return f"<Standings | {self.standings_type_name}, Entries: {len(self.standings)}>"

    def _load_standings_data(self):
        """
        Parses the standings JSON and populates the standings attribute.

        This method extracts relevant standings information, including details about athletes,
        manufacturers, and their performance records. It fetches additional data from ESPN APIs
        as needed to populate Player and Manufacturer objects.

        Populates:
            standings (list): A list of dictionaries, each containing:
                - 'athlete' (Player or None): The athlete associated with the standing.
                - 'manufacturer' (Manufacturer or None): The manufacturer associated with the standing.
                - 'record' (list of Record objects): Performance records for the athlete or manufacturer.
        """

        this_athlete = None
        this_manufacturer = None
        self.standings_type_name = self.standings_json.get('displayName')
        for competitor in self.standings_json.get('standings', []):
            if 'athlete' in competitor:
                athlete_content = fetch_espn_data(competitor.get('athlete', {}).get('$ref'))
                this_athlete = Player(player_json=athlete_content,
                                      espn_instance=self.espn_instance)
            elif 'manufacturer' in competitor:
                manufacturer_content = fetch_espn_data(competitor.get('manufacturer', {}).get('$ref'))
                this_manufacturer = Manufacturer(manufacturer_json=manufacturer_content,
                                                 espn_instance=self.espn_instance)
            records = []
            for record in competitor.get('records', []):
                records.append(Record(record_json=record,
                                      espn_instance=self.espn_instance))
            full_athlete = {
                'athlete': this_athlete,
                'manufacturer': this_manufacturer,
                'record': records
            }

            self.standings.append(full_athlete)
