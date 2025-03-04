from pyespn.utilities import open_json

team_lookup_file = 'files/college_teams_lookup.json'
college_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/nfl_teams_lookup.json'
nfl_teams_data = open_json(team_lookup_file)

team_lookup_file = 'files/nba_teams_lookup.json'
nba_teams_data = open_json(team_lookup_file)
