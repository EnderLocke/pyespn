from pyespn import PYESPN
player_id = 278 # Jimmy Smith, Goat
season = 2024
pick = 8
pick_round = 2


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    nfl_espn = PYESPN('nfl')
    #nba_espn = PYESPN('nba')
    nfl_espn.load_regular_season_schedule(season=season)
    #awards = espn.get_awards(season=season)
    #colors = espn.get_team_colors(team_id=30)
    pass
