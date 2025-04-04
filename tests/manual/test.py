from pyespn import PYESPN
player_id = 278 # Jimmy Smith, Goat
season = 2024
pick = 8
pick_round = 2


if __name__ == '__main__':

    espn = PYESPN('nfl')
    espn.load_season_teams_results(season=season)
    espn.load_season_rosters(season=2025)
    #stats = espn.get_players_historical_stats(player_id=player_id)
    #espn.load_athletes(season=season)
    #espn.load_regular_season_schedule(season=season)
    #awards = espn.get_awards(season=season)
    #colors = espn.get_team_colors(team_id=30)
    pass
