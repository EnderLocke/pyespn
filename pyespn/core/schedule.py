from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.classes import Schedule
from pyespn.data.version import espn_api_version as v


def get_weekly_schedule_core(league_abbv, espn_instance, season, week):
    api_info = lookup_league_api_info(league_abbv=league_abbv)

    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/weeks/{week}/events?lang=en&region=us'
    content = fetch_espn_data(url)

    for event_url in content.get('items', []):
        event_content = fetch_espn_data(event_url['$ref'])
        weekly_schedule = Schedule(schedule_json=event_content,
                                   espn_instance=espn_instance)
    return weekly_schedule


# todo 1 is preseason 2 is regular season and 3 is postseason
def get_regular_season_schedule_core(league_abbv, espn_instance, season):
    season_schedule = []
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/weeks'
    content = fetch_espn_data(url)

    pages = content.get('pageCount')
    weeks_urls = []
    for page in range(1, pages + 1):
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/weeks?page={page}'
        page_content = fetch_espn_data(url)
        for item in page_content.get('items', []):
            weeks_urls.append(item.get('$ref'))

    for week_url in weeks_urls:
        api_url = week_url.split('?')[0] + f'/events'
        week_content = fetch_espn_data(api_url)
        # todo here i need to capture the data
        week_pages = week_content.get('pageCount')

        for week_page in range(1, week_pages + 1):
            weekly_url = api_url + f'?page={week_page}'
            this_week_content = fetch_espn_data(weekly_url)
            event_list = []

            for event in this_week_content.get('items', []):
                event_content = fetch_espn_data(event.get('$ref'))
                event_list.append()
                pass
            pass
        pass

    return season_schedule
