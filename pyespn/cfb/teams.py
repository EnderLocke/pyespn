# todo these dont seem to work
import requests
import json


def get_season_team_stats(season, team):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_info(team_id):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/teams/{team_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content
