from pyespn.classes.position import Position


class DepthChart:

    def __init__(self, depth_chart_json, espn_instance, team_instance):
        self.depth_chart_json = depth_chart_json
        self.espn_instance = espn_instance
        self.team_instance = team_instance
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
        self.name = self.depth_chart_json.get('name')
        self.id = self.depth_chart_json.get('id')
        for key, value in self.depth_chart_json.get('positions', {}).items():
            self.positions[key] = Position(position_json=value,
                                           espn_instance=self.espn_instance,
                                           team_instance=self.team_instance)
