import requests
import subprocess
import json

moodPlaylist = []
characters = ['/', "\\", '?', "'", '&', '!', '@', '#', '%', '$', '*', '(', ')', '.', ',', '-', '+', ' ;', ':']
moodMap = { # Mapeando a entrada de humor do Chatterbot para um humor do Musicovery
    "com raiva": "angry",
    "estressade": "revolted",
    "nostalgicx": "nostalgic",
    "tense": "tense",
    "tranquil": "soft",
    "calme": "calm",
    "preocupade": "worried",
    "ansiose": "tormented",
    "animade": "energetic",
    "euforic": "euphorical",
    "cansade": "going%20to%20sleep",
    "relaxade": "chillout",
    "triste": "sad",
    "feliz": "happy",
    "pensative": "meditation"
}


def retPlaylist(tag):
  #results = subprocess.check_output(f"curl 'http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag={moodMap[tag]}'", shell=True)
  results = requests.get(f"http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag={moodMap[tag]}")
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

#for song in moodPlaylist: # Apenas para ter uma noção visual das músicas que foram selecionadas pelo Musicovery
#  print(song[0] + " - " + song[1])