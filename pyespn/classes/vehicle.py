

class Vehicle:
    """
    Represents a racing vehicle with details such as number, manufacturer,
    chassis, engine, tire, and associated team.

    Attributes:
        vehicle_json (dict): JSON data containing vehicle details.
        espn_instance: An instance of the ESPN API client.
        number (str or None): The vehicle's number.
        manufacturer (str or None): The vehicle's manufacturer.
        chassis (str or None): The vehicle's chassis type.
        engine (str or None): The engine used in the vehicle.
        tire (str or None): The tire manufacturer.
        team (str or None): The team associated with the vehicle.

    Methods:
        _set_vehicle_data(): Extracts and sets vehicle details from the JSON data.
    """

    def __init__(self, vehicle_json, espn_instance):
        """
        Initializes a Vehicle instance.

        Args:
            vehicle_json (dict): JSON data containing vehicle details.
            espn_instance (PYESPN): An instance of the ESPN API client.
        """
        self.vehicle_json = vehicle_json
        self.espn_instance = espn_instance
        self._set_vehicle_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Vehicle instance.

        Returns:
            str: A formatted string with the Vehicles name.
        """
        return f"<Vehicle | {self.team}, {self.manufacturer} ({self.number})>"

    def _set_vehicle_data(self):
        """
        Extracts and assigns vehicle details from the provided JSON data.
        """
        self.number = self.vehicle_json.get('number')
        self.manufacturer = self.vehicle_json.get('manufacturer')
        self.chassis = self.vehicle_json.get('chassis')
        self.engine = self.vehicle_json.get('engine')
        self.tire = self.vehicle_json.get('tire')
        self.team = self.vehicle_json.get('team')
