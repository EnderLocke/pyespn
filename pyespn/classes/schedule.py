from pyespn.core.decorators import validate_json
from pyespn.classes import Event


@validate_json("schedule_json")
class Schedule:

    def __init__(self, espn_instance, schedule_json):
        self.espn_instance = espn_instance
        self.schedule_json = schedule_json


    def _set_schedule_data(self):
        pass

