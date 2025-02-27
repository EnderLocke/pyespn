from pyespn.nfl.data import nfl_teams_data
import random
import requests
import json


def get_random_nfl_team_data():
    random_id = random.randint(1, len(nfl_teams_data) - 2)
    api_url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/{random_id}'
    selected_team = next((team for team in nfl_teams_data if team["team_id"] == random_id), None)
    response = requests.get(api_url)
    content = json.loads(response.content)

    return selected_team, content


def test_nfl_team_ids():
    local_team_data, api_team_data = get_random_nfl_team_data()

    assert local_team_data['team_abbv'] == api_team_data['abbreviation']
