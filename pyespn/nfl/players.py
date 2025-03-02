from pyespn.core import get_player_info_core, get_player_ids_core


def get_nfl_player_ids():
    return get_player_ids_core(league_abbv='nfl')


def get_player_info(player_id):
    return get_player_info_core(player_id=player_id,
                                league_abbv='nfl')
