from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Player
import requests
import json


def get_player_ids_core(league_abbv: str) -> list:
    """
    Retrieves a list of player IDs and names for a given league.

    Args:
        league_abbv (str): The abbreviation of the league (e.g., "nfl", "nba").

    Returns:
        list: A list of dictionaries containing player IDs and names.
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    all_players = []
    cfb_ath_url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/athletes?lang=en&region=us'
    content = fetch_espn_data(cfb_ath_url)

    num_pages = content.get('pageCount')

    for i in range(1, num_pages + 1):
        page_url = cfb_ath_url + f'&page={i}'
        page_response = requests.get(page_url)
        content = json.loads(page_response.content)

        for athlete in content:
            if athlete['$ref']:
                athlete_response = requests.get(athlete['$ref'])
                athlete_content = json.loads(athlete_response.content)
                athlete_data = {'id': athlete_content['id'],
                                'name': athlete_content['full_name']}
                all_players.append(athlete_data)

    return all_players


def get_player_stat_urls_core(player_id, league_abbv) -> list:
    """
    Retrieves all the ESPN URLs for a given player ID.

    Args:
        player_id (str): The unique identifier of the player.
        league_abbv (str): The abbreviation of the league.

    Returns:
        list: A list of URLs pointing to the player's statistics.
    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    stat_urls = []
    try:
        stat_log_url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/athletes/{player_id}/statisticslog?lang=en&region=us'
        log_response = requests.get(stat_log_url)
    except Exception as e:
        raise Exception(e)
    finally:
        content_str = log_response.content.decode('utf-8')
        content_dict = json.loads(content_str)
        for stat in content_dict.get('entries'):
            stat_urls.append(stat['statistics'][0]['statistics']['$ref'])

    return stat_urls


def extract_stats_from_url_core(url) -> list:
    """
    Extracts player statistics from a given URL.

    Args:
        url (str): The URL pointing to the player's statistics.

    Returns:
        list: A list of dictionaries containing the player's statistics.
    """

    response = requests.get(url)
    url_parts = url.split('/')
    all_stats = []
    year = url_parts[url_parts.index('seasons') + 1]
    player_id = url_parts[url_parts.index('athletes') + 1]
    content_str = response.content.decode('utf-8')
    content_dict = json.loads(content_str)
    stats = content_dict.get('splits').get('categories')

    for category in stats:
        category_name = category['name']
        for stat in category['stats']:
            this_stat = {
                'category': category_name,
                'season': year,
                'player_id': player_id,
                'stat_value': stat.get('value'),
                'stat_type_abbreviation': stat.get('abbreviation'),
                'league': 'nfl'
            }
            all_stats.append(this_stat)

    return all_stats


def get_player_info_core(player_id, league_abbv, espn_instance) -> Player:
    """
    Retrieves detailed player information for a given player ID from the ESPN API.

    Args:
        player_id (str): The unique identifier of the player whose information is being retrieved.
        league_abbv (str): The abbreviation of the league the player is part of (e.g., 'nfl', 'nba').
        espn_instance (object): An instance of the ESPN class used to manage and interact with ESPN data.

    Returns:
        Player: A Player object containing the detailed information of the player retrieved from the API.
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/athletes/{player_id}'
    response = requests.get(url)
    content = json.loads(response.content)
    current_player = Player(player_json=content,
                            espn_instance=espn_instance)
    return current_player
