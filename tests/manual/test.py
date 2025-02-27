from pyespn.nfl import get_nfl_players_historical_stats, get_nfl_player_ids


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    data = get_nfl_player_ids()
    print(data)
    pass
