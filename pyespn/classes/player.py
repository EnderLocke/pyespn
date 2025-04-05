from pyespn.core.decorators import validate_json
from pyespn.classes.vehicle import Vehicle


@validate_json('player_json')
class Player:
    from pyespn.core.orchestration import get_players_historical_stats_core
    """
    Represents a player within the ESPN API framework.

    This class stores player-related information and maintains a reference
    to a `PYESPN` instance, allowing access to league-specific details.

    Attributes:
        espn_instance (PYESPN): The parent `PYESPN` instance providing access to league details.
        player_json (dict): The raw player data retrieved from the ESPN API.
        api_ref (str | None): API reference link for the player.
        id (str | None): The unique identifier for the player.
        uid (str | None): The ESPN UID for the player.
        flag (dict | None): a dict with players nationality/flag (mostly for racing).
        guid (str | None): The GUID associated with the player.
        type (str | None): The type of player (e.g., 'athlete').
        alternate_ids (str | None): Alternative ID for the player.
        first_name (str | None): The player's first name.
        last_name (str | None): The player's last name.
        full_name (str | None): The player's full name.
        display_name (str | None): The player's display name.
        short_name (str | None): A shorter version of the player's name.
        weight (int | None): The player's weight in pounds.
        display_weight (str | None): Formatted string of the player's weight.
        height (int | None): The player's height in inches.
        display_height (str | None): Formatted string of the player's height.
        age (int | None): The player's age.
        date_of_birth (str | None): The player's date of birth (YYYY-MM-DD).
        debut_year (int | None): The player's debut year.
        links (list[dict]): A list of links related to the player.
        birth_city (str | None): The player's birth city.
        birth_state (str | None): The player's birth state.
        college_ref (str | None): Reference link to the player's college.
        slug (str | None): The player's slug identifier.
        jersey (str | None): The player's jersey number.
        position_ref (str | None): Reference link to the player's position.
        position_id (str | None): The player's position ID.
        position_name (str | None): The full name of the player's position.
        position_display_name (str | None): The display name of the position.
        position_abbreviation (str | None): The abbreviation of the position.
        position_leaf (bool | None): Indicates if the position is a leaf node.
        position_parent_ref (str | None): Reference link to the parent position.
        linked (str | None): Linked player information.
        team_ref (str | None): Reference link to the player's team.
        statistics_ref (str | None): Reference link to the player's statistics.
        contracts_ref (str | None): Reference link to the player's contracts.
        experience_years (int | None): The number of years of experience the player has.
        active (bool | None): Indicates whether the player is currently active.
        status_id (str | None): The player's status ID.
        status_name (str | None): The player's status name.
        status_type (str | None): The type of player status.
        status_abbreviation (str | None): Abbreviated form of the player's status.
        statistics_log_ref (str | None): Reference link to the player's statistics log.

    Methods:
        to_dict() -> dict:
            Returns the raw player JSON data as a dictionary.
    """

    def __init__(self, espn_instance, player_json: dict):
        """
        Initializes a Player instance.

        Args:
            espn_instance (PYESPN): The parent `PYESPN` instance, providing access to league details.
            player_json (dict): The raw player data retrieved from the ESPN API.
        """
        self.player_json = player_json
        self.espn_instance = espn_instance
        self.stats = {}
        self._set_player_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Player instance.

        Returns:
            str: A formatted string with the players's name, position and jersey.
        """
        return f"<Player | {self.full_name}, {self.position_abbreviation} ({self.jersey})>"

    def _set_player_data(self):
        """
        Extracts and sets player data from the provided JSON.
        """
        self.api_ref = self.player_json.get('$ref')
        self.id = self.player_json.get('id')
        self.uid = self.player_json.get('uid')
        self.guid = self.player_json.get('guid')
        self.type = self.player_json.get('type')
        self.flag = self.player_json.get('flag')
        self.citizenship = self.player_json.get('citizenship')
        self.experience = self.player_json.get('experience')
        self.event_log = self.player_json.get('eventLog')
        self.stats_log = self.player_json.get('statisticslog')
        self.alternate_ids = self.player_json.get('alternateIds', {}).get('sdr')
        self.first_name = self.player_json.get('firstName')
        self.last_name = self.player_json.get('lastName')
        self.full_name = self.player_json.get('fullName')
        if not self.full_name:
            self.full_name = self.first_name + ' ' + self.last_name
        self.display_name = self.player_json.get('displayName')
        self.short_name = self.player_json.get('shortName')
        self.weight = self.player_json.get('weight')
        self.display_weight = self.player_json.get('displayWeight')
        self.height = self.player_json.get('height')
        self.display_height = self.player_json.get('displayHeight')
        self.age = self.player_json.get('age')
        self.date_of_birth = self.player_json.get('dateOfBirth')
        self.debut_year = self.player_json.get('debutYear')
        self.college_athlete_ref = self.player_json.get('collegeAthlete', {}).get('$ref')

        self.links = self.player_json.get('links', [])

        birth_place = self.player_json.get('birthPlace', {})
        self.birth_city = birth_place.get('city')
        self.birth_state = birth_place.get('state')

        self.college_ref = self.player_json.get('college', {}).get('$ref')
        self.slug = self.player_json.get('slug')
        self.jersey = self.player_json.get('jersey', '--')

        position = self.player_json.get('position', {})
        self.position_ref = position.get('$ref')
        self.position_id = position.get('id')
        self.position_name = position.get('name')
        self.position_display_name = position.get('displayName')
        self.position_abbreviation = position.get('abbreviation')
        self.position_leaf = position.get('leaf')
        self.position_parent_ref = position.get('parent', {}).get('$ref')

        self.linked = self.player_json.get('linked')
        self.team_ref = self.player_json.get('team', {}).get('$ref')
        self.statistics_ref = self.player_json.get('statistics', {}).get('$ref')
        self.contracts_ref = self.player_json.get('contracts', {}).get('$ref')

        experience = self.player_json.get('experience', {})
        if type(experience) == dict:
            self.experience_years = experience.get('years')
        elif type(experience) == int:
            self.experience_years = experience

        self.active = self.player_json.get('active')

        status = self.player_json.get('status', {})
        self.status_id = status.get('id')
        self.status_name = status.get('name')
        self.status_type = status.get('type')
        self.status_abbreviation = status.get('abbreviation')

        self.statistics_log_ref = self.player_json.get('statisticslog', {}).get('$ref')

        if 'vehicles' in self.player_json:
            self.vehicles = []
            for vehicle in self.player_json.get('vehicles'):
                self.vehicles.append(Vehicle(vehicle_json=vehicle,
                                             espn_instance=self.espn_instance))

    def load_player_historical_stats(self) -> None:
        """
        Loads the historical statistics for the player.

        This method fetches and assigns the player's historical stats using the ESPN API.
        The stats are stored in the `self.stats` attribute.

        Returns:
            None
        """

        self.stats = self.get_players_historical_stats_core(player_id=self.id,
                                                            league_abbv=self.espn_instance.league_abbv,
                                                            espn_instance=self.espn_instance)

    def to_dict(self) -> dict:
        """
        Returns the raw player JSON data as a dictionary.

        Returns:
            dict: The original player data retrieved from the ESPN API.
        """
        return self.player_json


@validate_json("recruit_json")
class Recruit:
    """
    Represents a recruit in the ESPN recruiting system.

    Attributes:
        recruit_json (dict): The JSON data containing recruit details.
        espn_instance: The ESPN API instance.
        api_ref (str): API reference URL for the recruit.
        athlete (dict): Dictionary containing athlete details.
        id (str): The recruit's unique identifier.
        uid (str): The unique identifier for the recruit.
        guid (str): The global unique identifier.
        type (str): Type of recruit data.
        alternate_ids (str): Alternative ID for the recruit.
        first_name (str): First name of the recruit.
        last_name (str): Last name of the recruit.
        full_name (str): Full name of the recruit.
        display_name (str): Display name of the recruit.
        short_name (str): Shortened version of the recruit's name.
        weight (int): The recruit's weight in pounds (if available).
        height (int): The recruit's height in inches (if available).
        recruiting_class (str): The recruiting class year.
        grade (str): Grade assigned to the recruit.
        links (list): A list of links related to the recruit.
        birth_city (str): City where the recruit was born.
        birth_state (str): State where the recruit was born.
        high_school_id (str): The recruit's high school ID.
        high_school_name (str): Name of the recruit's high school.
        high_school_state (str): State where the recruit's high school is located.
        slug (str): A unique slug identifier for the recruit.
        position_ref (str): API reference for the recruit's position.
        position_id (str): The recruit's position ID.
        position_name (str): Name of the recruit's position.
        position_display_name (str): Display name of the position.
        position_abbreviation (str): Abbreviated name of the recruit's position.
        position_leaf (bool): Whether the position is a leaf node in the hierarchy.
        position_parent_ref (str): Reference to the parent position (if any).
        linked (dict): Additional linked data related to the recruit.
        schools (list): A list of schools associated with the recruit.
        status_id (str): The ID representing the recruit's status.
        status_name (str): Description of the recruit's status.
        rank (int or None): The recruit's overall rank, extracted from attributes.

    Methods:
        __repr__():
            Returns a string representation of the recruit instance.

        _set_recruit_data():
            Extracts and sets player data from the provided JSON.
    """

    def __init__(self, recruit_json: dict, espn_instance):
        """
        Initializes a Recruit instance.

        Args:
            recruit_json (dict): The JSON data containing recruit details.
            espn_instance (PYESPN): The ESPN API instance.
        """
        self.recruit_json = recruit_json
        self.espn_instance = espn_instance
        self._set_recruit_data()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Recruit instance.

        Returns:
            str: A formatted string with the recruits's name, debut year and jersey.
        """
        return f"<Recruit | {self.full_name}, {self.position_abbreviation} ({self.recruiting_class})>"

    def _set_recruit_data(self):
        """
        Extracts and sets recruit data from the provided JSON.
        """
        self.api_ref = self.recruit_json.get('$ref')
        self.athlete = self.recruit_json.get('athlete')
        self.id = self.athlete.get('id')
        self.uid = self.recruit_json.get('uid')
        self.guid = self.recruit_json.get('guid')
        self.type = self.recruit_json.get('type')
        self.alternate_ids = self.athlete.get('alternateIds', {}).get('sdr')
        self.first_name = self.athlete.get('firstName')
        self.last_name = self.athlete.get('lastName')
        self.full_name = self.athlete.get('fullName')
        self.display_name = self.athlete.get('displayName')
        self.short_name = self.athlete.get('shortName')
        self.weight = self.athlete.get('weight')
        self.height = self.athlete.get('height')
        self.recruiting_class = self.recruit_json.get("recruitingClass")
        self.grade = self.recruit_json.get('grade')

        self.links = self.recruit_json.get('links', [])

        birth_place = self.athlete.get('hometown', {})
        self.birth_city = birth_place.get('city')
        self.birth_state = birth_place.get('state')

        high_school = self.athlete.get('highSchool', {})
        self.high_school_id = high_school.get('id')
        self.high_school_name = high_school.get('name')
        self.high_school_state = high_school.get('address', {}).get('state')

        self.slug = self.recruit_json.get('slug')

        position = self.athlete.get('position', {})
        self.position_ref = position.get('$ref')
        self.position_id = position.get('id')
        self.position_name = position.get('name')
        self.position_display_name = position.get('displayName')
        self.position_abbreviation = position.get('abbreviation')
        self.position_leaf = position.get('leaf')
        self.position_parent_ref = position.get('parent', {}).get('$ref')

        self.linked = self.recruit_json.get('linked')
        self.schools = self.recruit_json.get('schools')

        status = self.recruit_json.get('status', {})
        self.status_id = status.get('id')
        self.status_name = status.get('description')

        self.rank = next((int(attr.get('displayValue')) for attr in self.recruit_json.get('attributes', []) if attr.get("name", '').lower() == "rank"), None)

