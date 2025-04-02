from pyespn.data.version import espn_api_version as v
from pyespn.utilities import (fetch_espn_data, get_schedule_type,
                              get_an_id, lookup_league_api_info)
from pyespn.exceptions import ScheduleTypeUnknownError
from pyespn.classes import Event
from datetime import datetime
import concurrent.futures


class Schedule:
    """
    Represents a sports league schedule.

    Attributes:
        espn_instance (PyESPN): The ESPN API instance.
        schedule_list (list[str]): A list of schedule URLs.
        schedule_type (str): The type of schedule (e.g., 'regular', 'postseason').
        season (int): The season year.
        weeks (list[Week]): A list of Week instances containing events.

    Methods:
        get_events(week: int) -> list[Event]:
            Retrieves the list of Event instances for the given week.
    """
    def __init__(self, espn_instance, schedule_list: list):
        """
        Inits the sports schedule class

        :param espn_instance:
        :param schedule_list:
        """
        self.schedule_list = schedule_list
        self.espn_instance = espn_instance
        self.league_api = lookup_league_api_info(self.espn_instance.league_abbv)
        self.season = get_an_id(self.schedule_list[0], 'seasons')
        self.schedule_type = None
        self.weeks = []

        schedule_type_id = get_schedule_type(self.schedule_list[0])

        if schedule_type_id == 1:
            self.schedule_type = 'pre'
        elif schedule_type_id == 2:
            self.schedule_type = 'regular'
        elif schedule_type_id == 3:
            self.schedule_type = 'post'

        if self.league_api.get('schedule') == 'weekly':
            self._set_schedule_weekly_data()
        elif self.league_api.get('schedule') == 'daily':
            self._set_schedule_daily_data()
        else:
            raise ScheduleTypeUnknownError(league_abbv=self.espn_instance.league_abbv)

    def __repr__(self):
        """
        Returns a string representation of the schedule instance.

        Returns:
            str: A formatted string with the schedule.
        """
        return f"<Schedule | {self.season} {self.schedule_type} season>"

    def _set_schedule_daily_data(self):
        for week_url in self.schedule_list:
            api_url = week_url
            week_content = fetch_espn_data(api_url)
            start_date = datetime.strptime(week_content.get('startDate')[:10], "%Y-%m-%d")
            end_date = datetime.strptime(week_content.get('endDate')[:10], "%Y-%m-%d")
            week_number = get_an_id(url=api_url,
                                    slug='weeks')
            week_events_url = f'http://sports.core.api.espn.com/{v}/sports/{self.league_api.get("sport")}/leagues/{self.league_api.get("league")}/events?dates={start_date.strftime("%Y%m%d")}-{end_date.strftime("%Y%m%d")}'
            week_content = fetch_espn_data(week_events_url)
            week_pages = week_content.get('pageCount')
            week_events = []
            for week in range(1, week_pages + 1):
                week_page_url = week_events_url + f"&page={week}"
                week_page_content = fetch_espn_data(week_page_url)

                for event in week_page_content.get('items', []):
                    week_events.append(event.get('$ref'))
                    pass

            self.weeks.append(Week(espn_instance=self.espn_instance,
                                   week_list=week_events,
                                   week_number=week_number,
                                   start_date=start_date,
                                   end_date=end_date))
            pass

    def _set_schedule_weekly_data(self):

        for week_url in self.schedule_list:
            weekly_content = fetch_espn_data(url=week_url)
            start_date = datetime.strptime(weekly_content.get('startDate')[:10], "%Y-%m-%d")
            end_date = datetime.strptime(weekly_content.get('endDate')[:10], "%Y-%m-%d")
            api_url = week_url.split('?')[0] + f'/events'
            week_content = fetch_espn_data(api_url)
            week_pages = week_content.get('pageCount')
            week_number = get_an_id(url=api_url,
                                    slug='weeks')
            for week_page in range(1, week_pages + 1):
                weekly_url = api_url + f'?page={week_page}'
                this_week_content = fetch_espn_data(weekly_url)
                event_urls = []
                for event in this_week_content.get('items', []):
                    event_urls.append(event.get('$ref'))

            self.weeks.append(Week(espn_instance=self.espn_instance,
                                   week_list=event_urls,
                                   week_number=week_number,
                                   start_date=start_date,
                                   end_date=end_date))

    def get_events(self, week: int) -> list["Event"]:
        """
        Retrieves the list of events for the specified week.

        Args:
            week (int): The week number to retrieve events for.

        Returns:
            list[Event]: A list of Event instances representing the scheduled games.
        """
        return self.weeks[week + 1].events


class Week:
    """
    Represents a week's worth of games for a league schedule.

    Attributes:
        espn_instance (PyESPN): The ESPN API instance.
        week_list (list[str]): A list of event URLs or event data references.
        week_number (int): The numerical representation of the week.
        events (list[Event]): A list of Event instances for this week.

    Methods:
        get_events() -> list[Event]:
            Retrieves the list of Event instances for this week.
    """
    def __init__(self, espn_instance, week_list: list,
                 week_number: int, start_date, end_date):
        """
        Initializes a Week instance.

        Args:
            espn_instance (PyESPN): The ESPN API instance.
            week_list (list[str]): A list of event URLs or event data references.
            week_number (int): The numerical representation of the week.
        """
        self.espn_instance = espn_instance
        self.week_list = week_list
        self.events = []
        self.week_number = None
        self.start_date = start_date
        self.end_date = end_date
        self.week_number = week_number

        self._set_week_datav2()

    def __repr__(self):
        """
        Returns a string representation of the week instance.

        Returns:
            str: A formatted string with the week.
        """
        return f"<Week | {self.week_number}>"

    def _set_week_data(self) -> None:
        """
        Populates the events list by fetching event data for the given week.
        """
        for event in self.week_list:
            event_content = fetch_espn_data(event)
            self.events.append(Event(event_json=event_content,
                                     espn_instance=self.espn_instance))

    def _set_week_datav2(self) -> None:
        """
        Populates the events list by fetching event data concurrently.

        Returns:
            None
        """
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self._fetch_event, event): event for event in self.week_list}

            for future in concurrent.futures.as_completed(futures):
                try:
                    self.events.append(future.result())  # Append event when future is done
                except Exception as e:
                    print(f"Error fetching event: {e}")  # Handle failed API calls gracefully

    def _fetch_event(self, event_url):
        """
        Fetches event data from the given URL.

        Args:
            event_url (str): The event URL.

        Returns:
            Event: An Event instance.
        """
        event_content = fetch_espn_data(event_url)
        return Event(event_json=event_content, espn_instance=self.espn_instance)

    def get_events(self) -> list["Event"]:
        """
        Retrieves the list of Event instances for this week.

        Returns:
            list[Event]: A list of Event instances for the week.
        """
        return self.events
