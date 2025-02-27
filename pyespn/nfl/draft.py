# todo add api call to the draft api

# http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/draft/rounds/1/picks/22?lang=en&region=us
import requests
import json


def get_draft_pick_data(round, pick, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/draft/rounds/{round}/picks/{pick}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content

