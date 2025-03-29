from pyespn.core.decorators import validate_json
from pyespn.classes import Event


@validate_json("schedule_json")
class Schedule:

    def __init__(self, espn_instance, schedule_json):
        self.schedule_json = schedule_json
        self.espn_instance = espn_instance

    def _set_schedule_data(self):
        # todo this is 1 preseason 2 regular 3 post
        self.schedule_type = 'regular'


@validate_json("week_json")
class Week:

    def __init__(self, espn_instance, week_json):
        self.espn_instance = espn_instance
        self.week_json = week_json


    def _set_schedule_data(self):
        pass

