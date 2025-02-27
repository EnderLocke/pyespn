import requests
import json


def get_game_info(event_id):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{event_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)

    return content
