from pyespn.utilities import get_an_id


def get_players_historical_stats_core(player_id, league_abbv, espn_instance) -> dict:
    from pyespn.core.players import extract_stats_from_url_core, get_player_stat_urls_core
    """
    Retrieves the historical statistics of a player.

    Args:
        player_id (str): The unique identifier of the player.
        league_abbv (str): The abbreviation of the league.

    Returns:
        dict: A dict of historical player statistics extracted from various URLs.
    """
    historical_player_stats = {}
    urls = get_player_stat_urls_core(player_id=player_id,
                                     league_abbv=league_abbv)
    for url in urls:
        year = get_an_id(url=url, slug='seasons')

        historical_player_stats[year] = extract_stats_from_url_core(url=url,
                                                                    espn_instance=espn_instance)

    return historical_player_stats
