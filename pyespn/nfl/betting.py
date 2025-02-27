# todo load up betting api calls here

# http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/2/teams/30/ats?lang=en&region=us
# http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/0/teams/30/odds-records?lang=en&region=us
import requests
import json


def get_team_year_ats(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/2/teams/{team_id}/ats?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_year_ml(team_id, season):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/0/teams/{team_id}/odds-records?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
