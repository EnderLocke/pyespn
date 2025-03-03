from pyespn.data.leagues import LEAGUE_API_MAPPING


def lookup_league_api_info(league_abbv):
    info = next(league for league in LEAGUE_API_MAPPING if league['league_abbv'] == league_abbv)
    return info
