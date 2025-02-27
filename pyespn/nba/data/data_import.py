import json

team_lookup_file = 'teams_lookup.json'

teams_data_load = json.loads(team_lookup_file)

nba_teams_data = teams_data_load['teams']
