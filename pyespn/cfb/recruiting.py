from pyespn.core import get_recruiting_rankings_core


def get_recruiting_rankings(season, max_pages=None):
    return get_recruiting_rankings_core(season=season,
                                        league_abbv='cfb',
                                        max_pages=max_pages)
