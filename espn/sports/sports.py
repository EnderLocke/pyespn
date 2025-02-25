import requests

def get_all_base_apis():
    url = 'http://sports.core.api.espn.com/v2/sports/'
    response = requests.get(url)
    return response.content


# todo add way to get all leagues from given sporst
#  http://sports.core.api.espn.com/v2/sports/soccer/leagues
#
