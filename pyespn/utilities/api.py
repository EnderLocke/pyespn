from pyespn.data.leagues import LEAGUE_API_MAPPING
from pyespn.exceptions import API400Error


def lookup_league_api_info(league_abbv):
    info = next(league for league in LEAGUE_API_MAPPING if league['league_abbv'] == league_abbv)
    return info


def check_response_code(content):
    if content.get('error'):
        error_code = content.get('error').get('code')
        if str(error_code)[0] == '4':
            raise API400Error(error_code=error_code,
                              error_message=content.get('error').get('message'))
