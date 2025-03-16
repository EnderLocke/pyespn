from pyespn.utilities import lookup_league_api_info, get_team_id, get_type_futures, get_type_ats
from pyespn.data.betting import LEAGUE_CHAMPION_FUTURES_MAP, LEAGUE_DIVISION_FUTURES_MAPPING
from pyespn.data.teams import LEAGUE_TEAMS_MAPPING
from pyespn.data.version import espn_api_version as v
import requests
import json


def _get_team_ats(team_id, season, ats_type, league_abbv):
    content = _get_team_year_ats(team_id=team_id,
                                 season=season,
                                 league_abbv=league_abbv)
    ats = get_type_ats(data=content,
                       ats_type=ats_type)
    return ats


def _get_futures_year(year, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def _get_team_year_ats(team_id, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_year_league_champions_futures_core(season, league_abbv, provider="Betradar"):

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


def get_division_champ_futures_core(season, division, league_abbv, provider="Betradar"):
    """

    :param season:
    :param division: must be one of east, west, south, north or conf
    :param provider:
    :return:
    """
    content = _get_futures_year(season,
                                league_abbv=league_abbv)

    league_futures = get_type_futures(data=content,
                                      futures_type=LEAGUE_DIVISION_FUTURES_MAPPING[league_abbv][division])

    provider_futures = next(future for future in league_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in LEAGUE_TEAMS_MAPPING[league_abbv] if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value'],
            'team_ref': item['team']['$ref'],
            'team_id': team_id
        }
        futures_list.append(item_dict)

    return futures_list


def get_team_year_ats_overall_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsOverall',
                         league_abbv=league_abbv)


def get_team_year_ats_favorite_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsFavorite',
                         league_abbv=league_abbv)


def get_team_year_ats_underdog_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsUnderdog',
                         league_abbv=league_abbv)


def get_team_year_ats_away_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsAway',
                         league_abbv=league_abbv)


def get_team_year_ats_home_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsHome',
                         league_abbv=league_abbv)


def get_team_year_ats_home_favorite_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsHomeFavorite',
                         league_abbv=league_abbv)


def get_team_year_ats_away_underdog_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsAwayUnderdog',
                         league_abbv=league_abbv)


def get_team_year_ats_home_underdog_core(team_id, season, league_abbv):
    return _get_team_ats(team_id=team_id,
                         season=season,
                         ats_type='atsHomeUnderdog',
                         league_abbv=league_abbv)

# todo need to look at this new api i just found
#  http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/0/teams/30/odds-records?lang=en&region=us
