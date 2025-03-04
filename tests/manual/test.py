from pyespn import PYESPN


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    espn = PYESPN('nba')
    data = espn.get_awards(season=2023)
    print(data)
    pass
