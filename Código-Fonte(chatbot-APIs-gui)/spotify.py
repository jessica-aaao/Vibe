#Eh preciso intalar a biblioteca primeiro
#pip install spotipy --upgrade

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import re
from pprint import pprint
import json

playlist = []

client_credentials_manager = SpotifyClientCredentials(client_id="<KEY ID>", client_secret="<KEY SECRET>")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def retSpotifyPlaylist(moodPlaylist):
	for song in moodPlaylist:
	  result = sp.search(q='artist:' + song[0] + ' track:' + song[1], type='track')
	  if result['tracks']['items']: # Verificação de existência da música no Spotify, caso não encontre passa para a próxima da lista ( Vida que segue )
	    link = result['tracks']['items'][0]['external_urls']['spotify'] # Remoção do Link da música no spotify pelo Json ( Transformado em Dict )
	    playlist.append(result['tracks']['items'][0]['external_urls']['spotify']) 
	return playlist
#for song in playlist: # Apenas para ter uma noção visual das músicas que passaram para a playlist
#  print(f'Link: {song}')