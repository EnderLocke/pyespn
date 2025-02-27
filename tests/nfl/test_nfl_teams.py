from pyespn.nfl.data import nfl_teams_data
from pyespn.nfl import get_team_info
from pytest_check import check
import random


def get_random_nfl_team_data():
    random_id = random.randint(1, len(nfl_teams_data) - 2)
    selected_team = next((team for team in nfl_teams_data if team["team_id"] == random_id), None)
    content = get_team_info(random_id)

    return selected_team, content


def test_nfl_team_ids():
    local_team_data, api_team_data = get_random_nfl_team_data()

    with check:
        assert local_team_data['team_abbv'] == api_team_data['abbreviation']
        assert local_team_data['team_city'] == api_team_data['location']
        assert local_team_data['team_name'] == api_team_data['name']
