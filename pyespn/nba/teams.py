from pyespn.core import get_team_info_core, get_season_team_stats_core


def get_season_team_stats(season, team):
    return get_season_team_stats_core(season=season,
                                      team=team,
                                      league_abbv='nba')


def get_team_info(team_id):
    return get_team_info_core(team_id=team_id,
                              league_abbv='nba')


