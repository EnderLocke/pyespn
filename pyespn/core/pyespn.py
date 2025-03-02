from pyespn.core import *
from pyespn.data.leagues import LEAGUE_API_MAPPING


class PYESPN():
    LEAGUE_API_MAPPING = LEAGUE_API_MAPPING
    valid_leagues = {league['league_abbv'] for league in LEAGUE_API_MAPPING}

    def __init__(self, sport_league='nfl'):
        # Validate sport_league
        if sport_league not in self.valid_leagues:
            raise ValueError(f"Invalid sport league: '{sport_league}'. Must be one of {self.valid_leagues}")

        self.league_abbv = sport_league

    def get_player_info(self, player_id):
        return get_player_info_core(player_id=player_id,
                                    league_abbv=self.league_abbv)

    def get_player_ids(self):
        return get_player_ids_core(league_abbv=self.league_abbv)

    def get_recruiting_rankings(self, season, max_pages=None):
        return get_recruiting_rankings_core(season=season,
                                            league_abbv=self.league_abbv,
                                            max_pages=max_pages)

    def get_game_info(self, event_id):
        return get_game_info_core(event_id=event_id,
                                  league_abbv=self.league_abbv)

    def get_team_info(self, team_id):
        return get_team_info_core(team_id=team_id,
                                  league_abbv=self.league_abbv)

    def get_season_team_stats(self, season):
        return get_season_team_stats_core(season=season,
                                          league_abbv=self.league_abbv)

    def get_draft_pick_data(self, season, pick_round, pick):
        return get_draft_pick_data_core(season=season,
                                        pick_round=pick_round,
                                        pick=pick,
                                        league_abbv=self.league_abbv)

    def get_players_historical_stats(self, player_id):
        return get_players_historical_stats_core(player_id=player_id,
                                                 league_abbv=self.league_abbv)

    def get_league_year_champion_futures(self, season, provider='DraftKings'):
        return get_year_league_champions_futures_core(season=season,
                                                      league_abbv=self.league_abbv,
                                                      provider=provider)
