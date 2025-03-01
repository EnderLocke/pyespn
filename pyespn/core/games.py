from pyespn.utilities import lookup_league_api_info
import requests
import json


def get_game_info_core(event_id, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/events/{event_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)

    return content
