import click

from espn.nfl import get_nfl_players_historical_stats

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



