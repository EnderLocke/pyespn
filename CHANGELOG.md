# Changelog

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
* 

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