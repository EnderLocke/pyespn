

class Broadcast:

    def __init__(self, broadcast_json, espn_instance, event_instance):
        self.broadcast_json = broadcast_json
        self._espn_instance = espn_instance
        self._event_instance = event_instance
        self._load_broadcast_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Broadcast instance.

        Returns:
            str: A formatted string with the broadcast information .
        """
        return f"<Official | {self.broadcast_type_name} | {self.station}>"


    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    @property
    def event_instance(self):
        """
            Event: the Event instance associated with the class
        """
        return self._event_instance

    def _load_broadcast_data(self):
        self.broadcast_type_name = self.broadcast_json.get('type', {}).get('longName')
        self.broadcast_type_short_name = self.broadcast_json.get('type', {}).get('shortName')
        self.broadcast_type_id = self.broadcast_json.get('type', {}).get('id')
        self.channel = self.broadcast_json.get('channel')
        self.station = self.broadcast_json.get('station')
        self.media = self.broadcast_json.get('media')
        self.channel = self.broadcast_json.get('channel')
