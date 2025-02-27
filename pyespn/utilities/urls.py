

def get_team_id(url):
    team_id = url.split('/')[url.split('/').index('teams') + 1].split('?')[0]
    return team_id
