import discord
from config.setup  import bot

@bot.command() 
async def help(context, command = None):
	if command != None:
		if command == 'ping':
			await context.send('Response time of the bot')
		else:
			await context.send('Command not found in the database')
			return
	else:
		await context.send('$>help and $>ping')