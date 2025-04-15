from pyespn.classes.position import Position


class DepthChart:
    """
    Represents a team's depth chart.

    This class parses and stores positional data from a depth chart JSON,
    using the ESPN API and team instance to initialize each position.

    Attributes:
        depth_chart_json (dict): Raw JSON data containing the depth chart.
        espn_instance (PYESPN): The ESPN API instance used for lookups.
        team_instance (Team): The team instance this depth chart belongs to.
        positions (dict): A mapping of position keys to `Position` instances.
        name (str): The name of the depth chart (usually the team name).
        id (int or None): The ID of the depth chart.
    """

    def __init__(self, depth_chart_json, espn_instance, team_instance):
        """
        Initializes a DepthChart instance.

        Args:
            depth_chart_json (dict): JSON data representing the depth chart.
            espn_instance (PYESPN): The ESPN API wrapper instance.
            team_instance (Team): The team associated with the depth chart.
        """
        self.depth_chart_json = depth_chart_json
        self._espn_instance = espn_instance
        self._team_instance = team_instance
        self.positions = {}
        self._load_depth_chart_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the DepthChart instance.

        Returns:
            str: A formatted string with the depthcharts's attributes.
        """
        return f"<DepthChart | {self.name}>"

    def _load_depth_chart_data(self):
        """
        Parses the raw depth chart JSON and initializes `Position` instances
        for each position listed.

        Sets the `name` and `id` attributes from the JSON, and populates the
        `positions` dictionary using the data under the 'positions' key.
        """
        self.name = self.depth_chart_json.get('name')
        self.id = self.depth_chart_json.get('id')
        for key, value in self.depth_chart_json.get('positions', {}).items():
            self.positions[key] = Position(position_json=value,
                                           espn_instance=self._espn_instance,
                                           team_instance=self._team_instance)

    @property
    def team_instance(self):
        """
            Team: the team instance associated with the depth chart
        """
        return self._team_instance

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def to_dict(self) -> dict:
        """
        Converts the DepthChart instance to its original JSON dictionary.

        Returns:
            dict: The depth charts's raw JSON data.
        """
        return self.depth_chart_json
