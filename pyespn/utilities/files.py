import os
import json


def open_json(file_path):
    team_lookup_file = file_path
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory path

    file_path = os.path.join(current_dir, team_lookup_file)  # Get full path

    with open(file_path, "r", encoding="utf-8") as file:
        teams_data_load = json.load(file)

    teams_data = teams_data_load['teams']

    return teams_data
