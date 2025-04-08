

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
    """

    def __init__(self, image_json, espn_instance):
        """
        Initializes an Image instance using the provided image JSON data.

        Args:
            image_json (dict): A dictionary containing image metadata from the ESPN API.
            espn_instance (object): A reference to the PyESPN instance.
        """

        self.image_json = image_json
        self.espn_instance = espn_instance
        self._load_image_data()

    def __repr__(self):
        """
        Returns a string representation of the Manufacturer instance.
        """
        return f"<Image | {self.name}>"

    def _load_image_data(self):
        """
        Parses the image JSON and sets image attributes such as URL, dimensions, and metadata.
        """
        self.ref = self.image_json.get('href')
        self.name = ' '.join(self.image_json.get('rel', []))
        self.width = self.image_json.get('width')
        self.height = self.image_json.get('height')
        self.alt = self.image_json.get('alt')
        self.rel = self.image_json.get('rel')
        self.last_updated = self.image_json.get('lastUpdated')
