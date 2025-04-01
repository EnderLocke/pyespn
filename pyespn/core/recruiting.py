from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.player import Recruit
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

    if not max_pages:
        num_of_pages = content['pageCount']
    else:
        num_of_pages = max_pages

    recruiting_data = []
    rank = 1
    for page in range(1, num_of_pages + 1):
        paged_url = url + f'?page={page}'
        paged_response = requests.get(paged_url)
        paged_content = json.loads(paged_response.content)
        for recruit in paged_content['items']:
            this_recruit = Recruit(recruit_json=recruit,
                                   espn_instance=espn_instance)
            rank += 1
            recruiting_data.append(this_recruit)

    return recruiting_data
