from pyespn.utilities import lookup_league_api_info
import requests
import json


def get_futures_year_core(year, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_year_ats_core(team_id, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content

