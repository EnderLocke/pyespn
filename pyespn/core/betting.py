from pyespn.utilities import lookup_league_api_info, get_team_id, get_type_futures, get_type_ats
from pyespn.data.betting import LEAGUE_CHAMPION_FUTURES_MAP
from pyespn.data.teams import LEAGUE_TEAMS_MAPPING
import requests
import json


def _get_futures_year(year, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def _get_team_year_ats(team_id, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_year_league_champions_futures_core(season, league_abbv, provider="DraftKings"):

    content = _get_futures_year(year=season,
                                league_abbv=league_abbv)

    league_futures = get_type_futures(data=content,
                                      futures_type=LEAGUE_CHAMPION_FUTURES_MAP[league_abbv])

    provider_futures = next(future for future in league_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in LEAGUE_TEAMS_MAPPING[league_abbv] if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value']
        }
        futures_list.append(item_dict)

    return futures_list


