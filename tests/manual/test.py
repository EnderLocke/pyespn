from pyespn.nfl import get_nfl_players_historical_stats


if __name__ == '__main__':
    data = get_nfl_players_historical_stats(278)
    print(data)
    pass
