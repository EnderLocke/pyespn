from pyespn.core.decorators import validate_json
import requests


@validate_json("image_json")
class Image:
    """
    Represents an image object from the ESPN API, typically associated with players, teams, or events.

    Attributes:
        image_json (dict): The raw JSON data representing the image.
        espn_instance (object): The ESPN API instance used for context or further data retrieval.
        ref (str): The direct URL to the image.
        name (str): A human-readable name derived from the image's `rel` field.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        alt (str): Alternative text for the image.
        rel (list): A list of roles describing the image (e.g., "default", "profile").
        last_updated (str): The last updated timestamp of the image.

    Methods:
        __init__(image_json, espn_instance):
            Initializes the Image object using JSON data and a reference to the ESPN API wrapper.

        __repr__():
            Returns a string representation of the Image object.

        _load_image_data():
            Parses and loads image metadata from the provided JSON data.

        load_image() -> bytes:
            Downloads and returns the binary content of the image from the reference URL.
    """

    def __init__(self, image_json, espn_instance):
        """
        Initializes an Image instance using the provided image JSON data.

        Args:
            image_json (dict): A dictionary containing image metadata from the ESPN API.
            espn_instance (object): A reference to the PyESPN instance.
        """

        self.image_json = image_json
        self._espn_instance = espn_instance
        self._load_image_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Image instance.

        Returns:
            str: A string showing the image's name.
        """
        return f"<Image | {self._name}>"

    def _load_image_data(self):
        """
        Parses the image JSON and sets image attributes such as URL, dimensions, and metadata.
        """
        self._ref = self.image_json.get('href')
        self._name = ' '.join(self.image_json.get('rel', []))
        self.width = self.image_json.get('width')
        self.height = self.image_json.get('height')
        self.alt = self.image_json.get('alt')
        if self._name == '':
            self._name = self.alt
        self.rel = self.image_json.get('rel')
        self.last_updated = self.image_json.get('lastUpdated')

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    @property
    def ref(self):
        """
            str: url for the image
        """
        return self._ref

    @property
    def name(self):
        """
            str: name of the image
        """
        return self._name

    def load_image(self) -> bytes:
        """
        Downloads and returns the image content from the object's reference URL.

        Returns:
            bytes: The binary content of the image.
        """
        image_request = requests.get(self._ref)
        image = image_request.content
        return image

    def to_dict(self) -> dict:
        """
        Converts the Image instance to its original JSON dictionary.

        Returns:
            dict: The images's raw JSON data.
        """
        return self.image_json
