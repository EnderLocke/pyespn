import json
import requests
from pyespn.utilities import lookup_league_api_info
from pyespn.data.version import espn_api_version as v
from pyespn.classes import League


def get_league_info_core(league_abbv, espn_instance):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}'
    response = requests.get(url)
    content = json.loads(response.content)
    current_league = League(league_json=content,
                            espn_instance=espn_instance)
    return current_league
