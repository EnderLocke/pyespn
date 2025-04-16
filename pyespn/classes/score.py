from pyespn.utilities import fetch_espn_data


class LineScore:

    def __init__(self, linescore_json, espn_instance, event_instance):
        self.linescore_json = linescore_json
        self._espn_instance = espn_instance
        self._event_instance = event_instance
        self._load_linescore_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the LineScore instance.

        Returns:
            str: A formatted string with the linescore data.
        """
        return f"<LineScore ({self.period}) | {self.display_value}>"

    def _load_linescore_data(self):
        with self.linescore_json as lj:
            self.value = lj.get('value')
            self.display_value = lj.get('displayValue')
            self.period = lj.get('period')
            self.source = lj.get('source')
            self.ref = lj.get('$ref')

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


class Score:

    def __init__(self, espn_instance, event_instance, team_id):
        self._espn_instance = espn_instance
        self._event_instance = event_instance
        self.api_info = self._espn_instance.api_mapping
        self._team_id = team_id
        self._linescores = []
        self._load_score_data()
        self._load_line_scores()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Score instance.

        Returns:
            str: A formatted string with the Score data.
        """
        return f"<Score | {self.display_value} - {self.winner}>"

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

    def _load_score_data(self):
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_instance.event_id}/competitions/{self._event_instance.event_id}/competitors/{self._team_id}/score'
        self.score_json = fetch_espn_data(url)
        self.value = self.score_json.get('value')
        self.display_value = self.score_json.get("displayValue")
        self.winner = self.score_json.get('winner')
        self.source = self.score_json.get('source')

    def _load_line_scores(self):
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_instance.event_id}/competitions/{self._event_instance.event_id}/competitors/{self._team_id}/linescores'
        content = fetch_espn_data(url)
        self.linescore_list = content.get('items')
        for line in self.linescore_list:
            self._linescores.append(LineScore(linescore_json=line,
                                              espn_instance=self._espn_instance,
                                              event_instance=self._event_instance))
