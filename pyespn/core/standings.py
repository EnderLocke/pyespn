# http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2025/types/2/standings?lang=en&region=us
# todo golf standings are different
from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.standings import Standings


def get_standings_core(season, league_abbv, espn_instance):
    """
    Fetches and returns the standings for a given season and league.

    This function retrieves standings data from ESPN's API for the specified season and league.
    It iterates through multiple pages if necessary to collect all standings.

    Args:
        season (int): The season year for which standings are to be retrieved.
        league_abbv (str): The abbreviation of the league (e.g., "f1" for Formula 1).
        espn_instance (object): An instance of the ESPN API client.

    Returns:
        list: A list of Standings objects containing the standings data.

    Raises:
        Exception: If fetching data from the API fails.

    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/standings'
    content = fetch_espn_data(url)
    page_count = content.get('pageCount')

    standings = []
    standings_url = []
    for page in range(1, page_count + 1):
        paged_url = url + f'?page={page}'
        paged_content = fetch_espn_data(paged_url)

        for item in paged_content.get('items', []):
            standings_url.append(item.get('$ref'))

    for standing in standings_url:
        standing_content = fetch_espn_data(standing)
        standings.append(Standings(standings_json=standing_content,
                                   espn_instance=espn_instance))

    return standings
