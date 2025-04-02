# todo there is venue info could add a lookup for that specirfcally
#  what else is out there/ add a teams logo call (its within team info data)
from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Team
import requests
import json


def get_season_team_stats_core(season, team, league_abbv) -> dict:
    """
    Fetches the team statistics for a specific season and team in a given league.

    Args:
        season (int): The season year (e.g., 2023).
        team (int): The team ID
        league_abbv (str): The abbreviation for the league (e.g., 'nfl', 'nba').

    Returns:
        dict: A dictionary containing the team's statistics for the specified season.

    Example:
        >>> stats = get_season_team_stats_core(2023, 30, 'nfl')
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    content = fetch_espn_data(url)

    return content


def get_team_info_core(team_id, league_abbv, espn_instance) -> Team:
    """
    Fetches detailed information about a team, including name, logo, and other team data.

    Args:
        team_id (int): The unique identifier
        league_abbv (str): The abbreviation for the league (e.g., 'nfl', 'nba').
        espn_instance (object): An instance of the ESPN class used for interaction with the API.

    Returns:
        Team: An instance of the `Team` class containing the team data.

    Example:
        >>> team_info, team = get_team_info_core(30, 'nfl', espn_instance)
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/teams/{team_id}?lang=en&region=us'
    content = fetch_espn_data(url)

    current_team = Team(espn_instance=espn_instance, team_json=content)
    return current_team
