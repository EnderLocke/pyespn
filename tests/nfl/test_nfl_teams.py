from pyespn import PYESPN

import random


def get_random_nfl_team_data():
    espn = PYESPN(sport_league='nfl')
    random_id = random.randint(1, len(espn.TEAM_ID_MAPPING) - 2)
    selected_team = next((team for team in espn.TEAM_ID_MAPPING if team["team_id"] == random_id), None)
    content = espn.get_team_info(random_id)

    return selected_team, content


def test_nfl_team_ids():
    local_team_data, api_team_data = get_random_nfl_team_data()

    errors = []
    if local_team_data['team_abbv'] != api_team_data['abbreviation']:
        errors.append("Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data['location']:
        errors.append("Team city does not match")
    if local_team_data['team_name'] != api_team_data['name']:
        errors.append("Team name does not match")

    if errors:
        raise AssertionError("\n".join(errors))