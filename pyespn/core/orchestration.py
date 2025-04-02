from pyespn.core import extract_stats_from_url_core, get_player_stat_urls_core


def get_players_historical_stats_core(player_id, league_abbv) -> list:
    """
    Retrieves the historical statistics of a player.

    Args:
        player_id (str): The unique identifier of the player.
        league_abbv (str): The abbreviation of the league.

    Returns:
        list: A list of historical player statistics extracted from various URLs.
    """
    historical_player_stats = []
    urls = get_player_stat_urls_core(player_id=player_id,
                                     league_abbv=league_abbv)
    for url in urls:
        historical_player_stats.append(extract_stats_from_url_core(url))

    return historical_player_stats
