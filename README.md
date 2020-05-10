# Spotify Analisis

## Authors
- Eduardo Manuel Ceja Cruz lalitoceja@gmaill.com
- Nikolai García Chkourak nikolai.garcia.98@gmail.com

## License:
GNU General Public License version 3

 # Instructions
1. First, you need to [install the spoitpy library](https://github.com/plamere/spotipy)

> 1.1 You can do this by simply running `pip install spotipy`

2. Then, you need to get the credential for your account

> 2.1 Go to the dashboard in the [spotify developer page](https://developer.spotify.com/dashboard/)

> 2.2 Log in with your spotify account.

> 2.3 Create a new app by clicking "My New App". If you don't know yet for what purpose you want for your app, tick the "I don't know" option. Give it a title and a description and tick all the boxes in the next page.
![creation of the app](https://github.com/theDeadIns/zombie/blob/master/resources/App%20creation.png)

> 2.4 On the left side you can find your "Client ID" and your "Client Secret". Sometimes the "spotipy" script requiers a redirect page. For that, go to "Edit Settings" and set "https://www.google.com/" (or any other generic and stable page) as your Redirect URI.
![Credentials](https://github.com/theDeadIns/zombie/blob/master/resources/Credentials.png)

3. You can now run the script


# Introduction:

 This project will atempt to give an analisis of songs from Spotify using a  library that implements the [Spotify API](https://developer.spotify.com/documentation/web-api/) into python called [Spotipy](https://github.com/plamere/spotipy). Using this information, we will try to build a playlist of the trends per country per day and then try to implement other features.


# Implementation:
The implementation can be found in the [spotify.py](https://github.com/theDeadIns/zombie/blob/master/spotify.py) file above

 # Testing Results:

 So far, we have managed to obtain as many as 20 songs per execution in json format however, we still need to determine the frecuency in witch we are going to be running the scrpit, given that the trends do not change that frecuently (we are still testing this).

 # Resources:
## Data stream:
- Spotify
## Data processing:
- Python
- Pandas
- Bokeh

## Data storage:
- json files
- MySQL
