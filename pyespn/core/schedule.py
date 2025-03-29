from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.classes import Schedule
from pyespn.data.version import espn_api_version as v


def get_weekly_schedule_core(league_abbv, espn_instance, season, week):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/weeks/{week}/events?lang=en&region=us'
    content = fetch_espn_data(url)
    weekly_schedule = Schedule(schedule_json=content,
                               espn_instance=espn_instance)
    return weekly_schedule
