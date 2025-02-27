from pyespn.nba.data import nba_teams_data
from pyespn.nba import get_team_info
import random


def get_random_nba_team_data():
    random_id = random.randint(1, len(nba_teams_data) - 2)
    selected_team = next((team for team in nba_teams_data if team["team_id"] == random_id), None)
    content = get_team_info(random_id)

    return selected_team, content


def test_nba_team_ids():
    local_team_data, api_team_data = get_random_nba_team_data()

    errors = []
    if local_team_data['team_abbv'] != api_team_data['abbreviation']:
        errors.append("Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data['location']:
        errors.append("Team city does not match")
    if local_team_data['team_name'] != api_team_data['name']:
        errors.append("Team name does not match")

    if errors:
        raise AssertionError("\n".join(errors))
