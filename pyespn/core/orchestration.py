from pyespn.core import extract_stats_from_url_core, get_player_stat_urls_core


def get_players_historical_stats_core(player_id, league_abbv):
    historical_player_stats = []
    urls = get_player_stat_urls_core(player_id=player_id,
                                     league_abbv=league_abbv)
    for url in urls:
        historical_player_stats.append(extract_stats_from_url_core(url))

    return historical_player_stats
