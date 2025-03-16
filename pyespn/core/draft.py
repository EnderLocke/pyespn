from pyespn.utilities import lookup_league_api_info
from pyespn.data.version import espn_api_version as v
import requests
import json


def get_draft_pick_data_core(pick_round, pick, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds/{pick_round}/picks/{pick}'
    response = requests.get(url)
    content = json.loads(response.content)
    return content

