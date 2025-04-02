import os
import json


def open_json(file_path):
    """
    Opens and reads a JSON file, returning the 'teams' data.

    Args:
        file_path (str): The relative path to the JSON file.

    Returns:
        list: The list of teams extracted from the JSON file.

    Example:
        >>> teams = open_json("data/teams.json")
        >>> print(teams)  # [{'team_id': 1, 'name': 'Team A'}, ...]

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the file is not a valid JSON format.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory path

    file_path = os.path.join(current_dir, file_path)  # Get full path

    with open(file_path, "r", encoding="utf-8") as file:
        teams_data_load = json.load(file)

    teams_data = teams_data_load['teams']

    return teams_data


team_lookup_file = 'files/college_teams_lookup.json'
college_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/nfl_teams_lookup.json'
nfl_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/nba_teams_lookup.json'
nba_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/wnba_teams_lookup.json'
wnba_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/mlb_teams_lookup.json'
mlb_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/f1_teams_lookup.json'
f1_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/nascar_teams_lookup.json'
nascar_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/indy_teams_lookup.json'
indy_teams_data = open_json(team_lookup_file)
