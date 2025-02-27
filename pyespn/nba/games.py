from pyespn.events import get_event_info


def get_game_info(event_id):
    data = get_event_info(sport='basketball',
                          league='nba',
                          event_id=event_id)
    return data
