from pyespn.data.leagues import LEAGUE_API_MAPPING
from pyespn.exceptions import API400Error, NoDataReturnedError
import requests


def lookup_league_api_info(league_abbv) -> dict:
    """
    Retrieves information about a league from the LEAGUE_API_MAPPING based on its abbreviation.

    Args:
        league_abbv (str): The abbreviation of the league (e.g., 'nfl', 'nba').

    Returns:
        dict: A dictionary containing the league's information.

    Raises:
        StopIteration: If no league with the provided abbreviation is found in the LEAGUE_API_MAPPING.
    """
    info = next(league for league in LEAGUE_API_MAPPING if league['league_abbv'] == league_abbv)
    return info


def check_response_code(content: dict):
    """
    Checks the response content for an error code and raises an API400Error
    if the error code starts with '4'.

    Args:
        content (dict): The response content from an API request.

    Raises:
        API400Error: If the response contains an error code in the 400 range.

    Example:
        >>> response = {"error": {"code": 404, "message": "Not Found"}}
        >>> check_response_code(response)  # Raises API400Error
    """
    if content.get('error'):
        error_code = content.get('error').get('code')
        if str(error_code)[0] == '4':
            raise API400Error(error_code=error_code,
                              error_message=content.get('error').get('message'))


def fetch_espn_data(url: str) -> dict:
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

