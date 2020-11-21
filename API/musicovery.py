import subprocess
import json

moodPlaylist = []
characters = ['/', "\\", '?', "'", '&', '!', '@', '#', '%', '$', '*', '(', ')', '.', ',', '-', '+', ' ;', ':']
moodMap = { # Mapeando a entrada de humor do Chatterbot para um humor do Musicovery
    "raiva": "angry",
    "estressado": "revolted",
    "nostalgico": "nostalgic",
    "tenso": "tense",
    "tranquilo": "soft",
    "calmo": "calm",
    "preocupado": "worried",
    "ansioso": "tormented",
    "animado": "energetic",
    "euforico": "euphorical",
    "cansado": "going%20to%20sleep",
    "relaxado": "chillout",
    "triste": "sad",
    "feliz": "happy",
    "pensativo": "meditation"
}

tag = "cansado" # Mood que será enviado através do chatterbot

results = subprocess.check_output(f"curl 'http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag={moodMap[tag]}'", shell=True)
data = json.loads(results)

if not data["tracks"]:
  print("Tag inexistente") # Mood inexistente para o Musicovery
else:
  for song in data["tracks"]["track"]:
    for char in characters: # Tratamento de remoção de alguns caracteres que estavam interferindo na busca da música
      song["artist_display_name"] = song["artist_display_name"].replace(char, " ")
      song["title"] = song["title"].replace(char, " ")
    moodPlaylist.append((song["artist_display_name"],song["title"]))

for song in moodPlaylist: # Apenas para ter uma noção visual das músicas que foram selecionadas pelo Musicovery
  print(song[0] + " - " + song[1])