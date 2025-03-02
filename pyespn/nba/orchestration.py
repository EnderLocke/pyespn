from pyespn.core import get_players_historical_stats_core


def get_nba_players_historical_stats(player_id):
    return get_players_historical_stats_core(player_id=player_id,
                                             league_abbv='nba')
