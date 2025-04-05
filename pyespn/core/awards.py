from pyespn.utilities import lookup_league_api_info, get_athlete_id, fetch_espn_data
from pyespn.core.players import get_player_info_core
from pyespn.data.version import espn_api_version as v
import requests
import json


def get_awards_core(season, league_abbv) -> dict:
    """
    Retrieves award winners for a given season and league.

    This function fetches award data from the ESPN API, retrieves information
    about each award and its winners, and compiles a structured list of award details.

    Args:
        season (int or str): The season year for which to retrieve awards.
        league_abbv (str): The abbreviation of the league (e.g., "NFL", "NBA").

    Returns:
        list[dict]: A list of dictionaries containing award details. Each dictionary includes:
            - athlete_id (int): The ID of the athlete who won the award.
            - award (str): The name of the award.
            - award_description (str or None): A description of the award, if available.
            - winner (str): The full name of the athlete.
            - position (str): The athlete’s position abbreviation.

    Raises:
        KeyError: If expected keys are missing from the API response.

    Example:
        >>> get_awards_core(2024, "NFL")
        [
            {
                'athlete_id': 12345,
                'award': 'MVP',
                'award_description': 'Most Valuable Player',
                'winner': 'Patrick Mahomes',
                'position': 'QB'
            },
            {
                'athlete_id': 67890,
                'award': 'Defensive Player of the Year',
                'award_description': 'Best defensive player of the season',
                'winner': 'Aaron Donald',
                'position': 'DT'
            }
        ]
    """

    api_info = lookup_league_api_info(league_abbv=league_abbv)
    url = f'http://sports.core.api.espn.com/{v}/sports/{api_info["sport"]}/leagues/{api_info["league"]}/seasons/{season}/awards?lang=en&region=us'
    content = fetch_espn_data(url)

    awards_urls = content['items']
    awards = []
    for award_url in awards_urls:
        award_response = requests.get(award_url['$ref'])
        award_content = json.loads(award_response.content)
        for winner in award_content['winners']:
            athlete_id = get_athlete_id(winner['athlete']['$ref'])
            athlete_info = get_player_info_core(player_id=athlete_id,
                                                league_abbv=league_abbv)
            this_award = {
                'athlete_id': athlete_id,
                'award': award_content['name'],
                'award_description': award_content.get('description'),
                'winner': athlete_info['fullName'],
                'position': athlete_info['position']['abbreviation']

            }

            awards.append(this_award)

    return awards
