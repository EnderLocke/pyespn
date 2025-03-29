from pyespn.data.leagues import LEAGUE_API_MAPPING
from pyespn.exceptions import API400Error, NoDataReturnedError
import requests


def lookup_league_api_info(league_abbv):
    info = next(league for league in LEAGUE_API_MAPPING if league['league_abbv'] == league_abbv)
    return info


def check_response_code(content):
    if content.get('error'):
        error_code = content.get('error').get('code')
        if str(error_code)[0] == '4':
            raise API400Error(error_code=error_code,
                              error_message=content.get('error').get('message'))


def fetch_espn_data(url):
    """
    Fetches data from the ESPN API and checks for errors.

    Args:
        url (str): The API endpoint URL.

    Returns:
        dict: Parsed JSON response if successful, otherwise None.

    Raises:
        Exception: If an error occurs in the response.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

        content = response.json()  # Automatically parses JSON

        check_response_code(content)

        items_count = content.get('items', '').__len__
        content_count = content.__len__
        if items_count == 0 and content_count != 5:
            raise NoDataReturnedError(code=content.get('status', {}).get('code'))

        return content
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as ve:
        print(f"Data error: {ve}")

    return None  # Return None if there is an error

