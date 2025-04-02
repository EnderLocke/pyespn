from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Event


def get_game_info_core(event_id, league_abbv, espn_instnace) -> Event:
    """
    Retrieves detailed information for a specific game event.

    Args:
        event_id (int): The unique identifier for the game event.
        league_abbv (str): The abbreviation of the league.
        espn_instnace (object): An instance of the ESPN API handler.

    Returns:
        Event: An Event object containing details about the game.
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/events/{event_id}?lang=en&region=us'
    content = fetch_espn_data(url)
    current_event = Event(event_json=content,
                          espn_instance=espn_instnace)
    return current_event


# todo i think this doesn't work
def get_events_by_team(team_id, season, league_abbv) -> list[Event]:
    """
    Retrieves a list of all events (games) for a given team in a specific season.

    Args:
        team_id (int): The unique identifier of the team.
        season (int): The season year.
        league_abbv (str): The abbreviation of the league.

    Returns:
        dict: A dictionary containing event details for the team's games.
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/teams/{team_id}/events?lang=en&region=us'
    content = fetch_espn_data(url)
    return content
