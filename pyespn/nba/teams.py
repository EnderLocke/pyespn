# todo add team info api

# http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2025/teams/1?lang=en&region=us

import requests
import json


def get_season_team_stats(season, team):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_team_info(team_id):
    url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/teams/{team_id}?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


