from pyespn.utilities import get_type_futures, get_team_id
from pyespn.cfb.data import cfb_teams_data, CONFERENCE_MAP
import requests
import json


def _get_futures_year(year):
    url = f'http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/futures?lang=en&region=us'
    response = requests.get(url)
    content = json.loads(response.content)
    return content


def get_year_cfb_champions_futures(season, provider="DraftKings"):
    content = _get_futures_year(season)

    cfb_futures = get_type_futures(data=content,
                                   futures_type='NCAA(F) - Championship')

    provider_futures = next(future for future in cfb_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in cfb_teams_data if team['team_id'] == team_id)

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value'],
            'team_ref': item['team']['$ref'],
            'team_id': team_id
        }
        futures_list.append(item_dict)

    return futures_list


def get_year_conference_champ_futures(season, conference, provider="DraftKings"):
    """

    :param season:
    :param conference:
    :param provider:
    :return:
    """
    content = _get_futures_year(season)

    cfb_futures = get_type_futures(data=content,
                                   futures_type=CONFERENCE_MAP[conference])

    provider_futures = next(future for future in cfb_futures['futures'] if future['provider']['name'] == provider)

    futures_list = []
    for item in provider_futures['books']:
        team_id = get_team_id(item['team']['$ref'])
        result = next(team for team in cfb_teams_data if int(team['team_id']) == int(team_id))

        item_dict = {
            'team_name': result['team_name'],
            'team_city': result['team_city'],
            'champion_future': item['value'],
            'team_ref': item['team']['$ref'],
            'team_id': team_id
        }
        futures_list.append(item_dict)

    return futures_list
