# todo create a league version of the api that can pull a certain amount of data
from pyespn.core.decorators import validate_json


@validate_json("league_json")
class League:

    def __init__(self, espn_instance, league_json):
        pass
