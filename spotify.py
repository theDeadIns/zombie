# -*- coding: utf-8 -*-
import credentials
import json
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print(spotify.audio_analysis(track['id']))
    print()


# print(spotify.new_releases(limit = 5))