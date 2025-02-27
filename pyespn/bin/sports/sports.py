import click
from pyespn.sports import get_all_base_apis

@click.command()
def get_all_sports_apis():
    apis = get_all_base_apis()
    print(apis)
