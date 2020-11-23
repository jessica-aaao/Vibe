import requests
import subprocess
import json


def retPlaylist(tag):
  characters = ['/', "\\", '?', "'", '&', '!', '@', '#', '%', '$', '*', '(', ')', '.', ',', '-', '+', ' ;', ':']
  moodPlaylist = []
  #results = subprocess.check_output(f"curl 'http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag={moodMap[tag]}'", shell=True)
  results = requests.get(f"http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag={tag}")
  data = results.json()

  if not data["tracks"]:
    print("Tag inexistente") # Mood inexistente para o Musicovery
  else:
    for song in data["tracks"]["track"]:
      for char in characters: # Tratamento de remoção de alguns caracteres que estavam interferindo na busca da música
        song["artist_display_name"] = song["artist_display_name"].replace(char, " ")
        song["title"] = song["title"].replace(char, " ")
      moodPlaylist.append((song["artist_display_name"],song["title"]))
  return moodPlaylist