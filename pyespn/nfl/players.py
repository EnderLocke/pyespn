import requests
import json


def get_nfl_player_ids():
    all_players = []
    nfl_ath_url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?lang=en&region=us'
    response = requests.get(nfl_ath_url)
    num_pages = json.loads(response.content.decode('utf-8')).get('pageCount')

    for i in range(1, num_pages):
        page_url = nfl_ath_url + f'&page={i}'
        page_response = requests.get(page_url)
        for athlete in page_response:
            if athlete['$ref']:
                athlete_response = requests.get(athlete['$ref'])
                athlete_data = {'id': athlete_response['data']['id'],
                                'name': athlete_data['data']['full_name']}
                all_players.append(athlete_data)

    return all_players


def get_player_stat_urls(player_id):
    """ this function gets all the espn urls for a given player id

    :param player_id:
    :return:
    """
    stat_urls = []
    try:
        stat_log_url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{player_id}/statisticslog?lang=en&region=us'
        log_response = requests.get(stat_log_url)
    except Exception as e:
        raise Exception(e)
    finally:
        content_str = log_response.content.decode('utf-8')
        content_dict = json.loads(content_str)
        for stat in content_dict.get('entries'):
            stat_urls.append(stat['statistics'][0]['statistics']['$ref'])

    return stat_urls


def extract_stats_from_url(url):
    response = requests.get(url)
    url_parts = url.split('/')
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
                'stat_value': stat['value'],
                'stat_type_abbreviation': stat['abbreviation'],
                'league': 'nfl'
            }

    return this_stat


def get_player_info(player_id):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{player_id}'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
