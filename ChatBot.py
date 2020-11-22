from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
import json
import sys
from time import sleep
import requests

URL_TELEGRAM_BASE = "https://api.telegram.org/bot1459276720:AAHHFCfxQ_V2nsyc9b0kIgk6Fw1LfsqPgbc"

resposta = requests.post(URL_TELEGRAM_BASE + "/getUpdates")

resposta = resposta.json()

print(resposta)

for item in resposta['result']:
	if 'photo' in item['message']:
		print('foto encontrada')
	else:
		conteudo = {
			'chat_id': item['message'['chat']['id'],
			'text': 'você é linde',
			'reply_to_message_id':item['message']['message_id']
		}

		requests.post(URL_TELEGRAM_BASE + "/sendMessage")

	vibe = ChatBot(
	name = 'Vibe',
	read_only = False,
	storage_adapter = "chatterbot.storage.SQLStorageAdapter",
	logic_adapters = ["chatterbot.logic.BestMatch"],
	database_uri = "sqlite:///database.sqlite3"
)

#trainer = ChatterBotCorpusTrainer(vibe)

trainer = ListTrainer(vibe)

#trainer.train("chatterbot.corpus.portuguese")

data_file = open('trainer.json').read()
learn = json.loads(data_file)

for topic in learn:
	for compliment in learn[topic]:
		trainer.train(compliment)

introducao = ["Amigo, estou aqui! Se a fase é ruim... E são tantos problemas que não tem fim... Não se esqueça que ouviu de mim... Amigo, estou aqui!",
			  "Oh, olha, um amigo!! lol",
			  "Olá, eu me chamo Vibe!! Posso te indicar músicas e imagens de acordo com o seu humor atual!! ",
			  "Quando quiser conversar é só digitar 'Olá, Vibe' ou 'Oi' (Conversa comigo ao invés de ficar aí 'talking to the moon';P)",
			  "E a qualquer momento que quiser sair, só digitar 'Stop' ('Não me deixe só... Eu tenho medo do escuro...' :`[ )"]


for frase in introducao:
	print(f'\n\n{vibe.name}: ')
	
	for char in frase:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	sleep(0.5)

print("\n")

'''
#Alternativa de Introdução

for frase in introducao:
	print(f'\n{vibe.name}: {frase}\n')
	sleep(2)

'''

hasPlaylist = 0

while True:
	message = input("Eu: ")
	message = message.lower()

	if ("feliz" in message):
		message = "feliz"
		url = "link"
		hasPlaylist = 1

	if ("triste" in message):
		message = "triste" 
		url = "link"
		hasPlaylist = 1

	if ("ansios" in message):
		message = "ansiose"
		url = "link"
		hasPlaylist = 1

	if ("raiva" in message):
		message = "com raiva"
		url = "link"
		hasPlaylist = 1

	if ("estressad" in message):
		message = "estressade"
		url = "link"
		hasPlaylist = 1

	if (("nostalgic" or "nostálgic")in message):
		message = "nostalgicx"
		url = "link"
		hasPlaylist = 1

	if ("tens" in message):
		message = "tense"
		url = "link"
		hasPlaylist = 1

	if (("tranquil" or "calm")in message):
		message = "calme"
		url = "link"
		hasPlaylist = 1

	if ("relaxad" in message):
		message = "relaxade"
		url = "link"
		hasPlaylist = 1

	if ("cansad" in message):
		message = "cansade"
		url = "link"
		hasPlaylist = 1

	if (("animad" or "euforic" or "eufóric") in message):
		message = "animade"
		url = "link"
		hasPlaylist = 1

	if ("preocupad" in message):
		message = "preocupade"
		url = "link"
		hasPlaylist = 1

	if ("pensativ" in message):
		message = "pensative"
		url = "link"
		hasPlaylist = 1

	#Se a pessoa responder que quer escutar a playlist	
	if (hasPlaylist == 1 and message == "sim"):
		print(f'\n{vibe.name}: Aqui está a sua playlist \n   {url}\n')
		hasPlaylist = 0
	
	try:
		response = vibe.get_response(message)
		

		if float(response.confidence) >= 0.5:
			print(f'\n{vibe.name}: {response}\n')
			
		else:
			print(f'\n{vibe.name}:Desculpa, eu ainda não sei como responder isso!\n')

		if (message == 'stop'):
			break

		#print(f'\n{vibe.name}: {response}\n')

	except(KeyboardInterrupt, EOFError, SystemExit):
		break

conteudo = {
	'chat_id': item['message'['chat']['id'],
	'text': 'você é linde',
	'reply_to_message_id':item['message']['message_id']
}

requests.post(URL_TELEGRAM_BASE + "/sendMessage")