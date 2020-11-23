import requests
import subprocess
import json

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

def retImages(tag):
    results = subprocess.check_output(f"curl 'https://api.unsplash.com/search/photos?client_id=<client_id>&page=1&query={imageMap[moodMap[tag]]}'", shell=True)
    #results = requests.get(f"https://api.unsplash.com/search/photos?client_id=<client_id>&page=1&query={imageMap[moodMap[tag]]}")
    data = json.loads(results) # Conversão de json para Dict de Python
    
    for image in data['results']:
      images.append(image['urls']['small']) # Coleta do link das imagens em tamanho "regular"
    return images
#for image in images: # Apenas para ter uma noção visual das imagens que foram selecionadas
#  print(image)