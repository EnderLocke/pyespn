# todo add recruiting rankings
#  to get stars its more complicated. i had to wait until the dom loaded
#  the rating-#_stars.png file so i could get the # for the stars

# https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/recruiting/${year}/athletes?page=${page}
import requests
import json


def get_recruiting_rankings(season):
    url = f'https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/recruiting/${season}/athletes'
    response = requests.get(url)
    content = json.loads(response.content)
    num_of_pages = content['pageCount']

    recruiting_data = []
    rank = 1
    for page in range(1, num_of_pages):
        paged_url = url + f'?page={page}'
        paged_response = requests.get(paged_url)
        paged_content = json.loads(paged_response.content)
        for recruit in paged_content['items']:
            this_recruit = {
                'first_name': recruit['firstName'],
                'last_name': recruit['lastName'],
                'id': recruit['id'],
                'position': recruit['position']['abbreviation'],
                'class': recruit['recruitingClass'],
                'grade': recruit['grade'],
                'rank': rank,

            }
            rank += 1
            recruiting_data.append(this_recruit)

    return recruiting_data
