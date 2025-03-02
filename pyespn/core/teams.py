# todo there is venue info could add a lookup for that specirfcally
#  what else is out there/ add a teams logo call (its within team info data)
#  build out a lookup table for a team name its not many lines
from pyespn.utilities import lookup_league_api_info
import requests
import json


def get_season_team_stats_core(season, team, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_info_core(team_id, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/teams/{team_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
