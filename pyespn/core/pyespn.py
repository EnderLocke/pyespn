from pyespn.core import *
from pyespn.data.leagues import LEAGUE_API_MAPPING
from pyespn.data.teams import LEAGUE_TEAMS_MAPPING
from pyespn.data.betting import (BETTING_PROVIDERS, DEFAULT_BETTING_PROVIDERS_MAP,
                                 LEAGUE_DIVISION_FUTURES_MAPPING)
from .decorators import *


@validate_league
class PYESPN:
    LEAGUE_API_MAPPING = LEAGUE_API_MAPPING
    valid_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'available'}
    untested_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'untested'}
    all_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING if league['status'] == 'unavailable'}

    def __init__(self, sport_league='nfl', load_teams=True):
        self.league_abbv = sport_league.lower()
        self.TEAM_ID_MAPPING = LEAGUE_TEAMS_MAPPING.get(self.league_abbv)
        self.BETTING_PROVIDERS = BETTING_PROVIDERS
        self.LEAGUE_DIVISION_BETTING_KEYS = [key for key in LEAGUE_DIVISION_FUTURES_MAPPING.get(self.league_abbv, [])]
        self.DEFAULT_BETTING_PROVIDER = DEFAULT_BETTING_PROVIDERS_MAP.get(self.league_abbv)
        self.teams = []
        self.betting_futures = {}
        self.schedules = {}
        self.league = None
        self._load_league_data()
        if load_teams:
            self._load_teams_data()

    def _load_teams_data(self):
        for team in self.TEAM_ID_MAPPING:
            data, team_cls = self.get_team_info(team_id=team['team_id'])
            self.teams.append(team_cls)

    def _load_league_data(self):
        self.league = self.get_league_info()

    def load_seasons_futures(self, season):
        self.betting_futures = {season: self.get_all_seasons_futures(season=season)}

    def load_regular_season_schedule(self, season):
        self.schedules = {season: self.get_regular_seasons_schedule(season=season)}

    def __repr__(self):
        """
        Returns a string representation of the PYESPN instance.

        Returns:
            str: A formatted string with class details
        """
        return f"<PyESPN | League {self.league_abbv}>"

    def get_player_info(self, player_id):
        return get_player_info_core(player_id=player_id,
                                    league_abbv=self.league_abbv,
                                    espn_instance=self)

    def get_player_ids(self):
        return get_player_ids_core(league_abbv=self.league_abbv)

    @requires_college_league('recruiting')
    def get_recruiting_rankings(self, season, max_pages=None):
        return get_recruiting_rankings_core(season=season,
                                            league_abbv=self.league_abbv,
                                            max_pages=max_pages)

    def get_game_info(self, event_id):
        return get_game_info_core(event_id=event_id,
                                  league_abbv=self.league_abbv,
                                  espn_instnace=self)

    def get_team_info(self, team_id):
        return get_team_info_core(team_id=team_id,
                                  league_abbv=self.league_abbv,
                                  espn_instance=self)

    def get_season_team_stats(self, season):
        return get_season_team_stats_core(season=season,
                                          league_abbv=self.league_abbv)

    @requires_pro_league('draft')
    def get_draft_pick_data(self, season, pick_round, pick):
        return get_draft_pick_data_core(season=season,
                                        pick_round=pick_round,
                                        pick=pick,
                                        league_abbv=self.league_abbv)

    def get_players_historical_stats(self, player_id):
        return get_players_historical_stats_core(player_id=player_id,
                                                 league_abbv=self.league_abbv)

    @requires_betting_available
    def get_league_year_champion_futures(self, season, provider=None):
        this_provider = provider if provider else self.DEFAULT_BETTING_PROVIDER
        return get_year_league_champions_futures_core(season=season,
                                                      league_abbv=self.league_abbv,
                                                      provider=this_provider)

    @requires_betting_available
    def get_league_year_division_champs_futures(self, season, division, provider=None):
        this_provider = provider if provider else self.DEFAULT_BETTING_PROVIDER
        return get_division_champ_futures_core(season=season,
                                               division=division,
                                               league_abbv=self.league_abbv,
                                               provider=this_provider)

    @requires_betting_available
    def get_team_year_ats_away(self, team_id, season):
        return get_team_year_ats_away_core(team_id=team_id,
                                           season=season,
                                           league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home_favorite(self, team_id, season):
        return get_team_year_ats_home_favorite_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_away_underdog(self, team_id, season):
        return get_team_year_ats_away_underdog_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_favorite(self, team_id, season):
        return get_team_year_ats_favorite_core(team_id=team_id,
                                               season=season,
                                               league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home(self, team_id, season):
        return get_team_year_ats_home_core(team_id=team_id,
                                           season=season,
                                           league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_overall(self, team_id, season):
        return get_team_year_ats_overall_core(team_id=team_id,
                                              season=season,
                                              league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_underdog(self, team_id, season):
        return get_team_year_ats_underdog_core(team_id=team_id,
                                               season=season,
                                               league_abbv=self.league_abbv)

    @requires_betting_available
    def get_team_year_ats_home_underdog(self, team_id, season):
        return get_team_year_ats_home_underdog_core(team_id=team_id,
                                                    season=season,
                                                    league_abbv=self.league_abbv)

    @requires_betting_available
    def get_all_seasons_futures(self, season):
        return get_season_futures_core(season=season,
                                       league_abbv=self.league_abbv,
                                       espn_instance=self)

    def get_awards(self, season):
        return get_awards_core(season=season,
                               league_abbv=self.league_abbv)

    @requires_standings_available
    def get_standings(self, season, standings_type):
        return get_standings_core(season=season,
                                  standings_type=standings_type,
                                  league_abbv=self.league_abbv)

    def get_logo_img(self, team_id):
        return get_team_logo_img(team_id=team_id,
                                 league_abbv=self.league_abbv)

    def get_team_colors(self, team_id):
        return get_team_colors_core(team_id=team_id,
                                    league_abbv=self.league_abbv)

    def get_venue_data(self, team_id):
        return get_home_venue(team_id=team_id,
                              league_abbv=self.league_abbv)

    def get_league_info(self):
        return get_league_info_core(league_abbv=self.league_abbv,
                                    espn_instance=self)

    def get_weekly_schedule(self, season, week):
        return get_weekly_schedule_core(league_abbv=self.league_abbv,
                                        espn_instance=self,
                                        season=season,
                                        week=week)

    def get_regular_seasons_schedule(self, season):
        return get_regular_season_schedule_core(league_abbv=self.league_abbv,
                                                espn_instance=self,
                                                season=season)
