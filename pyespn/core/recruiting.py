from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.player import Recruit
import concurrent.futures
import requests
import json


def get_recruiting_rankings_core(season, league_abbv, espn_instance, max_pages=None):
    """
    NOTE-> stars not available to get this you need to wait for players page to load and wait for
        the rating-#_stars.png file so i could get the #  of stars

    :param season:
    :param league_abbv:
    :param max_pages:
    :return:
    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'https://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/recruiting/{season}/athletes'
    content = fetch_espn_data(url)

    num_of_pages = content['pageCount'] if not max_pages else max_pages

    recruiting_data = []

    def fetch_and_process_page(page):
        """Fetches a page and processes recruits."""
        paged_url = f"{url}?page={page}"
        response = fetch_espn_data(paged_url)
        return [Recruit(recruit_json=recruit, espn_instance=espn_instance) for recruit in response.get('items', [])]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_page = {executor.submit(fetch_and_process_page, page): page for page in range(1, num_of_pages + 1)}

        for future in concurrent.futures.as_completed(future_to_page):
            recruiting_data.extend(future.result())

    return recruiting_data
