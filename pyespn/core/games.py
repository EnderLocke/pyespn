from pyespn.utilities import lookup_league_api_info
from pyespn.data.version import espn_api_version as v
import requests
import json


def get_game_info_core(event_id, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/events/{event_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)

    return content


def get_events_by_team(team_id, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/teams/{team_id}/events?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)


