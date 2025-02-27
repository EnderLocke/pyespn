# todo load up betting api calls here
# http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/0/teams/30/odds-records?lang=en&region=us
import requests
import json


def _get_type_ats(data, ats_type):
    try:
        result = next(item for item in data["items"] if item["type"]["name"] == ats_type)
    except StopIteration:
        result = None
    return result


def _get_team_year_ats(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


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


def get_team_year_ml(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/0/teams/{team_id}/odds-records?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
