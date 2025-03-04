# http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2025/types/2/standings?lang=en&region=us
from pyespn.utilities import lookup_league_api_info, get_athlete_id
from pyespn.data.standings import STANDINGS_TYPE_MAP
import requests
import json


def get_standings_core(season, standings_type, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/v2/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/0/standings/{STANDINGS_TYPE_MAP[league_abbv][standings_type]}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    standings = content['standings']
    all_records = []
    for record in standings:
        athlete_id = get_athlete_id(record['athlete']['$ref'])
        driver_stats = {'athlete_id': athlete_id}
        for stats in record['records'][0]['stats']:
            this_stat = {
                **stats
            }
            driver_stats.setdefault(stats['name'], this_stat)
        all_records.append(driver_stats)

    return all_records

