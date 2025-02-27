import json
import os

team_lookup_file = 'teams_lookup.json'
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory path

file_path = os.path.join(current_dir, team_lookup_file)  # Get full path

with open(file_path, "r", encoding="utf-8") as file:
    teams_data_load = json.load(file)

nfl_teams_data = teams_data_load['teams']
