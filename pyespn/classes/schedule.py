from pyespn.core.decorators import validate_json
from pyespn.utilities import fetch_espn_data, get_schedule_type, get_an_id
from pyespn.classes import Event


class Schedule:

    def __init__(self, espn_instance, schedule_list):
        self.schedule_list = schedule_list
        self.espn_instance = espn_instance
        self.schedule_type = None

        schedule_type_id = get_schedule_type(self.schedule_list[0])

        if schedule_type_id == 1:
            self.schedule_type = 'preseason'
        elif schedule_type_id == 2:
            self.schedule_type = 'regular'
        elif schedule_type_id == 3:
            self.schedule_type = 'post'

        self._set_schedule_data()

    def __repr__(self):
        """
        Returns a string representation of the schedule instance.

        Returns:
            str: A formatted string with the schedule.
        """
        return f"<Schedule | {self.schedule_type})>"


    def _set_schedule_data(self):

        for week_url in self.schedule_list:
            api_url = week_url.split('?')[0] + f'/events'
            week_content = fetch_espn_data(api_url)
            # todo here i need to capture the data
            week_pages = week_content.get('pageCount')

            for week_page in range(1, week_pages + 1):
                weekly_url = api_url + f'?page={week_page}'
                this_week_content = fetch_espn_data(weekly_url)
                event_urls = []
                for event in this_week_content.get('items', []):
                    event_urls.append(event.get('$ref'))
                self.weeks = Week(espn_instance=self.espn_instance,
                                  week_list=event_urls)


class Week:

    def __init__(self, espn_instance, week_list):
        self.espn_instance = espn_instance
        self.week_list = week_list
        self.events = []
        self.week_number = None

        self.week_number = get_an_id(url=self.week_list[0],
                                     slug='week')

        self._set_week_data()

    def __repr__(self):
        """
        Returns a string representation of the week instance.

        Returns:
            str: A formatted string with the week.
        """
        return f"<Week | {self.week_number})>"

    def _set_week_data(self):
        for event in self.week_list:
            event_content = fetch_espn_data(event.get('$ref'))
            self.events.append(Event(event_json=event_content,
                                     espn_instance=self.espn_instance))

