import requests
import subprocess
import json


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
    images = []
    results = requests.get(f"https://api.unsplash.com/search/photos?client_id=<KEY_CLIENT_ID>&page=1&query={imageMap[tag]}")
    data = results.json()
    #data = json.loads(results) # Conversão de json para Dict de Python
    
    for image in data['results']:
      images.append(image['urls']['regular']) # Coleta do link das imagens em tamanho "regular"
    return images