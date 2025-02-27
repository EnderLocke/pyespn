import requests
import json


def get_draft_pick_data(pick_round, pick, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/draft/rounds/{pick_round}/picks/{pick}'
    response = requests.get(url)
    content = json.loads(response.content)
    return content

