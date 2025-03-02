from pyespn.core import get_player_info_core
import requests
import json


def get_mcbb_player_ids():
    all_players = []
    mcbb_ath_url = 'http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/athletes?lang=en&region=us'
    response = requests.get(mcbb_ath_url)
    num_pages = json.loads(response.content.decode('utf-8')).get('pageCount')

    for i in range(1, num_pages + 1):
        page_url = mcbb_ath_url + f'&page={i}'
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


def get_player_info(player_id):
    return get_player_info_core(player_id=player_id,
                                league_abbv='mcbb')
