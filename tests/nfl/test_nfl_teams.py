from pyespn.nfl.data import nfl_teams_data
import random
import requests
import json


def check_nfl_team_id():
    random_id = random.randint(1, len(nfl_teams_data) - 2)
    api_url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/{random_id}'
    selected_team = next((team for team in nfl_teams_data if team["team_id"] == random_id), None)
    response = requests.get(api_url)
    content = json.loads(response.content)

    assert selected_team['team_abbv'] == content['abbreviation']




