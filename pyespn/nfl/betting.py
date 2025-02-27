# todo load up betting api calls here
# http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/0/teams/30/odds-records?lang=en&region=us
from pyespn.nfl.data import nfl_teams_data, AFC_CONFERENCE_MAP, NFC_CONFERENCE_MAP
from pyespn.utilities import get_team_id, get_type_futures, get_type_ats
import requests
import json


def _get_futures_year(year):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def _get_team_year_ats(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_year_nfl_super_bowl_futures(season, provider="DraftKings"):
    content = _get_futures_year(season)

    nfl_futures = get_type_futures(data=content,
                                   futures_type='NFL - Super Bowl Winner')

    provider_futures = next(future for future in nfl_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in nfl_teams_data if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value']
        }
        futures_list.append(item_dict)

    return futures_list


def get_year_afc_division_champ_futures(season, division, provider="DraftKings"):
    """

    :param season:
    :param division: must be one of east, west, south, north or conf
    :param provider:
    :return:
    """
    content = _get_futures_year(season)

    nfl_futures = get_type_futures(data=content,
                                   futures_type=AFC_CONFERENCE_MAP[division])

    provider_futures = next(future for future in nfl_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in nfl_teams_data if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value']
        }
        futures_list.append(item_dict)

    return futures_list


def get_year_nfc_division_champ_futures(season, division, provider="DraftKings"):
    """

    :param season:
    :param division: must be one of east, west, south, north or conf
    :param provider:
    :return:
    """
    content = _get_futures_year(season)

    nfl_futures = get_type_futures(data=content,
                                   futures_type=NFC_CONFERENCE_MAP[division])

    provider_futures = next(future for future in nfl_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in nfl_teams_data if team['team_id'] == team_id)

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
    ats = get_type_ats(data=content,
                        ats_type='atsOverall')
    return ats


def get_team_year_ats_favorite(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsFavorite')
    return ats


def get_team_year_ats_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsUnderdog')
    return ats


def get_team_year_ats_away(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsAway')
    return ats


def get_team_year_ats_home(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsHome')
    return ats


def get_team_year_ats_home_favorite(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsHomeFavorite')
    return ats


def get_team_year_ats_away_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsAwayUnderdog')
    return ats


def get_team_year_ats_home_underdog(team_id, season):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season)
    ats = get_type_ats(data=content,
                        ats_type='atsHomeUnderdog')
    return ats


def get_team_year_ml(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/0/teams/{team_id}/odds-records?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
