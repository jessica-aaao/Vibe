import random
import discord
from config.setup  import bot
from .musicovery import retPlaylist
from .unsplash import retImages
from .spotify import retSpotifyPlaylist

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

@bot.command()
async def test(context, mood = None):
	if not mood:
		await context.send("Por favor insira seu humor")
		return
	try:
		mapped = moodMap[mood]
	except KeyError:
		await context.send("Humor não reconhecido na tabela")
		return
	await context.send("Aguarde enquanto montamos sua playlist :)")
	spotifyPlaylist = retSpotifyPlaylist(retPlaylist(mapped))
	embed = discord.Embed(title=mood + " Playlist", description=f"Solicitada por {context.message.author.mention}", color=0x6A5ACD)
	embed.set_image(url=random.choice(retImages(mapped)))
	for song in spotifyPlaylist:
		embed.add_field(name = song[0] + " - " + song[1], value = song[2], inline = False)
	await context.send(embed=embed)
	spotifyPlaylist = [ ]
