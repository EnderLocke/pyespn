from pyespn.core.decorators import validate_json


@validate_json('player_json')
class Player:

    def __init__(self, espn_instance, player_json):
        self.player_json = player_json
        self.espn_instance = espn_instance
        self._set_player_data()

    def __repr__(self):
        """
        Returns a string representation of the Player instance.

        Returns:
            str: A formatted string with the players's name, debut year and jersey.
        """
        return f"<Player {self.full_name}, {self.debut_year} ({self.jersey})>"

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
