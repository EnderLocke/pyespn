# Exceptions using PYESPN
Custom Exceptions thrown by PYESPN package

## LeagueNotSupportedError
This error is raised when trying to access an api endpoint that does not exist for 
a given league or trying to create a PYESPN object without a proper league abbreviation 

## LeagueNotAvailableError
The league you have used is within the espn api but has not been developed within pyespn at this point

## InvalidLeagueError
The league you have used is not a valid league abbreviation within pyespn

## API400Error
This error is given when the espn api gives a 400 error, this could be many different things but it 
could just mean the endpoint is not available for the current league


