from pyespn.utilities import lookup_league_api_info, fetch_espn_data
from pyespn.data.version import espn_api_version as v
from pyespn.classes.draft import DraftPick


def get_draft_pick_data_core(pick_round, pick, season, league_abbv):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds/{pick_round}/picks/{pick}'
    content = fetch_espn_data(url)

    return content


def load_draft_data_core(season, league_abbv, espn_instance):
    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/draft/rounds?lang=en&region=us'
    content = fetch_espn_data(url)
    draft = []
    for draft_round in content.get('items', []):
        for pick in draft_round.get('picks', []):
            draft.append(DraftPick(espn_instance=espn_instance,
                                   pick_json=pick))

    return draft

