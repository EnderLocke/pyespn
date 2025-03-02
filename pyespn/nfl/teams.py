# todo there is venue info could add a lookup for that specirfcally
#  what else is out there/ add a teams logo call (its within team info data)
#  build out a lookup table for a team name its not many lines
from pyespn.core import get_team_info_core, get_season_team_stats_core


def get_season_team_stats(season, team):
    return get_season_team_stats_core(season=season,
                                      team=team,
                                      league_abbv='nfl')


def get_team_info(team_id):
    return get_team_info_core(team_id=team_id,
                              league_abbv='nfl')
