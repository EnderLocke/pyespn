from pyespn.utilities import lookup_league_api_info, fetch_espn_data, get_an_id, get_athlete_id
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Player, Stat
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import requests
import json
import warnings


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

    stat_log_url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/athletes/{player_id}/statisticslog?lang=en&region=us'
    content_dict = fetch_espn_data(stat_log_url)
    for stat in content_dict.get('entries'):
        stat_urls.append(stat['statistics'][0]['statistics']['$ref'])

    return stat_urls


def extract_stats_from_url_core(url, espn_instance) -> dict:
    """
    Extracts player statistics from a given URL.

    Args:
        url (str): The URL pointing to the player's statistics.

    Returns:
        dict: A dict with list of stat objects with statistics.
    """

    all_stats = []
    year = get_an_id(url=url, slug='seasons')
    player_id = get_athlete_id(url=url)
    content_dict = fetch_espn_data(url)
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
                'name': stat.get('name'),
                'description': stat.get('description')
            }
            all_stats.append(Stat(stat_json=this_stat,
                                  espn_isntance=espn_instance))

    return {year: all_stats}


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


def load_athletes_core(season, league_abbv, espn_instance, verbose=True) -> list["Player"]:
    """
    Loads athlete data for a given season and league abbreviation from the ESPN API.

    This function retrieves a list of athletes from the specified league and season,
    utilizing multi-threading to improve efficiency when fetching individual athlete data.

    Args:
        season (int): The season year for which athlete data is being retrieved.
        league_abbv (str): The abbreviation of the league (e.g., 'nfl', 'nba', 'mlb').
        espn_instance: An instance of the ESPN API client.
        verbose (bool, optional): If True, prints progress updates and warnings. Defaults to True.

    Returns:
        list[Player]: A list of `Player` objects containing athlete data.

    Raises:
        Exception: Logs and prints any errors encountered during data retrieval.

    Notes:
        - The function first retrieves a list of athlete URLs.
        - It then uses `ThreadPoolExecutor` to fetch athlete details in parallel.
        - Uses up to 10 worker threads for concurrent requests.
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/athletes'
    page_content = fetch_espn_data(url)
    page_count = page_content.get('pageCount', 1)
    record_count = page_content.get('count', 0)

    if verbose and record_count > 2500:
        warnings.warn(
            f"⚠️ Large dataset detected ({record_count} athletes). This may take some time.",
            UserWarning
        )

    athletes = []
    athlete_urls = []

    for page in range(1, page_count + 1):
        page_url = f'{url}?page={page}'
        page_content = fetch_espn_data(page_url)
        for athlete in page_content.get('items', []):
            athlete_urls.append(athlete.get('$ref'))

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust workers as needed
        future_to_url = {executor.submit(fetch_espn_data, url): url for url in athlete_urls}

        for future in tqdm(as_completed(future_to_url), total=len(athlete_urls), disable=not verbose, desc="Fetching athletes"):
            try:
                athlete_content = future.result()
                athletes.append(Player(player_json=athlete_content, espn_instance=espn_instance))
            except Exception as e:
                print(f"Failed to fetch athlete data: {e}")

    return athletes
