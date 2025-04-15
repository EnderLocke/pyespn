from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyespn import PYESPN
    from pyespn.classes import Event


class Broadcast:
    """
    Represents a broadcast of a sporting event.

    This class encapsulates details about a particular broadcast, including the station,
    channel, media type, and broadcast classification.

    Attributes:
        broadcast_json (dict): The raw JSON data representing the broadcast.
        _espn_instance (PYESPN): The ESPN API wrapper instance.
        _event_instance (Event): The Event instance this broadcast is associated with.
        broadcast_type_name (str): The long name of the broadcast type (e.g. "Television").
        broadcast_type_short_name (str): The short name of the broadcast type.
        broadcast_type_id (str or int): Identifier for the broadcast type.
        channel (str): The channel airing the broadcast (e.g. "ESPN2").
        station (str): The broadcasting station (e.g. "ESPN").
        media (dict): Additional media details provided by the API.
    """

    def __init__(self, broadcast_json, espn_instance, event_instance):
        """
        Initializes a Broadcast instance with raw JSON data and references to
        the ESPN API client and associated event.

        Args:
            broadcast_json (dict): The raw JSON data representing the broadcast.
            espn_instance (PYESPN): The ESPN API wrapper instance.
            event_instance (Event): The Event instance this broadcast is associated with.
        """
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
    def espn_instance(self) -> "PYESPN":
        """
        Returns the ESPN API wrapper instance associated with this broadcast.

        Returns:
            PYESPN: The ESPN client instance.
        """
        return self._espn_instance

    @property
    def event_instance(self) -> "Event":
        """
        Returns the event associated with this broadcast.

        Returns:
            Event: The related Event instance.
        """
        return self._event_instance

    def _load_broadcast_data(self):
        """
        Parses and loads broadcast data from the raw JSON object.

        Extracts details such as type, station, channel, and media content
        from the broadcast JSON and assigns them to class attributes.

        This method is called internally during initialization.
        """
        self.broadcast_type_name = self.broadcast_json.get('type', {}).get('longName')
        self.broadcast_type_short_name = self.broadcast_json.get('type', {}).get('shortName')
        self.broadcast_type_id = self.broadcast_json.get('type', {}).get('id')
        self.channel = self.broadcast_json.get('channel')
        self.station = self.broadcast_json.get('station')
        self.media = self.broadcast_json.get('media')
        self.channel = self.broadcast_json.get('channel')
