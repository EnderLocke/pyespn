# todo add recruiting rankings
#  to get stars its more complicated. i had to wait until the dom loaded
#  the rating-#_stars.png file so i could get the # for the stars

# https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/recruiting/${year}/athletes?page=${page}
import requests
import json


def get_recruiting_rankings(season, max_pages=None):
    url = f'https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/recruiting/{season}/athletes'
    response = requests.get(url)
    content = json.loads(response.content)
    if not max_pages:
        num_of_pages = content['pageCount']
    else:
        num_of_pages = max_pages

    recruiting_data = []
    rank = 1
    for page in range(1, num_of_pages + 1):
        paged_url = url + f'?page={page}'
        paged_response = requests.get(paged_url)
        paged_content = json.loads(paged_response.content)
        for recruit in paged_content['items']:
            athlete = recruit['athlete']
            this_recruit = {
                'first_name': athlete.get('firstName'),
                'last_name': athlete.get('lastName'),
                'id': athlete.get('id'),
                'position': athlete.get('position').get('abbreviation'),
                'class': recruit.get('recruitingClass'),
                'grade': recruit.get('grade'),
                'rank': rank,
                'stars': None

            }
            rank += 1
            recruiting_data.append(this_recruit)

    return recruiting_data
