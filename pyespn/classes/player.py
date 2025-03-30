from pyespn.core.decorators import validate_json


@validate_json('player_json')
class Player:
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
        guid (str | None): The GUID associated with the player.
        type (str | None): The type of player (e.g., "athlete").
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
        self._set_player_data()

    def __repr__(self):
        """
        Returns a string representation of the Player instance.

        Returns:
            str: A formatted string with the players's name, debut year and jersey.
        """
        return f"<Player | {self.full_name}, {self.debut_year} ({self.jersey})>"

    def _set_player_data(self):
        self.api_ref = self.player_json.get('$ref')
        self.id = self.player_json.get('id')
        self.uid = self.player_json.get('uid')
        self.guid = self.player_json.get('guid')
        self.type = self.player_json.get('type')
        self.alternate_ids = self.player_json.get('alternateIds', {}).get('sdr')
        self.first_name = self.player_json.get('firstName')
        self.last_name = self.player_json.get('lastName')
        self.full_name = self.player_json.get('fullName')
        self.display_name = self.player_json.get('displayName')
        self.short_name = self.player_json.get('shortName')
        self.weight = self.player_json.get('weight')
        self.display_weight = self.player_json.get('displayWeight')
        self.height = self.player_json.get('height')
        self.display_height = self.player_json.get('displayHeight')
        self.age = self.player_json.get('age')
        self.date_of_birth = self.player_json.get('dateOfBirth')
        self.debut_year = self.player_json.get('debutYear')

        self.links = self.player_json.get('links', [])

        birth_place = self.player_json.get('birthPlace', {})
        self.birth_city = birth_place.get('city')
        self.birth_state = birth_place.get('state')

        self.college_ref = self.player_json.get('college', {}).get('$ref')
        self.slug = self.player_json.get('slug')
        self.jersey = self.player_json.get('jersey')

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
        self.experience_years = experience.get('years')

        self.active = self.player_json.get('active')

        status = self.player_json.get('status', {})
        self.status_id = status.get('id')
        self.status_name = status.get('name')
        self.status_type = status.get('type')
        self.status_abbreviation = status.get('abbreviation')

        self.statistics_log_ref = self.player_json.get('statisticslog', {}).get('$ref')

    def to_dict(self):
        return self.player_json
