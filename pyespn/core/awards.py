from pyespn.utilities import lookup_league_api_info, get_athlete_id
from pyespn.core.players import get_player_info_core
from pyespn.data.version import espn_api_version as v
import requests
import json


def get_awards_core(season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/awards?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    awards_urls = content['items']
    awards = []
    for award_url in awards_urls:
        award_response = requests.get(award_url['$ref'])
        award_content = json.loads(award_response.content)
        for winner in award_content['winners']:
            athlete_id = get_athlete_id(winner['athlete']['$ref'])
            athlete_info = get_player_info_core(player_id=athlete_id,
                                                league_abbv=league_abbv)
            this_award = {
                'athlete_id': athlete_id,
                'award': award_content['name'],
                'award_description': award_content.get('description'),
                'winner': athlete_info['fullName'],
                'position': athlete_info['position']['abbreviation']

            }

            awards.append(this_award)

    return awards

