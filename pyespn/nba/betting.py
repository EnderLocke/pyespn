# todo add any betting apis here

# http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2023/futures?lang=en&region=us
from pyespn.nba.data import nba_teams_data
from pyespn.utilities import get_team_id
import requests
import json


def _get_futures_year(year):
    url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def _get_type_futures(data, futures_type):
    try:
        result = next(item for item in data["items"] if item["name"] == futures_type)
    except StopIteration:
        result = None
    return result


def _get_type_ats(data, ats_type):
    try:
        result = next(item for item in data["items"] if item["type"]["name"] == ats_type)
    except StopIteration:
        result = None
    return result


def _get_team_year_ats(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_year_nba_champ_futures(season, provider="DraftKings"):
    content = _get_futures_year(season)

    nba_futures = _get_type_futures(data=content,
                                    futures_type='NBA - Winner')

    provider_futures = next(future for future in nba_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in nba_teams_data if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value']
        }
        futures_list.append(item_dict)

    
    return futures_list


def get_team_year_ats_overall(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                    ats_type='atsOverall')
    return ats


def get_team_year_ats_favorite(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                    ats_type='atsFavorite')
    return ats


def get_team_year_ats_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsUnderdog')
    return ats


def get_team_year_ats_away(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsAway')
    return ats


def get_team_year_ats_home(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsHome')
    return ats


def get_team_year_ats_home_favorite(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsHomeFavorite')
    return ats


def get_team_year_ats_away_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsAwayUnderdog')
    return ats


def get_team_year_ats_home_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = _get_type_ats(data=content,
                        ats_type='atsHomeUnderdog')
    return ats
