from pyespn import PYESPN
import pytest
import random
espn = PYESPN(sport_league='nfl')


def get_random_nfl_team_data(team_id):
    selected_team = next((team for team in espn.TEAM_ID_MAPPING if team["team_id"] == team_id), None)
    content = espn.get_team_info(team_id)

    return selected_team, content


@pytest.mark.parametrize("test_case", espn.TEAM_ID_MAPPING)
def test_nfl_team_ids(test_case):
    local_team_data, api_team_data = get_random_nfl_team_data(test_case.get('team_id'))

    errors = []
    print(local_team_data.get('team_id'))

    if local_team_data['team_abbv'] != api_team_data.abbreviation:
        errors.append(f"Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data.location:
        errors.append(f"Team city does not match {local_team_data['team_city']} -> {api_team_data.location}")
    if local_team_data.get('team_name') != api_team_data.name:
        errors.append(f"Team name does not match {local_team_data['team_name']} -> {api_team_data.name}")

    if errors:
        raise AssertionError("\n".join(errors))