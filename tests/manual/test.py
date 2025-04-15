from pyespn import PYESPN
player_id = 278 # Jimmy Smith, Goat
season = 2025
pick = 8
pick_round = 2


if __name__ == '__main__':

    espn = PYESPN('mlb')
    espn.load_season_rosters(season=season)
    espn.load_season_schedule(season=season, load_only_current_week=True)  #, load_game_odds=True)

    espn.league.load_regular_season_schedule(season=season, load_game_odds=True)
    #espn.load_season_rosters(season=season)
    #espn.teams[0].load_season_roster_box_score(season=season)
    #espn.load_season_teams_results(season=2024)
    #espn.load_standings(season=season)
    #espn.load_season_league_stat_leaders(season=2024)
    #espn.load_season_team_stats(season=2024)
    #stats = espn.get_players_historical_stats(player_id=player_id)
    #espn.load_athletes(season=season)
    #espn.load_regular_season_schedule(season=season)
    #awards = espn.get_awards(season=season)
    #colors = espn.get_team_colors(team_id=30)
    pass
