from pyespn import PYESPN


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    espn = PYESPN('nascar')
    data = espn.get_standings(season=2024, standings_type='driver')
    print(data)
    pass
