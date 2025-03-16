# http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2025/types/2/standings?lang=en&region=us
# todo golf standings are different
from pyespn.utilities import lookup_league_api_info, get_athlete_id
from pyespn.data.version import espn_api_version as v
from pyespn.data.standings import STANDINGS_TYPE_MAP
import requests
import json


def get_standings_core(season, standings_type, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/0/standings/{STANDINGS_TYPE_MAP[league_abbv].get(standings_type, 0)}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    standings = content['standings']
    all_records = []
    for record in standings:
        athlete_url = record['athlete']['$ref']
        athlete_response = requests.get(athlete_url)
        athlete_content = json.loads(athlete_response.content)
        driver_stats = {
            'athlete_id': athlete_content.get('id'),
            'name': athlete_content.get('fullName'),
            'country': athlete_content.get('flag', {'alt': 'Not Known'}).get('alt')
        }
        vehicles = []
        for vehicle in athlete_content.get('vehicles', []):
            vehicles.append({
                **vehicle
            })
        driver_stats['vehicles'] = vehicles
        for stats in record['records'][0]['stats']:
            this_stat = {
                **stats
            }
            driver_stats.setdefault(stats['name'], this_stat)
        all_records.append(driver_stats)

    return all_records

