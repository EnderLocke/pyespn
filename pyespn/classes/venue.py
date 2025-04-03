from pyespn.core.decorators import validate_json
from pyespn.classes.player import Player


@validate_json("venue_json")
class Venue:
    """
    Represents a venue with associated details, such as name, address, and type of surface.

    Attributes:
        venue_json (dict): The raw JSON data representing the venue.
        venue_id (str): The unique ID of the venue.
        name (str): The full name of the venue.
        address_json (dict): The address details of the venue.
        grass (bool): Flag indicating if the venue has a grass surface.
        indoor (bool): Flag indicating if the venue is indoors.
        images (list): A list of image URLs related to the venue.

    Methods:
        __repr__(): Returns a string representation of the Venue instance.
        to_dict(): Converts the venue data to a dictionary format.
    """

    def __init__(self, venue_json):
        """
        Initializes a Venue instance using the provided venue JSON data.

        Args:
            venue_json (dict): The raw JSON data representing the venue.
        """

        self.venue_json = venue_json
        self.venue_id = self.venue_json.get('id')
        self.name = self.venue_json.get('fullName')
        self.address_json = self.venue_json.get('address')
        self.grass = self.venue_json.get('grass')
        self.indoor = self.venue_json.get('indoor')
        self.images = self.venue_json.get('images', [])

    def __repr__(self):
        """
        Returns a string representation of the Venue instance.

        Returns:
            str: A formatted string with the venues name.
        """
        return f"<Venue | {self.name}>"

    def to_dict(self) -> dict:
        """
        Converts the venue data to a dictionary format.

        Returns:
            dict: The raw JSON data representing the venue.
        """
        return self.venue_json


class Circuit:


    def __init__(self, circuit_json, espn_isntance):
        self.circuit_json = circuit_json
        self.espn_instance = espn_isntance
        self._load_circut_data()

    def _load_circut_data(self):
        """
        Sets each attribute from the circuit_json to its own attribute.
        """
        self.api_ref = self.circuit_json.get('$ref')
        self.id = self.circuit_json.get('id')
        self.full_name = self.circuit_json.get('fullName')

        # Extracting nested 'address' data
        address = self.circuit_json.get('address', {})
        self.city = address.get('city')
        self.country = address.get('country')

        self.type = self.circuit_json.get('type')
        self.length = self.circuit_json.get('length')
        self.distance = self.circuit_json.get('distance')
        self.laps = self.circuit_json.get('laps')
        self.turns = self.circuit_json.get('turns')
        self.direction = self.circuit_json.get('direction')
        self.established = self.circuit_json.get('established')

        # Fastest lap driver and fastest lap time
        self.fastest_lap_driver_ref = Player(player_json=self.circuit_json.get('fastestLapDriver', {}).get('$ref'),
                                             espn_instance=self.espn_instance)
        self.fastest_lap_time = self.circuit_json.get('fastestLapTime')
        self.fastest_lap_year = self.circuit_json.get('fastestLapYear')

        # Track reference
        self.track_ref = self.circuit_json.get('track', {}).get('$ref')

        # Extracting diagrams list and storing it
        self.diagrams = self.circuit_json.get('diagrams', [])
        # You can store each diagram in a separate variable if needed, for example:
        self.diagram_urls = [diagram.get('href') for diagram in self.diagrams]

    def __repr__(self):
        """
        Returns a string representation of the Circuit instance.
        """
        return f"<Circuit | {self.full_name}, {self.city}, {self.country}>"
