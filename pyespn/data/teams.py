from .data_import import *

LEAGUE_TEAMS_MAPPING = {
    'nfl': nfl_teams_data,
    'nba': nba_teams_data,
    'cfb': college_teams_data,
    'mcbb': college_teams_data,
    'cbb': college_teams_data,
    'csb': college_teams_data,
    'wnba': wnba_teams_data,
    'mlb': mlb_teams_data,
    'f1': f1_teams_data,
    'nascar': nascar_teams_data,
    'indy': indy_teams_data
}

team_files_path = './files/'


def build_team_files():
    pass
