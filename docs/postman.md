# Verifying Endpoint in Postman
You can use postman or a tool of the like to test the api. to do this you will need to be able to 
read into the pyespn.core code to get the makeup of the api calls.

For this example we'll look at a player

## Finding API URL

if you open up the pyespn.core.players python file you can find the api call

![player_code.png](img%2Fplayer_code.png)

inside the file you can find the function that calls the player info api. you will see here the api call, with the
parameterized variables.  

![player_api.png](img%2Fplayer_api.png)

you will need to update these parts to get postman to work. within the pyespn.data.leagues python file you
can find the LEAGUE_API_MAPPING which has the keys needed to complete the api call

## Testing in Postman

if you go ahead and fill in the variables into the url and run in postman you will see a response
with the details for the given player

![postman_player.png](img%2Fpostman_player.png)
