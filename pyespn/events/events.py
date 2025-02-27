import requests
import json


def get_event_info(sport, league, event_id):
    url = f'http://sports.core.api.espn.com/v2/sports/{sport}/leagues/{league}/events/{event_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)

    return content
