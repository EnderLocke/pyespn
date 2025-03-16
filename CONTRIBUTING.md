# How to Contribute
This section is still a work in progress

## Fork Repo


## Adding a League
to add a league to pyespn there are a few files that are needed. 

### pyespn.data
there are three different files that are needed

#### league teams lookup file
this is located at pyespn.data.files and has the naming convention of [league_abbv]_teams_lookup

this file also needs to be loaded in the data_import.py file so it can be included in later code

#### teams.py
the LEAGUE_TEAMS_MAPPING needs to be updated to the correct variable for the league/team lookup var from the data_import python file


#### leagues.py
in this file you need to either map the league/sport endpoint within LEAGUE_API_MAPPING if it is not already available
and if it is and unavailable you need to make it available for the object to build correctly


## Adding Tests



