import credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import datetime


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

with open("playlis_ids.json") as ids:
    playlist_ids = json.load(ids)


for playlist_id in playlist_ids:
    try:
        playlist = sp.playlist(playlist_id)
        playlist_name = playlist['name']
        tracks = sp.playlist_tracks(playlist_id)
        tracks = tracks['items']
        fecha = str(datetime.datetime.now().date())
        play_dict = {"playlist_name": playlist_name, "playlist_id": playlist_id, "tracks": tracks, "date": fecha}
        # for i,j in enumerate(play_dict['tracks']):
        #     print (f" {i} {j['track']['name']} {j['track']['id']}")
        try:
            path = os.path.join(f"Countries/")
            with open(f"{path}{play_dict['playlist_name']}_tracks.json", "w+") as json_file:
                json.dump(play_dict, json_file)
        except FileNotFoundError:
            os.mkdir(f"Countries")
            path = os.path.join("Countries/")
            with open(f"{path}{play_dict['playlist_name']}_tracks.json", "w+") as json_file:
                json.dump(play_dict, json_file)
    except Exception as e:
        print(f'{e} has occured')