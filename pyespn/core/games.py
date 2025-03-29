from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes import Event


def get_game_info_core(event_id, league_abbv, espn_instnace):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/events/{event_id}?lang=en&region=us'
    content = fetch_espn_data(url)
    current_event = Event(event_json=content,
                          espn_instance=espn_instnace)
    return content, current_event


def get_events_by_team(team_id, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/teams/{team_id}/events?lang=en&region=us'
    content = fetch_espn_data(url)
