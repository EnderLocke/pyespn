from pyespn.utilities import (fetch_espn_data, get_schedule_type,
                              get_an_id)
from pyespn.exceptions import ScheduleTypeUnknownError
from pyespn.classes import Event
from datetime import datetime, timezone
import concurrent.futures


class Schedule:
    """
    Represents a sports league schedule, capable of handling both weekly and daily formats.

    This class is responsible for loading and organizing schedule data for a given season,
    including determining the current week, fetching events, and storing them in `Week` objects.

    Attributes:
        espn_instance (PYESPN): The ESPN API wrapper instance.
        schedule_list (list[str]): A list of URLs referencing weekly or daily schedule endpoints.
        schedule_type (str): The type of schedule ('pre', 'regular', 'post', 'off', or 'play in').
        season (int): The season year, parsed from the schedule URL.
        weeks (list[Week]): A list of Week instances containing schedule events.
        current_week (Week or None): The Week instance that corresponds to the current date, if applicable.

    Methods:
        get_events(week: int) -> list[Event]:
            Retrieves the list of Event instances for the given week number.

        _set_schedule_weekly_data() -> None:
            Loads and processes weekly-formatted schedule data, detecting the current week.

        _set_schedule_daily_data() -> None:
            Loads and processes daily-formatted schedule data, detecting the current week.

        to_dict() -> list:
            Returns the original list of schedule URLs, suitable for serialization or debugging.

    Notes:
        - The class automatically determines whether the league uses a weekly or daily schedule
          based on API metadata.
        - The current week is determined by comparing today's date with the start and end dates
          of each weekly/daily block.
    """

    def __init__(self, espn_instance, schedule_list: list,
                 load_current_week_only: bool = False,
                 load_odds: bool = False,
                 load_plays: bool = False):
        """
        Initializes the Schedule instance.

        Args:
            espn_instance (PYESPN): The ESPN API wrapper instance.
            schedule_list (list[str]): A list of URLs pointing to schedule data for the season.
            load_current_week_only (bool): If True, only the current week will be processed.
            load_odds (bool): If True, odds data will be loaded for each event.
            load_plays (bool): If True, play-by-play data will be loaded for each event.
        """
        self.schedule_list = schedule_list
        self._espn_instance = espn_instance
        self.only_current_week = load_current_week_only
        self.load_odds = load_odds
        self.load_plays = load_plays
        self.api_info = self._espn_instance.api_mapping

        self.season = get_an_id(self.schedule_list[0], 'seasons')
        self.schedule_type = None
        self._current_week = None
        self._weeks = []

        schedule_type_id = get_schedule_type(self.schedule_list[0])

        if schedule_type_id == 1:
            self.schedule_type = 'pre'
        elif schedule_type_id == 2:
            self.schedule_type = 'regular'
        elif schedule_type_id == 3:
            self.schedule_type = 'post'
        elif schedule_type_id == 4:
            self.schedule_type = 'off'
        elif schedule_type_id == 5:
            self.schedule_type = 'play in'

        if self.api_info.get('schedule') == 'weekly':
            self._set_schedule_weekly_data()
        elif self.api_info.get('schedule') == 'daily':
            self._set_schedule_daily_data()
        else:
            raise ScheduleTypeUnknownError(league_abbv=self._espn_instance.league_abbv)

    @property
    def current_week(self):
        """
            Week: the current week in the season
        """
        return self._current_week

    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance

    @property
    def weeks(self):
        """
            list[Week]: a list of Week objects
        """
        return self._weeks

    def __repr__(self) -> str:
        """
        Returns a string representation of the schedule instance.

        Returns:
            str: A formatted string with the schedule.
        """
        return f"<Schedule | {self.season} {self.schedule_type} season>"

    def _set_schedule_daily_data(self) -> None:
        """
        Constructs the schedule for leagues using a daily schedule format.

        This method fetches data for each provided schedule URL and builds a list of
        events within the specified date range. Each page of event data is retrieved
        and its events are collected before constructing a Week object.
        """

        for week_url in self.schedule_list:
            api_url = week_url
            week_content = fetch_espn_data(api_url)
            start_date = datetime.strptime(week_content.get('startDate')[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            end_date = datetime.strptime(week_content.get('endDate')[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            self.now = datetime.now(timezone.utc)

            if start_date <= self.now <= end_date:
                current_week = True
            else:
                current_week = False
            if not self.only_current_week or current_week:
                week_number = get_an_id(url=api_url,
                                        slug='weeks')
                week_events_url = f'http://sports.core.api.espn.com/{self._espn_instance.v}/sports/{self.api_info.get("sport")}/leagues/{self.api_info.get("league")}/events?dates={start_date.strftime("%Y%m%d")}-{end_date.strftime("%Y%m%d")}'
                week_content = fetch_espn_data(week_events_url)
                week_pages = week_content.get('pageCount')
                week_events = []
                for week in range(1, week_pages + 1):
                    week_page_url = week_events_url + f"&page={week}"
                    week_page_content = fetch_espn_data(week_page_url)

                    for event in week_page_content.get('items', []):
                        week_events.append(event.get('$ref'))
                this_week = (Week(espn_instance=self._espn_instance,
                                  week_list=week_events,
                                  week_number=week_number,
                                  start_date=start_date,
                                  end_date=end_date))
                if not self.only_current_week:
                    self._weeks.append(this_week)
                if current_week:
                    self._current_week = this_week

    def _set_schedule_weekly_data(self) -> None:
        """
        Constructs the schedule for leagues using a weekly schedule format.

        This method paginates through each week's event data from the ESPN API and
        assembles a list of event references to create corresponding Week instances.
        """
        for week_url in self.schedule_list:
            weekly_content = fetch_espn_data(url=week_url)
            start_date = datetime.strptime(weekly_content.get('startDate')[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            end_date = datetime.strptime(weekly_content.get('endDate')[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            self.now = datetime.now(timezone.utc)

            if start_date <= self.now <= end_date:
                current_week = True
            else:
                current_week = False

            if not self.only_current_week or current_week:
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
                    if event_urls:
                        this_week = Week(espn_instance=self._espn_instance,
                                         week_list=event_urls,
                                         week_number=week_number,
                                         start_date=start_date,
                                         end_date=end_date)
                        if not self.only_current_week:
                            self._weeks.append(this_week)
                        if current_week:
                            self._current_week = this_week

    def get_events(self, week_num: int) -> list["Event"]:
        """
        Retrieves the list of events for the specified week.

        Args:
            week_num (int): The week number to retrieve events for.

        Returns:
            list[Event]: A list of Event instances representing the scheduled games for the specified week.

        Raises:
            StopIteration: If no Week instance is found for the specified week number.
        """
        week = next((week for week in self._weeks if str(week.week_number) == str(week_num)), None)

        if week is None:
            raise ValueError(f"No events found for week number {week_num}")

        return week.events

    def to_dict(self) -> list:
        """
        Converts the Schedule instance to its original list of JSON dictionaries.

        Returns:
            list: A list of dictionaries, each representing a scheduled event or game.

        Note:
            This method returns the raw schedule data as a list of dictionaries,
            suitable for serialization or further processing.
        """
        return self.schedule_list


class Week:
    """
    Represents a week's worth of games for a league schedule.

    Attributes:
        week_list (list[str]): A list of event URLs or event data references for the week.
        week_number (int): The numerical representation of the week (e.g., Week 1, Week 2).
        start_date (str): The start date of the week (ISO 8601 format or as provided).
        end_date (str): The end date of the week (ISO 8601 format or as provided).

    Methods:
        __repr__() -> str:
            Returns a string representation of the Week instance showing the week number.

        get_events() -> list[Event]:
            Retrieves the list of Event instances for this week.

        _set_week_data() -> None:
            (Legacy) Populates the events list sequentially by fetching data for each event.

        _set_week_datav2() -> None:
            Populates the events list concurrently using threading for faster data fetching.

        _fetch_event(event_url: str) -> Event:
            Fetches and returns a single Event instance given a URL.
    """

    def __init__(self, espn_instance, week_list: list,
                 week_number: int, start_date, end_date):
        """
        Initializes a Week instance.

        Args:
            espn_instance (PyESPN): The primary ESPN API wrapper instance.
            week_list (list[str]): A list of event reference URLs (or identifiers) for games in the week.
            week_number (int): The numerical representation of the week (e.g., 1 for Week 1).
            start_date (str or datetime): The start date of the week.
            end_date (str or datetime): The end date of the week.
        """
        self._espn_instance = espn_instance
        self.week_list = week_list
        self._events = []
        self._events_today = []
        self.week_number = None
        self.start_date = start_date
        self.end_date = end_date
        self.now = datetime.now(timezone.utc)

        if start_date <= self.now <= end_date:
            self._current_week = True
        else:
            self._current_week = False

        self.week_number = week_number

        self._set_week_datav2()

    @property
    def events_today(self):
        """
        list[Event]: A list of Event objects scheduled for today.

        This property returns only the events whose scheduled date matches today's date (UTC).
        Useful for quickly accessing games or matches occurring on the current day.
        """
        return self._events_today

    @property
    def current_week(self):
        """
            bool: true if this weeks events is the current week
        """
        return self._current_week
        
    @property
    def espn_instance(self):
        """
            PYESPN: the espn client instance associated with the class
        """
        return self._espn_instance
    
    @property
    def events(self):
        """
            list[Event]: a list of Event objects
        """
        return self._events

    def __repr__(self) -> str:
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
            self._events.append(Event(event_json=event_content,
                                      espn_instance=self._espn_instance,
                                      load_game_odds=self._espn_instance.league.load_game_odds,
                                      load_play_by_play=self._espn_instance.league.load_game_play_by_play))

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
                    f = future.result()
                    self._events.append(f)  # Append event when future is done
                    if f.today:
                        self._events_today.append(f)
                except Exception as e:
                    print(f"Error fetching event: {e}")  # Handle failed API calls gracefully

    def _fetch_event(self, event_url) -> "Event":
        """
        Fetches event data from the given URL.

        Args:
            event_url (str): The event URL.

        Returns:
            Event: An Event instance.
        """
        event_content = fetch_espn_data(event_url)
        return Event(event_json=event_content,
                     espn_instance=self._espn_instance,
                     load_game_odds=self._espn_instance.league.load_game_odds,
                     load_play_by_play=self._espn_instance.league.load_game_play_by_play)

    def get_events(self) -> list["Event"]:
        """
        Retrieves the list of Event instances for this week.

        Returns:
            list[Event]: A list of Event instances for the week.
        """
        return self._events

    def load_event_officials(self):
        """
        Loads officials for all events in the week.

        Iterates through all Event instances associated with this Week and calls
        `load_officials` on each to fetch and attach their respective officials data
        from the ESPN API.

        This enriches each event in the week with information about referees,
        umpires, or other officiating personnel.

        Returns:
            None

        Example:
            >>> week.load_event_officials()
            >>> for event in week.events:
            >>>     print(event.officials)
        """
        for event in self._events:
            event.load_officials()

    def load_event_broadcasts(self):
        """
        Loads broadcast data for all events in the week.

        This method iterates through each `Event` instance in the `_events` list
        and calls its `load_broadcasts` method to fetch and store associated
        broadcast information.

        Returns:
            None

        Example:
            >>> week.load_event_broadcasts()
            >>> for event in week.events:
            >>>     print(event.broadcasts)
        """
        for event in self._events:
            event.load_broadcasts()

