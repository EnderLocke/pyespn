from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.draft import DraftPick


def get_draft_pick_data_core(pick_round, pick, season, league_abbv) -> dict:
    """
    Retrieves data for a specific draft pick in a given season and league.

    Args:
        pick_round (int): The round of the draft.
        pick (int): The specific pick number in the round.
        season (int): The season year of the draft.
        league_abbv (str): The league abbreviation.

    Returns:
        dict: The draft pick data.
    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds/{pick_round}/picks/{pick}'
    content = fetch_espn_data(url)

    return content


def load_draft_data_core(season, league_abbv, espn_instance) -> list[DraftPick]:
    """
    Loads all draft data for a given season and league.

    Args:
        season (int): The season year of the draft.
        league_abbv (str): The league abbreviation.
        espn_instance (object): The ESPN instance for processing draft data.

    Returns:
        list: A list of DraftPick objects containing draft pick details.
    """
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds?lang=en&region=us'
    content = fetch_espn_data(url)
    draft = []
    for draft_round in content.get('items', []):
        for pick in draft_round.get('picks', []):
            draft.append(DraftPick(espn_instance=espn_instance,
                                   pick_json=pick))

    return draft
