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
                athlete_data = {'id': athlete_response['data']['id'],
                                'name': athlete_data['data']['full_name']}
                all_players.append(athlete_data)

    return all_players


def get_player_stat_urls(player_id):
    """ this function gets all the espn urls for a given player id

    example:
    {
  "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/278/statisticslog?lang=en&region=us",
  "entries": [
    {
      "season": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2005?lang=en&region=us"
      },
      "statistics": [
        {
          "type": "total",
          "statistics": {
            "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2005/types/2/athletes/278/statistics/0?lang=en&region=us"
          }
        },
        {
          "type": "team",
          "team": {
            "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2005/teams/30?lang=en&region=us"
          },
          "statistics": {
            "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2005/types/2/teams/30/athletes/278/statistics?lang=en&region=us"
          }
        }
      ]
    }
    ]
    }

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
        for stat in log_response.data['entries']:
            stat_urls.append(stat['statistics'][0]['statistics']['$ref'])

    return stat_urls

def extract_stats_from_url(url):
    response = requests.get(url)
    url_parts = url.split('/')
    year = url_parts[url_parts.index('seasons') + 1]
    player_id = url_parts[url_parts.index('athletes') + 1]
    stats = response.data['splits']['categories']

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
