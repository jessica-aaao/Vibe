import subprocess
from spotify import playlist
from musicovery import moodMap, tag
import json

images = []
imageMap = { # Mapeando o humor do Musicovery para um estilo de imagens
    "angry": "mad",
    "revolted": "riot",
    "nostalgic": "nostalgic",
    "tense": "stress",
    "soft": "soft",
    "calm": "calm",
    "worried": "stress",
    "tormented": "anxiety",
    "energetic": "energetic",
    "euphorical": "carefree",
    "going%20to%20sleep": "relaxing",
    "chillout": "chillout",
    "sad": "sad",
    "happy": "happy",
    "meditation": "thoughtful-meditation"
}

results = subprocess.check_output(f"curl 'https://api.unsplash.com/search/photos?client_id=<KEY_USER_ID>&page=1&query={imageMap[moodMap[tag]]}'", shell=True)
data = json.loads(results) # Conversão de json para Dict de Python

for image in data['results']:
  images.append(image['urls']['regular']) # Coleta do link das imagens em tamanho "regular"

for image in images: # Apenas para ter uma noção visual das imagens que foram selecionadas
  print(image)