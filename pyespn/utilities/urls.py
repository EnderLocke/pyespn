

def get_team_id(url):
    team_id = url.split('/')[url.split('/').index('teams') + 1].split('?')[0]
    return int(team_id)


def get_athlete_id(url):
    athlete_id = url.split('/')[url.split('/').index('athletes') + 1].split('?')[0]
    return int(athlete_id)


def get_schedule_type(url):
    schedule_type = url.split('/')[url.split('/').index('types') + 1].split('?')[0]
    return int(schedule_type)


def get_an_id(url, slug):
    this_id = url.split('/')[url.split('/').index(slug) + 1].split('?')[0]
    return int(this_id)
