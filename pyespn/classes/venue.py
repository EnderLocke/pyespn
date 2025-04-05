from pyespn.core.decorators import validate_json
from pyespn.classes.player import Player
from pyespn.classes.image import Image


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

    def __init__(self, venue_json, espn_instance):
        """
        Initializes a Venue instance using the provided venue JSON data.

        Args:
            venue_json (dict): The raw JSON data representing the venue.
            espn_instance (object): The ESPN instance used for making API calls.
        """

        self.venue_json = venue_json
        self.espn_instance = espn_instance
        self.venue_id = self.venue_json.get('id')
        self.name = self.venue_json.get('fullName')
        self.address_json = self.venue_json.get('address')
        self.grass = self.venue_json.get('grass')
        self.indoor = self.venue_json.get('indoor')
        self.images = [Image(image_json=image, espn_instance=self.espn_instance) for image in self.venue_json.get('images', [])]

    def __repr__(self) -> str:
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
    """
    A class to represent a Circuit.

    This class takes a JSON response from an API and processes the data to create
    a Circuit object with relevant attributes. It provides details such as the
    circuit's name, address, type, laps, and fastest lap times, as well as any
    related diagrams and references to other objects like the fastest lap driver
    and track.

    Attributes:
        api_ref (str): The API reference URL for the circuit.
        id (str): The unique identifier of the circuit.
        full_name (str): The full name of the circuit.
        city (str): The city where the circuit is located.
        country (str): The country where the circuit is located.
        type (str): The type of the circuit (e.g., street, permanent).
        length (str): The length of the circuit.
        distance (str): The total distance of the race at the circuit.
        laps (int): The number of laps in the race at the circuit.
        turns (int): The number of turns in the circuit.
        direction (str): The racing direction (e.g., clockwise, counterclockwise).
        established (int): The year when the circuit was established.
        fastest_lap_driver_ref (Player): A reference to the fastest lap driver.
        fastest_lap_time (str): The time of the fastest lap at the circuit.
        fastest_lap_year (int): The year in which the fastest lap was recorded.
        track_ref (str): A reference to the track.
        diagrams (list): A list of diagrams related to the circuit.
        diagram_urls (list): A list of URLs pointing to the circuit diagrams.
    """

    def __init__(self, circuit_json, espn_instance):
        """
        Initializes a Circuit instance with data from a JSON response and an ESPN instance.

        Args:
            circuit_json (dict): The JSON data containing information about the circuit.
            espn_instance (object): The ESPN instance used for making API calls.

        This method also calls _load_circuit_data to load the data into attributes.
        """
        self.circuit_json = circuit_json
        self.espn_instance = espn_instance
        self._load_circuit_data()

    def _load_circuit_data(self):
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
