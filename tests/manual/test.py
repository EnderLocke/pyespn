#from pyespn.nba import get_year_nba_champ_futures
from pyespn.nfl import get_year_nfl_super_bowl_futures


if __name__ == '__main__':
    #data = get_nfl_players_historical_stats(278)
    data = get_year_nfl_super_bowl_futures(season=2023)
    print(data)
    pass
