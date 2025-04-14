from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.classes.schedule import Schedule
from pyespn.data.version import espn_api_version as v
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyespn.classes import Schedule


# todo 1 is preseason 2 is regular season and 3 is postseason
def get_regular_season_schedule_core(league_abbv, espn_instance,
                                     season, load_odds: bool = False,
                                     load_pbp: bool = False,
                                     season_type='2') -> "Schedule":
    """
    Retrieves the regular season schedule for a specific season and league, including all weeks.

    Args:
        league_abbv (str): Abbreviation of the league (e.g., 'nfl', 'cfb').
        espn_instance (PyESPN): An instance of the ESPN API wrapper used to fetch and parse data.
        season (int): The year of the season (e.g., 2023).
        load_odds (bool, optional): Whether to include betting odds in the schedule. Defaults to False.
        load_pbp (bool, optional): Whether to load play-by-play data for each event. Defaults to False.
        season_type (str, optional): Season type as defined by ESPN:
            - '1' = preseason
            - '2' = regular season (default)
            - '3' = postseason

    Returns:
        Schedule: A `Schedule` object containing the schedule for the specified season and league.
                        This includes the list of weeks and events for that season.

    Notes:
        - The function fetches data from ESPN's internal API using core URLs and pagination.
        - The resulting `Schedule` object will have all available week URLs converted into
          full event data structures upon initialization.

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
                        espn_instance=espn_instance,
                        load_odds=load_odds,
                        load_plays=load_pbp)

    return schedule
