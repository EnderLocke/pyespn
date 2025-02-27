# todo build out player stats by player id

# https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/athletes/${player_id}/statisticslog?lang=en&region=us

# todo build out player info call

# https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/athletes/${playerId}
import requests
import json


def get_cfb_player_ids():
    all_players = []
    nba_ath_url = 'http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/athletes?lang=en&region=us'
    response = requests.get(nba_ath_url)
    num_pages = json.loads(response.content.decode('utf-8')).get('pageCount')

    for i in range(1, num_pages):
        page_url = nba_ath_url + f'&page={i}'
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
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/athletes/{player_id}'
    response = requests.get(url)
    content = json.loads(response.content)
    return content

