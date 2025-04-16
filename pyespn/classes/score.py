from pyespn.utilities import fetch_espn_data


class LineScore:
    """
    Represents a period-specific score entry for a team in a sports event.

    Attributes:
        linescore_json (dict): Raw JSON data representing a single period's score.
        _espn_instance (PYESPN): The ESPN API wrapper instance.
        _event_instance (Event): The Event associated with the linescore.
        value (int | None): Raw numerical score for the period.
        display_value (str | None): Human-readable score for the period (e.g., "7").
        period (int | None): The period number this score represents (e.g., 1st quarter, 2nd inning).
        source (str | None): The source of the score (e.g., "official").
        ref (str | None): A reference URL for the linescore entry.

    Methods:
        _load_linescore_data() -> None:
            Parses and assigns values from the JSON into class attributes.
    """

    def __init__(self, linescore_json, espn_instance, event_instance):
        """
        Initializes the LineScore instance for a specific period of a team in an event.

        Args:
            linescore_json (dict): The raw JSON representing this period's score.
            espn_instance (PYESPN): The ESPN API wrapper instance.
            event_instance (Event): The Event associated with this linescore.
        """
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
        """
        Loads and sets the attributes from the provided linescore JSON.
        """
        self.value = self.linescore_json.get('value')
        self.display_value = self.linescore_json.get('displayValue')
        self.period = self.linescore_json.get('period')
        self.source = self.linescore_json.get('source')
        self.ref = self.linescore_json.get('$ref')

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
    """
    Represents the score data for a specific team in a sports event, including total score and per-period breakdowns.

    Attributes:
        _espn_instance (PYESPN): The ESPN API wrapper instance.
        _event_instance (Event): The Event instance associated with the score.
        api_info (dict): Mapped API configuration for the league and sport.
        _team_id (int): The team ID for which this score object is created.
        _linescores (list[LineScore]): A list of LineScore objects representing period-by-period scores.
        value (int | None): Raw numerical score value.
        display_value (str | None): Human-readable score (e.g., "24").
        winner (bool | None): Whether this team won the event.
        source (str | None): Origin of the score data (e.g., "official").
        linescore_list (list): Raw list of linescore JSON entries returned from the API.

    Methods:
        _load_score_data() -> None:
            Fetches and sets the overall score information from the ESPN API for the team.

        _load_line_scores() -> None:
            Fetches and builds the list of LineScore objects for each period in the event.
    """

    def __init__(self, espn_instance, event_instance, team_id):
        """
        Initializes the Score object for a specific team in an event.

        Args:
            espn_instance (PYESPN): The ESPN API wrapper instance.
            event_instance (Event): The Event this score is tied to.
            team_id (int): The team ID for the team whose score is being loaded.
        """
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
    def periods(self):
        """
        list[LineScore]: a list of linescore objects with period score data
        """
        return self._linescores

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
        """
        Fetches and loads the main score data for the team in this event.

        This includes the final score value, display version, winner status, and source.
        """
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_instance.event_id}/competitions/{self._event_instance.event_id}/competitors/{self._team_id}/score'
        self.score_json = fetch_espn_data(url)
        self.value = self.score_json.get('value')
        self.display_value = self.score_json.get("displayValue")
        self.winner = self.score_json.get('winner')
        self.source = self.score_json.get('source')

    def _load_line_scores(self):
        """
        Fetches and constructs LineScore objects for each period of the event.

        The method populates the `self._linescores` list with structured LineScore instances
        based on the data returned from the ESPN API.
        """
        url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info["sport"]}/leagues/{self.api_info["league"]}/events/{self._event_instance.event_id}/competitions/{self._event_instance.event_id}/competitors/{self._team_id}/linescores'
        content = fetch_espn_data(url)
        self.linescore_list = content.get('items')
        for line in self.linescore_list:
            self._linescores.append(LineScore(linescore_json=line,
                                              espn_instance=self._espn_instance,
                                              event_instance=self._event_instance))
