# http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2025/types/2/standings?lang=en&region=us
# todo golf standings are different
from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.standings import Standings
import requests
import json


def get_standings_core(season, league_abbv, espn_instance):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/standings'
    content = fetch_espn_data(url)
    page_count = content.get('count')

    standings = []
    standings_url = []
    for page in range(1, page_count + 1):
        paged_url = url + f'?page={page}'
        paged_content = fetch_espn_data(paged_url)

        for item in paged_content.get('items', []):
            standings_url.append(item.get('$ref'))

    for standing in standings_url:
        standing_content = fetch_espn_data(standing)
        standings.append(Standings(standings_json=standing_content,
                                   espn_instance=espn_instance))
