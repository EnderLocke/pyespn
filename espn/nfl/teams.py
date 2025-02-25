# todo a func for getting team stats by year//
#  build out a lookup table for a team name its not many lines
import requests


def get_season_team_stats(season, team):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/2/teams/{team}/statistics?lang=en&region=us'
    response = requests.get(url)
    return response.content


def get_team_info(team_id):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/{team_id}?lang=en&region=us'
    response = requests.get(url)
    return response
