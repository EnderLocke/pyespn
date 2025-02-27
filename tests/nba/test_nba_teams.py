from pyespn.nba.data import nba_teams_data
from pytest_check import check
import random
import requests
import json


def get_random_nba_team_data():
    random_id = random.randint(1, len(nba_teams_data) - 2)
    api_url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/teams/{random_id}'
    selected_team = next((team for team in nba_teams_data if team["team_id"] == random_id), None)
    response = requests.get(api_url)
    content = json.loads(response.content)

    return selected_team, content


def test_nba_team_ids():
    local_team_data, api_team_data = get_random_nba_team_data()

    with check:
        assert local_team_data['team_abbv'] == api_team_data['abbreviation']
        assert local_team_data['team_city'] == api_team_data['location']
        assert local_team_data['team_name'] == api_team_data['name']
