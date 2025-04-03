# todo there is venue info could add a lookup for that specirfcally
#  what else is out there/ add a teams logo call (its within team info data)
from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Team, Manufacturer
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


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


def get_manufacturers_core(season, espn_instance, league_abbv) -> list[Manufacturer]:
    """
    Fetches a list of manufacturers for a specific season and league from the ESPN API.

    This function first retrieves the base API URL for the specified league and season,
    then iterates over multiple pages of manufacturer data, collecting the relevant
    manufacturer URLs. It then fetches detailed data for each manufacturer concurrently
    using a ThreadPoolExecutor, and returns a list of Manufacturer objects.

    Args:
        season (str): The season for which manufacturers data is to be fetched.
        espn_instance (object): An instance of the ESPN API handler used for making requests.
        league_abbv (str): The abbreviation of the league (e.g., 'f1', 'nascar').

    Returns:
        list: A list of Manufacturer objects, each representing a manufacturer with
              detailed data fetched from the ESPN API.

    Raises:
        Exception: If there is an error fetching manufacturer data or processing it.

    Example:
        >>> manufacturers = get_manufacturers_core(season="2025", espn_instance=espn_instance, league_abbv="f1")
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/manufacturers'
    page_content = fetch_espn_data(url)
    page_count = page_content.get('pageCount', 1)

    manufacturers = []
    manufacturer_urls = []

    for page in range(1, page_count + 1):
        page_url = f'{url}?page={page}'
        page_content = fetch_espn_data(page_url)
        for manufacturer in page_content.get('items', []):
            manufacturer_urls.append(manufacturer.get('$ref'))

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust workers as needed
        future_to_url = {executor.submit(fetch_espn_data, url): url for url in manufacturer_urls}

        for future in tqdm(as_completed(future_to_url), total=len(manufacturer_urls), desc="Fetching manufacturers"):
            try:
                athlete_content = future.result()
                manufacturers.append(Manufacturer(manufacturer_json=athlete_content, espn_instance=espn_instance))
            except Exception as e:
                print(f"Failed to fetch athlete data: {e}")

    return manufacturers
