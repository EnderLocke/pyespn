from pyespn.nfl import extract_stats_from_url, get_player_stat_urls


def get_nfl_players_historical_stats(player_id):
    historical_player_stats = []
    urls = get_player_stat_urls(player_id=player_id)
    for url in urls:
        historical_player_stats.append(extract_stats_from_url(url))

    return historical_player_stats
