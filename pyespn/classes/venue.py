from pyespn.core.decorators import validate_json


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
        Returns a string representation of the Team instance.

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
