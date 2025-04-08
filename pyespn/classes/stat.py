from pyespn.classes.player import Player
from pyespn.utilities import fetch_espn_data, get_team_id, get_athlete_id


class Stat:
    """
    Represents a statistical record for a player within a given season.

    Attributes:
        stat_json (dict): The raw JSON data containing the statistical information.
        espn_instance (PYESPN): The ESPN API instance used for retrieving additional data.
        category (str): The category of the stat (e.g., 'batting', 'pitching').
        season (int): The season in which the stats were recorded.
        player_id (str): The unique ID of the player.
        stat_value (float | int): The value of the stat.
        stat_type_abbreviation (str): Abbreviation of the stat type.
        description (str): A description of the stat.
        name (str): The name of the stat (e.g., 'home runs', 'strikeouts').
        type (str): The type of stat (e.g., 'single', 'accumulated').
        per_game_value (float | None): The value per game, if available.
        rank (int | None): The player's rank in the stat category.

    Methods:
        __repr__() -> str:
            Returns a string representation of the Stat instance, including the stat name, season, and value.

        _set_stats_data() -> None:
            Extracts and sets the statistical attributes from the provided JSON data.
    """

    def __init__(self, stat_json, espn_instance):
        """
        Initializes a Stat instance.

        Args:
            stat_json (dict): The JSON object containing the stat data.
            espn_instance (PYESPN): An instance of the ESPN API client.
        """
        self.stat_json = stat_json
        self.espn_instance = espn_instance
        self._set_stats_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Stat instance.

        Returns:
            str: A formatted string with the stat name, value, and season.
        """
        return f"<Stat | {self.season}-{self.name}: {self.stat_value}>"

    def _set_stats_data(self):
        """
        Extracts and sets the statistical attributes from the provided JSON data.
        """
        self.category = self.stat_json.get('category')
        self.season = self.stat_json.get('season')
        self.player_id = self.stat_json.get('player_id')
        self.stat_value = self.stat_json.get('stat_value')
        if not self.stat_value:
            self.stat_value = self.stat_json.get('value')

        self.stat_type_abbreviation = self.stat_json.get('stat_type_abbreviation')
        if not self.stat_type_abbreviation:
            self.stat_type_abbreviation = self.stat_json.get('abbreviation')
        self.description = self.stat_json.get('description')
        self.name = self.stat_json.get('name')
        if not self.name:
            self.name = self.stat_json.get("displayName")
        self.type = self.stat_json.get('type')
        self.per_game_value = self.stat_json.get('perGameValue')
        self.rank = self.stat_json.get('rank')


class Record:
    """
    Represents a statistical record for a player, team, or manufacturer in ESPN's data.

    This class extracts and organizes record-related information from the provided JSON data,
    including general details and associated statistics.

    Attributes:
        espn_instance (object): An instance of the ESPN API client.
        record_json (dict): The raw JSON data containing record details.
        stats (list): A list of Stat objects representing individual statistical entries.
        id (str or None): The unique identifier for the record.
        ref (str or None): The API reference URL for the record.
        name (str or None): The full name of the record.
        abbreviation (str or None): The abbreviated form of the record name.
        display_name (str or None): The display name for the record.
        short_display_name (str or None): The short display name for the record.
        description (str or None): A brief description of the record.
        type (str or None): The type of record (e.g., season record, career record).

    Methods:
        _load_record_data(): Extracts and assigns values from record_json to class attributes.
    """

    def __init__(self, record_json, espn_instance):
        """
        Initializes a Record object.

        Args:
            record_json (dict): The JSON data representing the record.
            espn_instance (object): An instance of the ESPN API client.
        """
        self.espn_instance = espn_instance
        self.record_json = record_json
        self.stats = []
        self._load_record_data()

    def __repr__(self):
        """
        Returns a string representation of the Record instance.

        The representation includes the record's display name and abbreviation
        for easy identification.
        """
        return f"<Record | {self.display_name} ({self.abbreviation})>"

    def _load_record_data(self):
        """
        Parses and assigns values from record_json to class attributes.

        This method extracts record details such as names, abbreviations, descriptions, and stats.
        It also initializes Stat objects for each statistical entry found in the record.
        """
        self.id = self.record_json.get('id')
        self.ref = self.record_json.get('$ref')
        self.name = self.record_json.get('name')
        self.summary = self.record_json.get('summary')
        self.display_value = self.record_json.get('displayValue')
        self.value = self.record_json.get('value')
        self.abbreviation = self.record_json.get('abbreviation')
        self.display_name = self.record_json.get('displayName')
        self.short_display_name = self.record_json.get('shortDisplayName')
        self.description = self.record_json.get('description')
        self.type = self.record_json.get('type')
        self.name = self.record_json.get('name')
        for stat in self.record_json.get('stats', []):
            self.stats.append(Stat(stat_json=stat,
                                   espn_instance=self.espn_instance))


class LeaderCategory:
    """
    Represents a category of statistical leaders for a given season.

    The LeaderCategory class is responsible for storing and managing information
    about a specific leader category, such as the category's name, abbreviation,
    and the athletes who are the statistical leaders in that category for the
    specified season. The data is loaded from a given JSON object, and the class
    provides methods to represent and interact with this data.

    Attributes:
        leader_cat_json (dict): The JSON data containing information about the leader category.
        espn_instance (object): The instance of the ESPN-related class for interacting with ESPN data.
        athletes (dict): A dictionary holding athletes (as instances of the Leader class) for each season.
        season (str or int): The season for which the leader category data is relevant.
        abbreviation (str): The abbreviation of the leader category.
        name (str): The name of the leader category.
        display_name (str): The display name of the leader category.

    Methods:
        __repr__(): Returns a string representation of the LeaderCategory instance.
        _load_leaders_data(): Loads the leader data from the provided JSON and initializes the class attributes.
    """

    def __init__(self, leader_cat_json, espn_instance, season):
        """
        Initializes a LeaderCategory instance with the given data.

        Args:
            leader_cat_json (dict): The JSON data for the leader category.
            espn_instance (object): An instance of the ESPN class for interacting with ESPN data.
            season (str or int): The season the leader category is related to.
        """
        self.leader_cat_json = leader_cat_json
        self.espn_instance = espn_instance
        self.athletes = {}
        self.season = season
        self._load_leaders_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Leader Category instance.

        Returns:
            str: A formatted string with the leader info.
        """
        return f"<LeaderCategory | {self.season}-{self.display_name}>"

    def _load_leaders_data(self):
        """
        Loads the leaders' data from the provided JSON.

        This method extracts relevant information (such as abbreviation, name,
        display name, and athletes) from the `leader_cat_json` and populates
        the corresponding attributes. It also creates instances of the `Leader`
        class for each athlete and stores them in the `athletes` dictionary,
        indexed by season.
        """
        self.abbreviation = self.leader_cat_json.get('abbreviation')
        self.name = self.leader_cat_json.get('name')
        self.abbreviation = self.leader_cat_json.get('abbreviation')
        self.display_name = self.leader_cat_json.get('displayName')
        all_athletes = []
        rank = 1
        for ath in self.leader_cat_json.get('leaders', []):
            all_athletes.append(Leader(leader_json=ath,
                                       espn_instance=self.espn_instance,
                                       season=self.season,
                                       rank=rank))
            rank += 1
        self.athletes[self.season] = all_athletes


class Leader:
    """
    Represents a statistical leader in a specific category for a given season.

    The Leader class encapsulates information about an athlete (Player) and their
    team in the context of a statistical category. It fetches relevant data from
    the provided JSON, stores the athlete and team information, and tracks the
    leader's rank and statistical value.

    Attributes:
        leader_json (dict): The JSON data for the leader.
        espn_instance (object): The instance of the ESPN-related class for interacting with ESPN data.
        rank (int): The rank of the athlete in the leader category.
        athlete (Player or None): The Player instance representing the athlete who is the leader.
        team (Team or None): The Team instance representing the team of the leader.
        value (float): The statistical value of the leader in the category.
        rel (dict or None): The relationship data in the leader JSON, which may contain references to athlete and team data.

    Methods:
        __repr__(): Returns a string representation of the Leader instance.
        _load_leader_data(): Loads the leader data from the provided JSON, initializing athlete, team, and value.
    """

    def __init__(self, leader_json, espn_instance, season, rank):
        """
        Initializes a Leader instance with the given leader data.

        Args:
            leader_json (dict): The JSON data representing the leader's information.
            espn_instance (object): An instance of the ESPN class for interacting with ESPN data.
            rank (int): The rank of the athlete in the leader category.
        """
        self.leader_json = leader_json
        self.espn_instance = espn_instance
        self.rank = rank
        self.season = season
        self.athlete = None
        self.team = None
        self._load_leader_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Leader instance.

        Returns:
            str: A formatted string with the Leader Info.
        """

        return f"<Leader - {self.rank} | {self.athlete.full_name}-{self.value}: {self.team.name}>"

    def _load_leader_data(self):
        """
        Loads the leader's data from the provided JSON.

        This method extracts the statistical value, the athlete reference, and
        the team reference from the leader's JSON data. It fetches the athlete
        information by calling `fetch_espn_data` if an athlete reference exists,
        and it fetches the team information by calling `get_team_id` and
        `get_team_by_id` if a team reference exists.

        This method initializes the athlete and team attributes, as well as the
        statistical value and rank.

        """
        self.value = self.leader_json.get('value', 0)
        self.rel = self.leader_json.get('rel')

        if 'team' in self.leader_json:
            team_id = get_team_id(self.leader_json.get('team', {}).get('$ref'))
            self.team = self.espn_instance.get_team_by_id(team_id=team_id)

        if 'athlete' in self.rel:
            try:
                athlete_id = get_athlete_id(self.leader_json.get('athlete', {}).get('$ref'))
                self.athlete = self.team.get_player_by_season_id(season=self.season, player_id=athlete_id)
            except Exception as e:
                print(e)
            finally:
                if not self.athlete:
                    #print('athlete not found')
                    athlete_content = fetch_espn_data(self.leader_json.get('athlete', {}).get('$ref'))
                    self.athlete = Player(player_json=athlete_content,
                                          espn_instance=self.espn_instance)
