from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.classes.schedule import Schedule
from pyespn.data.version import espn_api_version as v
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyespn.classes import Schedule


# todo 1 is preseason 2 is regular season and 3 is postseason
def get_regular_season_schedule_core(league_abbv, espn_instance, season, season_type='2') -> "Schedule":
    """
    Retrieves the regular season schedule for a specific season and league, including all weeks.

    Args:
        league_abbv (str): The abbreviation for the league (e.g., 'nfl', 'nba').
        espn_instance (object): An instance of the ESPN class used for interaction with the ESPN API.
        season (int): The season year for which the schedule is to be fetched (e.g., 2023).
        season_type (str, optional): The type of season to fetch. Default is '2' for the regular season.
                                     '1' corresponds to the preseason, and '3' corresponds to the postseason.

    Returns:
        Schedule: A `Schedule` object containing the schedule for the specified season and league.
                        This includes the list of weeks and events for that season.

    Note:
        This function works primarily for NFL and college football leagues. It retrieves the weeks' data from the ESPN API
        and processes it into a `Schedule` object. The function handles pagination, fetching all available pages of schedule data.

    Example:
        >>> schedule = get_regular_season_schedule_core('nfl', espn_instance, 2023)
        >>> print(schedule)
    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/{season_type}/weeks'
    content = fetch_espn_data(url)

    pages = content.get('pageCount')
    weeks_urls = []
    for page in range(1, pages + 1):
        url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/types/2/weeks?page={page}'
        page_content = fetch_espn_data(url)
        for item in page_content.get('items', []):
            weeks_urls.append(item.get('$ref'))
    schedule = Schedule(schedule_list=weeks_urls,
                        espn_instance=espn_instance)

    return schedule
