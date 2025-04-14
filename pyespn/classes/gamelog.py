from pyespn.utilities import get_team_id
from pyespn.core.decorators import validate_json


@validate_json("drive_json")
class Drive:
    """
    Represents a single drive within a sports event.

    A drive typically consists of a sequence of plays executed by the offensive team,
    and may result in a score, turnover, or punt. This class handles loading and
    structuring that information from the ESPN API response.

    Attributes:
        drive_json (dict): Raw JSON data for the drive.
        espn_instance (PYESPN): The ESPN API interface instance.
        event_instance (Event): The parent event this drive belongs to.
        plays (list[Play]): List of Play objects associated with this drive.
        description (str): Summary of the drive.
        id (str): Unique drive identifier.
        sequence_number (int): Order of the drive within the event.
        ref (str): API reference URL to this drive.
        start (dict): Metadata about how the drive started.
        end (dict): Metadata about how the drive ended.
        time_elapsed (dict): Duration of the drive.
        yards (int): Total yardage gained during the drive.
        is_score (bool): Whether the drive resulted in a score.
        offensive_plays (int): Number of offensive plays run during the drive.
        result (str): Raw result string (e.g., 'Touchdown', 'Punt').
        result_display (str): Formatted display result.
        team (Team): Team that had possession during the drive.
        end_team (Team): Team that was on defense at the end of the drive.
        plays_ref (str): API reference to the list of plays in this drive.
    """

    def __init__(self, drive_json, espn_instance, event_instance):
        """
        Initializes a Drive instance using the provided drive JSON.

        Args:
            drive_json (dict): JSON representation of the drive.
            espn_instance (PYESPN): The ESPN API interface instance.
            event_instance (Event): The event this drive belongs to.
        """
        self.drive_json = drive_json
        self._espn_instance = espn_instance
        self.event_instance = event_instance
        self._plays = None
        self._load_drive_data()

    def __repr__(self) -> str:
        """
        Returns a human-readable string representation of the Drive instance.

        Returns:
            str: A formatted string in the form "<Drive | Team Name | Drive Result>".
        """
        return f"<Drive | {self.team.name} | {self.result_display}>"

    def _load_drive_data(self):
        """
        Internal method to parse and load data from the drive JSON payload.
        Creates `Play` objects for each play in the drive.
        """
        self.description = self.drive_json.get('description')
        self.id = self.drive_json.get('id')
        self.sequence_number = self.drive_json.get('sequence_number')
        self.ref = self.drive_json.get('$ref')
        self.start = self.drive_json.get('start')
        self.end = self.drive_json.get('end')
        self.time_elapsed = self.drive_json.get('timeElapsed')
        self.yards = self.drive_json.get('yards')
        self.is_score = self.drive_json.get('isScore')
        self.offensive_plays = self.drive_json.get('offensivePlays')
        self.result = self.drive_json.get('result')
        self.result_display = self.drive_json.get('displayResult')
        team_id = get_team_id(self.drive_json.get('team', {}).get('$ref'))
        self.team = self._espn_instance.get_team_by_id(team_id=team_id)
        end_team_id = get_team_id(self.drive_json.get('endTeam', {}).get('$ref'))
        self.end_team = self._espn_instance.get_team_by_id(team_id=end_team_id)
        self.plays_ref = self.drive_json.get('plays', {}).get('$ref')

        self._load_plays()

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance
    
    @property
    def plays(self):
        """
            list[Play]: a list of plays for the drive
        """
        return self._plays

    def _load_plays(self):
        plays = []
        for play in self.drive_json.get('plays', {}).get('items'):
            plays.append(Play(play_json=play,
                              espn_instance=self._espn_instance,
                              event_instance=self.event_instance,
                              drive_instance=self))
        self._plays = plays

    def to_dict(self) -> dict:
        """
        Converts the Drive instance to its original JSON dictionary.

        Returns:
            dict: The drives's raw JSON data.
        """
        return self.drive_json


@validate_json("play_json")
class Play:
    """
    Represents a single play within an ESPN sports event.

    This class parses and stores data related to an individual play, such as the
    team involved, score, text descriptions, and various metadata about the play.

    Attributes:
        play_json (dict): Raw JSON data representing the play.
        espn_instance (PYESPN): The parent ESPN API wrapper instance.
        event_instance (Event): The parent event this play belongs to.
        drive_instance (Drive or None): The parent drive (if applicable).
        team (Team or None): The team associated with the play.
        id (str): Unique identifier for the play.
        text (str): Full text description of the play.
        short_text (str): Shortened description of the play.
        alt_text (str): Alternative description of the play.
        short_alt_text (str): Shortened alternative text.
        home_score (int): Score for the home team at this play.
        away_score (int): Score for the away team at this play.
        sequence_number (int): Play's sequence number in the event.
        type (str): Type of the play.
        period (dict): Information about the game period (e.g., quarter, half).
        clock (dict): Game clock status at time of play.
        scoring_play (bool): Whether the play resulted in scoring.
        priority (int): Display priority of the play.
        score_value (int): Amount of points scored on the play.
        start (dict): Start context for the play.
        end (dict): End context for the play.
        wallclock (str): Wallclock timestamp of the play.
        modified (str): Last modification time.
        probability (dict or None): Win probability shift, if present.
        stat_yardage (int or None): Yardage gained or lost (football-specific).
        participants (list or None): Athletes involved in the play.
        shooting_play (bool or None): Whether the play is a shooting play (basketball).
        coordinate (dict or None): X/Y position of the play (if supported).
    """

    def __init__(self, play_json, espn_instance,
                 event_instance, drive_instance):
        """
        Initializes a Play instance using the provided JSON data.

        Args:
            play_json (dict): The JSON data representing the play.
            espn_instance (PYESPN): The ESPN API interface instance.
            event_instance (Event): The event this play belongs to.
            drive_instance (Drive or None): The drive this play belongs to (if applicable).
        """
        self.play_json = play_json
        self._espn_instance = espn_instance
        self.event_instance = event_instance
        self.drive_instance = drive_instance
        self._load_play_data()

    def __repr__(self):
        """
        Returns a string representation of the Play instance.
        """
        return f"<Play | {self.team.name} | {self.short_text}>"

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    def _load_play_data(self):
        """
        Internal method to parse and assign play-related data from the JSON payload.
        """
        self.ref = self.play_json.get('$ref')
        self.id = self.play_json.get('id')
        self.text = self.play_json.get('text')
        self.alt_text = self.play_json.get('alternativeText')
        self.short_text = self.play_json.get('shortText')
        self.home_score = self.play_json.get('homeScore')
        self.away_score = self.play_json.get('awayScore')
        self.sequence_number = self.play_json.get('sequenceNumber')
        self.type = self.play_json.get('type')
        self.short_alt_text = self.play_json.get('shortAlternativeText')
        self.period = self.play_json.get('period')
        self.clock = self.play_json.get('clock')
        self.scoring_play = self.play_json.get('scoringPlay')
        self.priority = self.play_json.get('priority')
        self.score_value = self.play_json.get('scoreValue')
        self.start = self.play_json.get('start')
        self.end = self.play_json.get('end')
        self.wallclock = self.play_json.get('wallclock')
        self.modified = self.play_json.get('modified')
        # todo this is probably its own class
        self.probability = self.play_json.get('probability')
        self.stat_yardage = self.play_json.get('statYardage')
        if 'team' in self.play_json:
            team_id = get_team_id(self.play_json.get('team', {}).get('$ref'))
            self.team = self._espn_instance.get_team_by_id(team_id=team_id)
        else:
            self.team = None
        # todo these look like a list of athletes
        self.participants = self.play_json.get('participants')
        self.shooting_play = self.play_json.get('shootingPlay')
        self.coordinate = self.play_json.get('coordinate')

    def to_dict(self) -> dict:
        """
        Converts the Play instance to its original JSON dictionary.

        Returns:
            dict: The plays's raw JSON data.
        """
        return self.play_json


class PlayType:

    def __init__(self):
        pass



