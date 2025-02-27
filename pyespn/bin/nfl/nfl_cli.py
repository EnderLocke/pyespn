import click
import datetime

from pyespn.nfl import (get_nfl_players_historical_stats, get_player_info,
                        get_season_team_stats)

@click.command()
@click.argument('player_ids',
                nargs=-1)
#@click.option('--save-excel-file', '-sef', is_flag=True, default=True,
#              help='flag to save the output to current path')
def cli_pull_nfl_espn_stats(player_ids): #, save_excel_file: bool, save_path):
    """ cli function for hitting espn api for an nfl player(s)
    NOTE: max is 10 at a time

    :param player_ids: the list of ids to pull data for
    :return:
    """

    all_player_stats = []
    all_player_ids = list(player_ids)
    if len(all_player_ids) <= 10:
        pass
    else:
        raise click.BadParameter(
            "only 10 ids max at a time"
            f"you entered: {len(all_player_ids)}"
        )
    for player_id in all_player_ids:
        player_stats = get_nfl_players_historical_stats(player_id=player_id)
        this_json = {
            player_id: player_stats
        }
        all_player_stats.append(this_json)
    print(all_player_stats)

@click.command()
@click.argument('player_ids',
                nargs=-1)
def get_player_metadata(player_ids):
    all_player_info = []
    all_player_ids = list(player_ids)
    if len(all_player_ids) <= 10:
        pass
    else:
        raise click.BadParameter(
            "only 10 ids max at a time"
            f"you entered: {len(all_player_ids)}"
        )
    for player_id in all_player_ids:
        player_info = get_player_info(player_id)
        this_json = {
            player_id: player_info
        }
        all_player_info.append(this_json)
    print(all_player_info)

@click.command()
@click.argument('season')
@click.argument('team_id')
def get_team_season_stats(season, team_id):
    current_year = datetime.datetime.now().year
    if 1990 <= season <= current_year:
        pass
    else:
        click.BadParameter(f'season must be between 1990 and {current_year}')
    if 0 < team_id < 35:
        pass
    else:
        click.BadParameter(f'team id must be between 1 and 34')

    stats = get_season_team_stats(season=season,
                                  team=team_id)
    print(stats)
