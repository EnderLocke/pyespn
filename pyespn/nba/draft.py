from pyespn.core import get_draft_pick_data_core


def get_draft_pick_data(pick_round, pick, season):
    return get_draft_pick_data_core(pick_round=pick_round,
                                    pick=pick,
                                    season=season,
                                    league_abbv='nba')
