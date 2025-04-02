from pyespn import PYESPN
player_id = 278 # Jimmy Smith, Goat
season = 2021
pick = 8
pick_round = 2


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    #nfl_espn = PYESPN('nfl')
    espn = PYESPN('nba')
    #cfb_espn = PYESPN('cfb')
    #cfb_espn.load_regular_season_schedule(season=season)
    ayo = espn.get_draft_pick_data(season=season,
                                   pick_round=pick_round,
                                   pick=pick)
    espn.load_year_draft(season=season)
    espn.load_regular_season_schedule(season=season)
    #awards = espn.get_awards(season=season)
    #colors = espn.get_team_colors(team_id=30)
    pass
