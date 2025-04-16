# Changelog

## 0.3.4
* adding in preseason/postseason schedules
  * also play in for nba
* added in depthchart api endpoints
* added in current_week/todays_events across schedule/week classes
* event has a today indicator
* added in indicators in week/events if it is today/this week
* added in current_week property in schedule class
* added in events_today property in weeks class
* added in function to event to load the officials for it
* added in function to add broadcast info to event
* added in event functions to build out the competitors
* added in winner property in event that holds the winner object
* 

## 0.3.3
* moved schedule functions out of client and into league class
* added in function to team/client to load box scores for a roster for a season
* added in call from event to pull competition data
* added in event call to build out odds
* added in headshot to player class
* added in drives and plays data (nfl)
* added in pbp for basketball leagues
* added function to image class to download image
* changed some of the clients vars to properties
* made sure to_dicts were across the classes where they are needed
* made sure validate_json decorator was acorss classes as needed
* tech debt
  * moved from calling lookup api function to pulling from espn client
  * removed v import to all classes and put it in client
  * teams/league are client properties now
  * client is now property across classes
  * league has properties betting futures and schedules now + league leaders
  * added stats/stats_log as properties to athlete/player
  * team class has betting and rosters/ stats/coaches and records as properties now
  * made lots of ids properties
* added in pass thru so that you can load odds or play by play when loading schedule
* 

## 0.3.2
* added in epl / soccer
* added in pulling betting records for a season for teams/ teams in a league
* fixed pulling team stats
* removed client functions that are now found within other classes. i.e. betting calls are available in teams
* fixed some functions to use futures, this probably wont improve much performance but if a call hangs it could help
* added func to load futures (betting) for league class for a season
* removed get_team_info call from client
  * all this data is in the .teams once the client loads
* removed betting calls from client as the data is in classes teams and league now
* added in call for league leaders for a season in league class
* removed get_league_info call from client as all the data is in the league variable once client is loaded
* added functions to client to search teams rosters for a given season for a player
* added in auto load for rosters for given season for both betting futures and league leaders to reduce calls to api
* 

## 0.3.1
* added function to client/team to pull a seasons roster
* adding in tests and fixed some of the long running tests
* added in vehicle class to pull current vehicles for athletse with vehicles (i.e. racing leagues)
* added in client function to pull all athletes for a season
  * big note this is a lot of calls for both american and european football
* added in client function to pull manufactures for the current year versus teams for racing leagues
* adding in class for stats for players / teams
* added in standings class to pull racing (Eventually tennis amd assume golf rankings)
* pga / golf is now available
* atp/ tennis is now available
* added function to pull a seasons results to team class / pyespn client
* added im image class and connected to team logos and venue images
* added in func to pull stats for a team/all teams of a league
* added in call for coaches

## 0.3.0
* lots of changes
  * doc strings across codebase
  * new documentation
  * classes for data returns (no more json!)
* new data sources
  * draft
  * recruiting
  * schedule
* new client functions
  * instead of calling different api calls now the client automatically loads:
    * team data on creation
    * league data on creation
    * schedule data on function call
    * draft data on function call
    * recruit data on function call

## 0.2.2
* added variable at pyespn.data.version that makes it easy to switch between versions throughout code
* added contributing
* removed old readme -> now find it at the mkdocs site this is referenced in readme
* added more league options
* added league status, unavailable ones will error if used, you can fork the repo to try those out and pr if you'd like
* added more detailed errors when creating class
* 


## 0.2.1
* readme updates
* added indy car
* added team colors func
* added team logo func
* moneyline todo
* moved to github
* added mkdocs readme
* 

## 0.2.0
* started adding exceptions when apis aren't available
  * don't expect this to be fully fleshed out until 1.0
* adding standings for racing leagues (f1/nascar right now)
* added nascar
* added wnba
* added college baseball & softball
* added mlb
* added f1
* added team class to make easier use of data in the future
* added awards api call
* added doc w/ readme
* removed old readme

## 0.1.5
* forgot init py


## 0.1.4
* refactored to class
* new documentation -> old readme is saved as old_readme.md
* 

## 0.1.3
* adding in mcbb functions
* 


## 0.1.2
* started to add in cfb functions
* fixed nfl/nba get historical stats
* fixed get all ids for nfl/nba
* added in cfb teams lookup
* added in doc for cfb functions
* added in tests for cfb functions
* *_note that cfb teams lookup still appears to be missing some teams_*

## 0.1.1
* added in nba futures -> note there is not all data for every season
* added in nfl futures

## 0.1.0

### Features
* initial nba and nfl functions to pull:
  * team info
  * betting info
  * player info
  * historical stats
  * draft info

## 0.0.1

### Features

#### NFL
* added in func to pull all athletes and ids
* added in func to pull players stats by id
  * added cli func
* added func to pull player info
  * added cli func
* added func to get teams stats for a given year
  * added cli func
* added func to pull all sports api urls
  * cli added