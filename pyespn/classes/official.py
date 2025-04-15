

class Official:
    """
    Represents an official (referee, umpire, etc.) assigned to a specific sports event.

    Attributes:
        official_json (dict): Raw JSON data representing the official from the ESPN API.
        _event_instance (Event): Reference to the Event instance this official is part of.
        _espn_instance (PYESPN): The ESPN API wrapper instance.
        name (str): Full name of the official.
        first_name (str): First name of the official.
        last_name (str): Last name of the official.
        display_name (str): Display name of the official.
        position_name (str): Role of the official (e.g., Referee, Umpire).
        position_display_name (str): User-friendly version of the role.
        position_id (int or str): ID representing the position type.
        order (int): Order of appearance or importance in the official listing.
    """

    def __init__(self, event_instance, espn_instance, official_json):
        """
        Initializes an Official instance with data from the ESPN API.

        Args:
            event_instance (Event): The event to which this official is assigned.
            espn_instance (PYESPN): The ESPN API wrapper instance.
            official_json (dict): JSON data containing the official's information.

        Returns:
            None
        """
        self.official_json = official_json
        self._event_instance = event_instance
        self._espn_instance = espn_instance
        self._load_official_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Official instance.

        Returns:
            str: A formatted string with the official information .
        """
        return f"<Official | {self.display_name} | {self.position_name}>"

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

    def _load_official_data(self):
        """
        Parses and assigns official details from the raw JSON data.

        Extracts attributes such as name, position, and order from the
        `official_json` dictionary provided during initialization.

        Returns:
            None
        """
        self.name = self.official_json.get('fullName')
        self.first_name = self.official_json.get('firstName')
        self.last_name = self.official_json.get('lastName')
        self.display_name = self.official_json.get('displayName')
        self.position_name = self.official_json.get('position', {}).get('name')
        self.position_display_name = self.official_json.get('position', {}).get('displayName')
        self.position_id = self.official_json.get('position', {}).get('id')
        self.order = self.official_json.get('order')
