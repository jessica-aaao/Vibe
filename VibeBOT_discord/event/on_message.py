# -- coding: utf-8 --
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from functions.musicovery import retPlaylist
from functions.spotify import retSpotifyPlaylist
from functions.unsplash import retImages
from event.on_ready import vibe
import json
import sys
import discord
from config.setup  import bot
import random

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

@bot.event # Chatterbot
async def on_message(message):
	if message.author == bot.user:
		return
	#await message.channel.send("Hello there!")
	author = message.author.mention

	'''
	trainer = ListTrainer(vibe)

	data_file = open('event/Bot.json').read()
	learn = json.loads(data_file)
	for topic in learn:
		for compliment in learn[topic]:
			trainer.train(compliment)
	'''
	'''
	introducao = ["Amigo, estou aqui! Se a fase é ruim... E são tantos problemas que não tem fim... Não se esqueça que ouviu de mim... Amigo, estou aqui!",
                  "Oh, olha, um amigo!! lol",
                  "Olá, eu me chamo Vibe!! Posso te indicar músicas e imagens de acordo com o seu humor atual!! ",
                  "Quando quiser conversar é só digitar 'Olá, Vibe' ou 'Oi' (Conversa comigo ao invés de ficar aí 'talking to the moon' :grin:)",
                  "E a qualquer momento que quiser sair, só digitar 'Stop' ('Não me deixe só... Eu tenho medo do escuro...' :pleading_face: )"]

	#Alternativa de Introdução ( CONVERTER )
	print("1")
	for frase in introducao:
		print("2")
		await channel.send(f"{frase}")
	'''
	channel = message.channel
	dm = message.author
	hasPlaylist = 0

	print("3")
    
#	while True:
	#message = await bot.wait_for('message')
	message = message.content.lower()
	print("4")
	if ("feliz" in message):
		print("5")
		tag, message = "feliz", "feliz"
		hasPlaylist = 1

	if ("triste" in message):
		tag, message = "triste", "triste" 
		hasPlaylist = 1

	if ("ansios" in message):
		tag, message = "ansiose", "ansiose"
		hasPlaylist = 1

	if ("raiva" in message):
		tag, message = "com raiva", "com raiva"
		hasPlaylist = 1

	if ("estressad" in message):
		tag, message = "estressade", "estressade"
		hasPlaylist = 1

	if ("nostalgic" in message):
		tag, message = "nostalgicx", "nostalgicx"
		hasPlaylist = 1

	if ("nostálgic" in message):
		tag, message = "nostalgicx", "nostalgicx"
		hasPlaylist = 1

	if ("tens" in message):
		tag, message = "tense", "tense"
		hasPlaylist = 1

	if ("tranquil" in message):
		tag, message = "calme", "calme"
		hasPlaylist = 1

	if ("calm" in message):
		tag, message = "calme", "calme"
		hasPlaylist = 1

	if ("relaxad" in message):
		tag, message = "relaxade", "relaxade"
		hasPlaylist = 1

	if ("cansad" in message):
		tag, message = "cansade", "cansade"
		hasPlaylist = 1

	if ("animad" in message):
		tag, message = "animade", "animade"
		hasPlaylist = 1

	if ("euforic" in message):
		tag, message = "animade", "animade"
		hasPlaylist = 1

	if ("eufóric" in message):
		tag, message = "animade", "animade"
		hasPlaylist = 1

	if ("preocupad" in message):
		tag, message = "preocupade", "preocupade"
		hasPlaylist = 1

	if ("pensativ" in message):
		tag, message = "pensative", "pensative"
		hasPlaylist = 1

	#Se a pessoa responder que quer escutar a playlist ( CONVERTER PRA DISC )	
	if hasPlaylist == 1: #and message == "sim"):
		print("6")
		await dm.send("Aguarde enquanto montamos sua playlist :)")
		mapped = moodMap[tag]
		print("7")
		spotifyPlaylist = retSpotifyPlaylist(retPlaylist(mapped))
		embed = discord.Embed(title= "Playlist", description=f"Solicitada por {author}", color=0x6A5ACD)
		embed.set_image(url=random.choice(retImages(mapped)))
		for song in spotifyPlaylist:
			embed.add_field(name = song[0] + " - " + song[1], value = song[2], inline = False)
		await dm.send(embed=embed)

		hasPlaylist = 0
	else:
		print("9")
		try:
			print("8")
			response = vibe.get_response(message)
			if float(response.confidence) >= 0.5:
				await dm.send(f"{response}")
				print(f'\n{response}\n')			
			else:
				await dm.send(f"Desculpa, eu ainda não sei como responder isso!")
				#print(f'\n{vibe.name}:Desculpa, eu ainda não sei como responder isso!\n')
			#if (message == 'stop'):
			#	pass
		except(KeyboardInterrupt, EOFError, SystemExit):
			pass