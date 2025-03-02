from .data_import import nba_teams_data, nfl_teams_data, college_teams_data

LEAGUE_TEAMS_MAPPING = {
    'nfl': nfl_teams_data,
    'nba': nba_teams_data,
    'cfb': college_teams_data,
    'mcbb': college_teams_data
}
