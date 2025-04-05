

class Image:

    def __init__(self, image_json, espn_instance):
        self.image_json = image_json
        self.espn_instance = espn_instance
        self._load_image_data()

    def __repr__(self):
        """
        Returns a string representation of the Manufacturer instance.
        """
        return f"<Image | {self.name}>"

    def _load_image_data(self):
        self.ref = self.image_json.get('href')
        self.name = ' '.join(self.image_json.get('rel', []))
        self.width = self.image_json.get('width')
        self.height = self.image_json.get('height')
        self.alt = self.image_json.get('alt')
        self.rel = self.image_json.get('rel')
        self.last_updated = self.image_json.get('lastUpdated')
