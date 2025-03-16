# todo there is venue info could add a lookup for that specirfcally
#  what else is out there/ add a teams logo call (its within team info data)
from pyespn.utilities import lookup_league_api_info
from pyespn.data.version import espn_api_version as v
import requests
import json


def get_season_team_stats_core(season, team, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_info_core(team_id, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/teams/{team_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_logo_img(team_id, league_abbv):
    team_content = get_team_info_core(team_id=team_id,
                                      league_abbv=league_abbv)
    logo_url = team_content.get('logos', [{'href': None}])[0].get('href')
    logo = None
    if logo_url:
        logo_response = requests.get(logo_url)
        logo = logo_response.content

    return logo


def get_team_colors_core(team_id, league_abbv):
    team_content = get_team_info_core(team_id=team_id,
                                      league_abbv=league_abbv)
    primary_color = team_content.get('color')
    alt_color = team_content.get('alternateColor')

    return {
        'primary_color': primary_color,
        'alt_color': alt_color
        }


def get_home_venue(team_id, league_abbv):
    team_content = get_team_info_core(team_id=team_id,
                                      league_abbv=league_abbv)

    venue_info = team_content.get('venue')

    venue = {
        'id': venue_info['id'],
        'name': venue_info['fullName'],
        'address': venue_info['address'],
        'grass': venue_info['grass'],
        'indoor': venue_info['indoor'],
        'img_url': venue_info.get('images', [{'href': None}])[0].get('href')
    }

    return venue
