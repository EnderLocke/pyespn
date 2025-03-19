from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v


def get_draft_pick_data_core(pick_round, pick, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds/{pick_round}/picks/{pick}'
    content = fetch_espn_data(url)

    return content

