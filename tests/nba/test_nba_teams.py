from pyespn import PYESPN
import random
import pytest

espn = PYESPN(sport_league='nba')

def get_random_nba_team_data(team_id):

    selected_team = next((team for team in espn.TEAM_ID_MAPPING if team["team_id"] == team_id), None)
    content = espn.get_team_info(team_id=team_id)

    return selected_team, content


@pytest.mark.parametrize("test_case", espn.TEAM_ID_MAPPING)
def test_nba_team_ids(test_case):
    local_team_data, api_team_data = get_random_nba_team_data(test_case.get('team_id'))

    errors = []
    print(local_team_data.get('team_id'))
    if local_team_data['team_abbv'] != api_team_data.abbreviation:
        errors.append("Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data.location:
        errors.append("Team city does not match")
    if local_team_data['team_name'] != api_team_data.name:
        errors.append("Team name does not match")

    if errors:
        raise AssertionError("\n".join(errors))
