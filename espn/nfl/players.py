import requests


def get_nfl_player_ids():
    all_players = []
    nfl_ath_url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?lang=en&region=us'
    response = requests.get(nfl_ath_url)
    num_pages = response['data']['entries']

    for i in range(1, num_pages):
        page_url = nfl_ath_url + f'&page={i}'
        page_response = requests.get(page_url)
        for athlete in page_response:
            if athlete['$ref']:
                athlete_response = requests.get(athlete['$ref'])
                athlete_data = {'id': athlete_response.data.id,
                                'name': athlete_data.data.full_name}
                all_players.append(athlete_data)

    return all_players


def get_player_stats(player_id):
    stat_log_url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{player_id}/statisticslog?lang=en&region=us'
    log_response = requests.get(stat_log_url)


