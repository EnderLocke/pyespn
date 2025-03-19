from pyespn import PYESPN
player_id = 278 # Jimmy Smith, Goat
season = 2021
pick = 8
pick_round = 2


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    espn = PYESPN('nba')
    data = espn.get_draft_pick_data(pick_round=pick_round,
                                    pick=pick,
                                    season=season)
    awards = espn.get_awards(season=season)
    print(espn.BETTING_PROVIDERS)
    #colors = espn.get_team_colors(team_id=30)
    print(data)
    pass
