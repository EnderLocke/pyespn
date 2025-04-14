from pyespn.core import *
from pyespn.data.leagues import LEAGUE_API_MAPPING, NO_TEAMS
from pyespn.data.teams import LEAGUE_TEAMS_MAPPING
from pyespn.data.betting import (BETTING_PROVIDERS,
                                 LEAGUE_DIVISION_FUTURES_MAPPING)
from pyespn.exceptions import API400Error
from pyespn.utilities import lookup_league_api_info
from pyespn.data.version import espn_api_version as v
from .decorators import *
from datetime import datetime
from typing import TYPE_CHECKING, Optional
import concurrent.futures

if TYPE_CHECKING:
    from pyespn.classes import Team, Player, Recruit, Event, League  # Only imports for type checking


@validate_league
class PYESPN:
    """
    Main client for interacting with ESPN's sports data API.

    This class serves as the central entry point for retrieving and managing data
    related to leagues, teams, players, drafts, betting, recruiting, and more.
    It is designed to support multiple sports leagues by using a unified interface
    and dynamic loading of league-specific components.

    Attributes:
        league_abbv (str): Abbreviation for the selected league (e.g., 'nfl', 'nba').
        teams (List[Team]): List of all teams in the current league.
        league (League): League-specific metadata and configuration.
        team_id_mapping (dict): Mapping of team IDs to team data for the current league.
        betting_providers (dict): Available betting providers for the current league.
        league_division_betting_keys (list): Division-level betting market keys.
        api_mapping (dict): API endpoint configuration for the current league.
        standings (dict): Season-specific standings data.
        drafts (dict): Draft results by season.
        recruit_rankings (dict): Recruiting rankings by season (college leagues only).
        athletes (dict): Athlete metadata and statistics by season.
        manufacturers (dict): Manufacturer/team-like objects (e.g., F1 constructors).
        v (str): ESPN API version.

    Args:
        sport_league (str): Abbreviation of the league to interact with (default is `'nfl'`).
        load_teams (bool): Whether to immediately load team data (default is `True`).

    Example:
        >>> from pyespn import PYESPN
        >>> espn = PYESPN('nfl')
        >>> espn.teams[0].name
        'Kansas City Chiefs'
    """
    LEAGUE_API_MAPPING = LEAGUE_API_MAPPING
    valid_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'available'}
    untested_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'untested'}
    all_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'unavailable'}

    def __init__(self, sport_league='nfl', load_teams=True):
        """
        Initializes the PYESPN instance for a specified sport league.

        Args:
            sport_league (str): The abbreviation of the league to interact with (default is 'nfl').
            load_teams (bool): Whether to load team data (default is True).
        """
        self._league_abbv = sport_league.lower()
        self._team_id_mapping = LEAGUE_TEAMS_MAPPING.get(self._league_abbv)
        self._betting_providers = BETTING_PROVIDERS
        # todo i think this key can be removed
        self._league_division_betting_keys = [key for key in LEAGUE_DIVISION_FUTURES_MAPPING.get(self._league_abbv, [])]
        self._api_mapping = lookup_league_api_info(league_abbv=self._league_abbv)
        self._v = v
        self._teams = []
        self.standings = {}
        self.recruit_rankings = {}
        self.drafts = {}
        self.manufacturers = {}
        self.athletes = {}
        self._league = None
        self._load_league_data()
        if load_teams:
            if self._api_mapping['sport'] not in NO_TEAMS:
                self._load_teams_datav2()
            else:
                self._load_manufacturers()

    @property
    def teams(self):
        """
        list[Team]: a list of teams in the league
        """
        return self._teams

    @property
    def league(self):
        """
            League: a league object representing the data for the league
        """
        return self._league

    @property
    def league_abbv(self):
        """
            str: league abbreviation for the league client is built for
        """
        return self._league_abbv

    @property
    def v(self):
        """
        str: api version for espn api
        """
        return self._v

    @property
    def team_id_mapping(self):
        """
        dict: Mapping of team IDs for the current league.
        """
        return self._team_id_mapping

    @property
    def betting_providers(self):
        """
        dict: Dictionary of betting providers supported by the API.
        """
        return self._betting_providers

    @property
    def league_division_betting_keys(self):
        """
        list: List of keys representing league division betting markets.
        """
        return self._league_division_betting_keys

    @property
    def api_mapping(self):
        """
        dict: Mapping of endpoints and API config values for the current league.
        """
        return self._api_mapping

    def __repr__(self) -> str:
        """
        Returns a string representation of the PYESPN instance.

        Returns:
            str: A formatted string with class details
        """
        return f"<PyESPN | League {self._league_abbv}>"

    def _load_teams_datav2(self):
        """
        Loads data for all teams in the current league using concurrency and stores them in the `teams` attribute.
        """

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.fetch_team_data, team): team for team in self._team_id_mapping}

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:  # Append only if result is not None
                    self._teams.append(result)

    def fetch_team_data(self, team):
        """
        Fetches team data for a given team ID.

        Args:
            team (dict): A dictionary containing the team's ID.

        Returns:
            team_cls (Team or None): The team instance if found, otherwise None.
        """
        try:
            team_cls = get_team_info_core(team_id=team['team_id'],
                                          league_abbv=self._league_abbv,
                                          espn_instance=self)
            return team_cls
        except API400Error:
            return None  # Skip teams that don't exist in the data

    def _load_league_data(self):
        """
        Loads data for the current league and stores it in the `league` attribute.
        """
        self._league = get_league_info_core(league_abbv=self._league_abbv,
                                            espn_instance=self)

    def load_seasons_futures(self, season):
        """
        Loads betting futures for a given season and stores them in the `betting_futures` attribute.

        Args:
            season (str): The season for which to load betting futures.
        """
        self.league.get_all_seasons_futures(season=season)

    def load_year_draft(self, season: int) -> None:
        """
        Loads draft data for a given season and stores it in the drafts dictionary.

        This method retrieves draft data for the specified season using
        `load_draft_data_core` and associates it with the season in the `drafts` attribute.

        Args:
            season (int): The season year for which to load draft data.

        Returns:
            None
        """

        self.drafts[season] = load_draft_data_core(season=season,
                                                   league_abbv=self._league_abbv,                                           espn_instance=self)

    def get_player_info(self, player_id) -> "Player":
        """
        Retrieves detailed information about a player.

        Args:
            player_id (str): The ID of the player.

        Returns:
            Player: The player's information in player class
        """
        return get_player_info_core(player_id=player_id,
                                    league_abbv=self._league_abbv,
                                    espn_instance=self)

    def get_player_ids(self) -> list:
        """
        Retrieves the IDs of all players in the league.

        Returns:
            list: A list of player IDs.
        """
        return get_player_ids_core(league_abbv=self._league_abbv)

    @requires_college_league('recruiting')
    def get_recruiting_rankings(self, season, max_pages=None) -> list["Recruit"]:
        """
        Retrieves the recruiting rankings for a given season.

        Args:
            season (int): The season for which to retrieve rankings.
            max_pages (int, optional): The maximum number of pages of data to retrieve.

        Returns:
            list[Recruit]: The recruiting rankings.
        """
        return get_recruiting_rankings_core(season=season,
                                            league_abbv=self._league_abbv,
                                            espn_instance=self,
                                            max_pages=max_pages)

    def load_year_recruiting_rankings(self, year: int):
        """
        Loads the regular season recruiting rankings for a given season and stores it in the `recruiting rankings` attribute.

        Args:
            year (int): The season for which to load the recruiting rankings.
        """

        self.recruit_rankings = {year: self.get_recruiting_rankings(season=year)}

    def get_game_info(self, event_id) -> "Event":
        """
        Retrieves detailed information about a specific game.

        Args:
            event_id (str or int): The ID of the game.

        Returns:
            Event: The game's information.
        """
        return get_game_info_core(event_id=event_id,
                                  league_abbv=self._league_abbv,
                                  espn_instnace=self)

    def get_season_team_stats(self, season) -> dict:
        """
        Retrieves statistics for teams during a specific season.

        Args:
            season (str or int): The season for which to retrieve stats.

        Returns:
            dict: The season's team statistics.
        """
        return get_season_team_stats_core(season=season,
                                          league_abbv=self._league_abbv)

    @requires_pro_league('draft')
    def get_draft_pick_data(self, season, pick_round, pick) -> dict:
        """
        Retrieves data about a specific draft pick.

        Args:
            season (int): The season of the draft.
            pick_round (int): The round of the pick.
            pick (int): The specific pick number.

        Returns:
            dict: The draft pick's data.
        """
        return get_draft_pick_data_core(season=season,
                                        pick_round=pick_round,
                                        pick=pick,
                                        league_abbv=self._league_abbv)

    def get_players_historical_stats(self, player_id) -> dict:
        """
        Retrieves historical statistics for a player.

        Args:
            player_id (str): The ID of the player.

        Returns:
            dict: The player's historical stats.
        """
        return get_players_historical_stats_core(player_id=player_id,
                                                 espn_instance=self,
                                                 league_abbv=self._league_abbv)

    def get_awards(self, season) -> list[dict]:
        """
        Retrieves awards for a given season.

        Args:
            season (str): The season for which to retrieve awards.

        Returns:
            list: The awards for the specified season.
        """
        return get_awards_core(season=season,
                               league_abbv=self._league_abbv)

    @requires_standings_available
    def load_standings(self, season) -> None:
        """
        Retrieves standings for a given season and type.

        Args:
            season (str): The season for which to retrieve standings.

        Returns:
            None
        """
        self.standings[season] = get_standings_core(season=season,
                                                    league_abbv=self._league_abbv,
                                                    espn_instance=self)

    def load_seasons_box_scores(self, season):

        self.load_season_rosters(season=season)
        for team in self._teams:
            team.load_season_roster_box_score(season=season)

    def get_team_by_id(self, team_id) -> "Team":
        """
        Finds and returns the Team object that matches the given team_id.

        Args:
            team_id (int or str): The ID of the team to find.

        Returns:
            Team: The matching Team object, or None if not found.
        """
        return next((team for team in self._teams if str(team.team_id) == str(team_id)), None)

    def load_season_rosters(self, season) -> None:
        """
        Loads the season roster for all teams in the league.

        This method iterates through all teams and calls their `load_season_roster`
        method to fetch and store the roster data for the specified season.

        Args:
            season (int or str): The season year for which to load rosters.

        Returns:
            None

        Example:
            >>> espn = PYESPN('nfl')
            >>> espn.load_season_rosters(season=2023)
            >>> for team in espn.teams:
            >>>     print(team.roster[2023])
            [<Player | John Doe>, <Player | Jane Smith>, ...]

        """

        for team in self._teams:
            team.load_season_roster(season=season)

    def load_season_team_stats(self, season) -> None:
        """
        Loads seasonal statistical data for each team in the league.

        Iterates through all teams in the current league instance and calls each team's
        `load_team_season_stats` method, passing in the specified season. This typically
        includes team-level metrics such as points scored, allowed, total yardage, turnovers, etc.

        Args:
            season (int): The season year for which team stats should be retrieved.
        """
        for team in self._teams:
            team.load_team_season_stats(season=season)

    def load_season_league_stat_leaders(self, season) -> None:
        """
        Loads the league's statistical leaders for the specified season.

        This method retrieves the statistical leaders for the given season
        by calling the `load_season_league_leaders` method on the league object.

        Args:
            season (str or int): The season for which the league's stat leaders
                                should be loaded. This can be a string (e.g., "2023")
                                or an integer (e.g., 2023).

        Returns:
            None: This method doesn't return any value. It performs an action
                  on the league object to load the stat leaders.
        """
        self.league.load_season_league_leaders(season=season)

    def load_seasons_betting_records(self, season) -> None:
        """
        Loads the betting records for each team in the specified season.

        This method iterates over all the teams in the instance and calls the
        `load_season_betting_records` method on each team to load their
        respective betting records for the given season.

        Args:
            season (str or int): The season for which the betting records need to be loaded.
                                This can be a string (e.g., "2023") or an integer (e.g., 2023).
        """
        for team in self._teams:
            team.load_season_betting_records(season=season)

    def load_season_teams_results(self, season) -> None:
        """
        Loads win/loss and game result data for each team in the specified season.

        For each team in the league, this method calls `load_season_results`, which
        fetches the outcomes of all games played during the season, including opponent
        data, scores, home/away context, and dates.

        Args:
            season (int): The season year for which game results should be retrieved.
        """
        for team in self._teams:
            team.load_season_results(season=season)

    def load_season_coaches(self, season) -> None:
        """
        Loads coaching staff information for each team for the specified season.

        This method calls each team's `load_season_coaches` method, which typically
        retrieves data such as head coach, offensive/defensive coordinators, tenure,
        and any mid-season coaching changes.

        Args:
            season (int): The season year for which coaching data should be retrieved.
        """
        for team in self._teams:
            team.load_season_coaches(season=season)

    def load_athletes(self, season) -> None:
        """
        Loads and stores athlete data for a given season.

        This function retrieves athlete data for the specified season using `load_athletes_core`
        and stores it in the `athletes` attribute of the instance.

        Args:
            season (int): The season year for which athlete data is being loaded.

        Returns:
            None: The retrieved athlete data is stored in `self.athletes[season]`.

        Notes:
            - Uses `load_athletes_core` to fetch athlete data.
            - Stores the result in `self.athletes` with the season as the key.
        """
        self.athletes[season] = load_athletes_core(season=season,
                                                   league_abbv=self._league_abbv,
                                                   espn_instance=self)

    def _load_manufacturers(self, season:str = None) -> None:
        """
        Loads the manufacturers data for a specific season and stores it in the
        instance's manufacturers attribute.

        This method retrieves the manufacturers data by calling the
        `get_manufacturers_core` function and stores the result in the
        `self.manufacturers` dictionary using the season as the key.

        Args:
            season (str, optional): The season for which the manufacturers data should be loaded.
                                    Defaults to the current year if not provided.
        Side Effects:
            - Updates the `self.manufacturers` dictionary with the manufacturers data
              for the given season.

        Example:
            # Assuming get_manufacturers_core retrieves manufacturer data for the season
            self._load_manufacturers('2025')
        """
        if season is None:
            season = str(datetime.now().year)  # Default to the current year if no season is provided

        self.manufacturers[season] = get_manufacturers_core(season=season,
                                                            espn_instance=self,
                                                            league_abbv=self._league_abbv)

    def check_teams_for_player_by_season(self, season, player_id) -> Optional["Player"]:
        """
        Searches through all teams for a specific player by season and player ID.

        Iterates over each team in `self._teams` and checks if the player with the given
        `player_id` was on the roster during the specified `season`. Returns the first
        matching athlete found.

        Args:
            season (int or str): The season year to search within each team.
            player_id (int or str): The unique identifier of the player to find.

        Returns:
            Player or None: The matching player object if found; otherwise, None.
        """
        athlete = None
        for team in self._teams:
            athlete = team.get_player_by_season_id(season=season,
                                                   player_id=player_id)
        return athlete
