from pyespn.core import get_game_info_core


def get_game_info(event_id):
    return get_game_info_core(event_id=event_id,
                              league_abbv='cfb')
