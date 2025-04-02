from pyespn.core import *
from pyespn.data.leagues import LEAGUE_API_MAPPING
from pyespn.data.teams import LEAGUE_TEAMS_MAPPING
from pyespn.data.betting import (BETTING_PROVIDERS, DEFAULT_BETTING_PROVIDERS_MAP,
                                 LEAGUE_DIVISION_FUTURES_MAPPING)
from pyespn.exceptions import API400Error
from .decorators import *
import concurrent.futures


@validate_league
class PYESPN:
    """
    A class to interact with ESPN's API for retrieving and manipulating sports data related to leagues, teams, players, betting, schedules, drafts, and more.

    Attributes:
        LEAGUE_API_MAPPING (dict): A mapping of league abbreviations to corresponding league data.
        valid_leagues (set): A set of available league abbreviations.
        untested_leagues (set): A set of untested league abbreviations.
        all_leagues (set): A set of unavailable league abbreviations.
        league_abbv (str): The abbreviation of the currently selected sport league.
        TEAM_ID_MAPPING (dict): A mapping of team IDs to corresponding team data for the current league.
        BETTING_PROVIDERS (dict): A mapping of available betting providers for the current league.
        LEAGUE_DIVISION_BETTING_KEYS (list): A list of league division betting keys for the current league.
        DEFAULT_BETTING_PROVIDER (dict): The default betting provider for the current league.
        teams (list): A list of teams in the current league.
        betting_futures (dict): A mapping of betting futures for the current season.
        schedules (dict): A mapping of regular season schedules for the current season.
        league (dict): A dictionary containing data for the current league.

    Examples:
        >>> from pyespn import PYESPN
        >>> nfl_espn = PYESPN(sport_league='nfl')
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
        self.league_abbv = sport_league.lower()
        self.TEAM_ID_MAPPING = LEAGUE_TEAMS_MAPPING.get(self.league_abbv)
        self.BETTING_PROVIDERS = BETTING_PROVIDERS
        self.LEAGUE_DIVISION_BETTING_KEYS = [key for key in LEAGUE_DIVISION_FUTURES_MAPPING.get(self.league_abbv, [])]
        self.DEFAULT_BETTING_PROVIDER = DEFAULT_BETTING_PROVIDERS_MAP.get(self.league_abbv)
        self.teams = []
        self.betting_futures = {}
        self.schedules = {}
        self.recruit_rankings = {}
        self.drafts = {}
        self.league = None
        self._load_league_data()
        if load_teams:
            self._load_teams_datav2()

    def __repr__(self) -> str:
        """
        Returns a string representation of the PYESPN instance.

        Returns:
            str: A formatted string with class details
        """
        return f"<PyESPN | League {self.league_abbv}>"

    def _load_teams_data(self):
        """
        Loads data for all teams in the current league and stores them in the `teams` attribute.
        """
        for team in self.TEAM_ID_MAPPING:
            try:
                team_cls = self.get_team_info(team_id=team['team_id'])
                self.teams.append(team_cls)
            except API400Error as e:
                # right now i am assuming if it doesn't exist here its not in the data
                pass

    def _load_teams_datav2(self):
        """
        Loads data for all teams in the current league using concurrency and stores them in the `teams` attribute.
        """

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.fetch_team_data, team): team for team in self.TEAM_ID_MAPPING}

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:  # Append only if result is not None
                    self.teams.append(result)

    def fetch_team_data(self, team):
        """
        Fetches team data for a given team ID.

        Args:
            team (dict): A dictionary containing the team's ID.

        Returns:
            team_cls (Team or None): The team instance if found, otherwise None.
        """
        try:
            team_cls = self.get_team_info(team_id=team['team_id'])
            return team_cls
        except API400Error:
            return None  # Skip teams that don't exist in the data

    def _load_league_data(self):
        """
        Loads data for the current league and stores it in the `league` attribute.
        """
        self.league = self.get_league_info()

    def load_seasons_futures(self, season):
        """
        Loads betting futures for a given season and stores them in the `betting_futures` attribute.

        Args:
            season (str): The season for which to load betting futures.
        """
        self.betting_futures[season] = self.get_all_seasons_futures(season=season)

    def load_regular_season_schedule(self, season: int):
        """
        Loads the regular season schedule for a given season and stores it in the `schedules` attribute.

        Args:
            season (int): The season for which to load the schedule.
        """

        self.schedules[season] = self.get_regular_seasons_schedule(season=season)

    def load_year_draft(self, season: int):
        self.drafts[season] = load_draft_data_core(season=season,
                                                   league_abbv=self.league_abbv,
                                                   espn_instance=self)

    def get_player_info(self, player_id) -> dict:
        """
        Retrieves detailed information about a player.

        Args:
            player_id (str): The ID of the player.

        Returns:
            dict: The player's information.
        """
        return get_player_info_core(player_id=player_id,
                                    league_abbv=self.league_abbv,
                                    espn_instance=self)

    def get_player_ids(self) -> list:
        """
        Retrieves the IDs of all players in the league.

        Returns:
            list: A list of player IDs.
        """
        return get_player_ids_core(league_abbv=self.league_abbv)

    @requires_college_league('recruiting')
    def get_recruiting_rankings(self, season, max_pages=None) -> dict:
        """
        Retrieves the recruiting rankings for a given season.

        Args:
            season (int): The season for which to retrieve rankings.
            max_pages (int, optional): The maximum number of pages of data to retrieve.

        Returns:
            dict: The recruiting rankings.
        """
        return get_recruiting_rankings_core(season=season,
                                            league_abbv=self.league_abbv,
                                            espn_instance=self,
                                            max_pages=max_pages)

    def load_year_recruiting_rankings(self, year: int):
        """
        Loads the regular season schedule for a given season and stores it in the `schedules` attribute.

        Args:
            year (int): The season for which to load the schedule.
        """

        self.recruit_rankings = {year: self.get_recruiting_rankings(season=year)}

    def get_game_info(self, event_id) -> dict:
        """
        Retrieves detailed information about a specific game.

        Args:
            event_id (str): The ID of the game.

        Returns:
            dict: The game's information.
        """
        return get_game_info_core(event_id=event_id,
                                  league_abbv=self.league_abbv,
                                  espn_instnace=self)

    def get_team_info(self, team_id) -> dict:
        """
        Retrieves detailed information about a team.

        Args:
            team_id (str): The ID of the team.

        Returns:
            dict: The team's information.
        """
        return get_team_info_core(team_id=team_id,
                                  league_abbv=self.league_abbv,
                                  espn_instance=self)

    def get_season_team_stats(self, season):
        """
        Retrieves statistics for teams during a specific season.

        Args:
            season (str): The season for which to retrieve stats.

        Returns:
            dict: The season's team statistics.
        """
        return get_season_team_stats_core(season=season,
                                          league_abbv=self.league_abbv)

    @requires_pro_league('draft')
    def get_draft_pick_data(self, season, pick_round, pick):
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
                                        league_abbv=self.league_abbv)

    def get_players_historical_stats(self, player_id):
        """
        Retrieves historical statistics for a player.

        Args:
            player_id (str): The ID of the player.

        Returns:
            dict: The player's historical stats.
        """
        return get_players_historical_stats_core(player_id=player_id,
                                                 league_abbv=self.league_abbv)

    @requires_betting_available
    def get_league_year_champion_futures(self, season, provider=None):
        """
        Retrieves betting odds for the league champion for a given season.

        Args:
            season (str): The season for which to retrieve the champion futures.
            provider (str, optional): The betting provider to use.

        Returns:
            dict: The league champion futures for the specified season.
        """
        this_provider = provider if provider else self.DEFAULT_BETTING_PROVIDER
        return get_year_league_champions_futures_core(season=season,
                                                      league_abbv=self.league_abbv,
                                                      provider=this_provider)

    @requires_betting_available
    def get_league_year_division_champs_futures(self, season, division, provider=None):
        """
        Retrieves betting odds for division champions for a given season and division.

        Args:
            season (str): The season for which to retrieve division champion futures.
            division (str): The division for which to retrieve betting odds.
            provider (str, optional): The betting provider to use.

        Returns:
            dict: The division champion futures for the specified season and division.
        """
        this_provider = provider if provider else self.DEFAULT_BETTING_PROVIDER
        return get_division_champ_futures_core(season=season,
                                               division=division,
                                               league_abbv=self.league_abbv,
                                               provider=this_provider)

    @requires_betting_available
    def get_team_year_ats_away(self, team_id, season):
        """
        Retrieves the team's against the spread (ATS) performance for away games in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance for away games.
        """
        return get_team_year_ats_away_core(team_id=team_id,
                                           season=season,
                                           league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home_favorite(self, team_id, season):
        """
        Retrieves the team's ATS performance for home games as a favorite in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance for home games as a favorite.
        """
        return get_team_year_ats_home_favorite_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_away_underdog(self, team_id, season):
        """
        Retrieves the team's ATS performance for away games as an underdog in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance for away games as an underdog.
        """
        return get_team_year_ats_away_underdog_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_favorite(self, team_id, season):
        """
        Retrieves the team's ATS performance as a favorite in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance as a favorite.
        """
        return get_team_year_ats_favorite_core(team_id=team_id,
                                               season=season,
                                               league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home(self, team_id, season):
        """
        Retrieves the team's ATS performance for home games in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance for home games.
        """
        return get_team_year_ats_home_core(team_id=team_id,
                                           season=season,
                                           league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_overall(self, team_id, season):
        """
        Retrieves the team's overall ATS performance for a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's overall ATS performance.
        """
        return get_team_year_ats_overall_core(team_id=team_id,
                                              season=season,
                                              league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_underdog(self, team_id, season):
        """
        Retrieves the team's ATS performance as an underdog in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance as an underdog.
        """
        return get_team_year_ats_underdog_core(team_id=team_id,
                                               season=season,
                                               league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home_underdog(self, team_id, season):
        """
        Retrieves the team's ATS performance for home games as an underdog in a given season.

        Args:
            team_id (str): The ID of the team.
            season (str): The season for which to retrieve ATS data.

        Returns:
            dict: The team's ATS performance for home games as an underdog.
        """
        return get_team_year_ats_home_underdog_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_all_seasons_futures(self, season):
        """
        Retrieves all betting futures for a given season.

        Args:
            season (str): The season for which to retrieve betting futures.

        Returns:
            dict: All betting futures for the specified season.
        """
        return get_season_futures_core(season=season,
                                       league_abbv=self.league_abbv,
                                       espn_instance=self)

    def get_awards(self, season):
        """
        Retrieves awards for a given season.

        Args:
            season (str): The season for which to retrieve awards.

        Returns:
            dict: The awards for the specified season.
        """
        return get_awards_core(season=season,
                               league_abbv=self.league_abbv)

    @requires_standings_available
    def get_standings(self, season, standings_type):
        """
        Retrieves standings for a given season and type.

        Args:
            season (str): The season for which to retrieve standings.
            standings_type (str): The type of standings (e.g., 'division', 'conference').

        Returns:
            dict: The standings for the specified season and type.
        """
        return get_standings_core(season=season,
                                  standings_type=standings_type,
                                  league_abbv=self.league_abbv)

    def get_league_info(self) -> dict:
        """
        Retrieves information about the league.

        Returns:
            dict: The league's information.
        """
        return get_league_info_core(league_abbv=self.league_abbv,
                                    espn_instance=self)

    def get_regular_seasons_schedule(self, season:int):
        """
        Retrieves the regular season schedule for a given season.

        Args:
            season (int): The season for which to retrieve the schedule.

        Returns:
            dict: The regular season schedule for the specified season.
        """
        return get_regular_season_schedule_core(league_abbv=self.league_abbv,
                                                espn_instance=self,
                                                season=season)

    def get_team_by_id(self, team_id):
        """
        Finds and returns the Team object that matches the given team_id.

        Args:
            team_id (int or str): The ID of the team to find.

        Returns:
            Team: The matching Team object, or None if not found.
        """
        return next((team for team in self.teams if str(team.team_id) == str(team_id)), None)
