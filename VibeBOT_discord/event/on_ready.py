# -- coding: utf-8 --
import discord
from config.setup  import bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json

vibe = ChatBot(
	name = 'Vibe',
	read_only = False,
	storage_adapter = "chatterbot.storage.SQLStorageAdapter",
	logic_adapters = ["chatterbot.logic.BestMatch"],
	database_uri = "sqlite:///database.sqlite3"
)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name='Escreva .info para mais'))
	print('Vibe Chatterbot is Ready')


	trainer = ListTrainer(vibe)

	data_file = open('event/Bot.json').read()
	with open('event/Bot.json', encoding='utf-8') as fh:
		learn = json.load(fh)
	#learn = json.loads(data_file)
	'''
	for topic in learn:
		for compliment in learn[topic]:
			trainer.train(compliment)
	'''
