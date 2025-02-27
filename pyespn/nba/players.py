# todo add athlete stats and info
#  stats
# http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2025/athletes/4277905?lang=en&region=us

#  todo all players?
# http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/athletes/
import requests
import json

def get_nba_player_ids():
    all_players = []
    nba_ath_url = 'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/athletes?lang=en&region=us'
    response = requests.get(nba_ath_url)
    num_pages = json.loads(response.content.decode('utf-8')).get('pageCount')

    for i in range(1, num_pages):
        page_url = nba_ath_url + f'&page={i}'
        page_response = requests.get(page_url)
        for athlete in page_response:
            if athlete['$ref']:
                athlete_response = requests.get(athlete['$ref'])
                athlete_data = {'id': athlete_response['data']['id'],
                                'name': athlete_data['data']['full_name']}
                all_players.append(athlete_data)

    return all_players


def get_player_info(player_id):
    url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/athletes/{player_id}'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
