# PyESPN

[![documentation](https://img.shields.io/badge/docs-pyespn-blue.svg?style=flat)](https://enderlocke.github.io/pyespn/)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/EnderLocke/pyespn/deploy.yml)

![PyPI - Downloads](https://img.shields.io/pypi/dm/pyespn)
![PyPI - Version](https://img.shields.io/pypi/v/pyespn)
![PyPI - Status](https://img.shields.io/pypi/status/pyespn)
![PyPI - License](https://img.shields.io/pypi/l/pyespn)

![GitHub language count](https://img.shields.io/github/languages/count/EnderLocke/pyespn)
![GitHub top language](https://img.shields.io/github/languages/top/EnderLocke/pyespn)

## Introduction

PyESPN is a work in progress for hitting the ESPN API with Python, I am not affiliated with ESPN.

## Easy to Use

### How to Install

```
pip install pyespn
```

### Pick a league

```py
from pyespn import PYESPN

espn = PYESPN('nfl')
```

### Grab some data

```py
from pyespn import PYESPN

season = 2024
espn = PYESPN('nfl')
espn.load_season_rosters(season=season)
espn.load_season_schedule(season=season, load_postseason=True)
```

### Data Organization

The data is organized throughout classes, our detailed documents have detailed out each class, but most of the 
data you will look for will be with the .teams or .league attribute to the client

```py
from pyespn import PYESPN

season = 2024
espn = PYESPN('nfl')
espn.load_season_rosters(season=season)
espn.load_season_schedule(season=season, load_postseason=True)
for team in espn.teams:
    print(team.name)
    for athlete in team.roster.get(season, []):
        print(athlete.name)
```

## Extras

not all api end points are available for all leagues, some return errors some return no data.

for more details please see [detailed documents](https://enderlocke.github.io/pyespn/)  

and read the [CHANGELOG.md](CHANGELOG.md) for version to version changes