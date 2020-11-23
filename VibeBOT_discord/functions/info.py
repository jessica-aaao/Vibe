import discord
from config.setup  import bot

@bot.command() 
async def info(context):
	introducao = ["Amigo, estou aqui! Se a fase é ruim... E são tantos problemas que não tem fim... Não se esqueça que ouviu de mim... Amigo, estou aqui!",
                  "Oh, olha, um amigo!! lol",
                  "Olá, eu me chamo Vibe!! Posso te indicar músicas e imagens de acordo com o seu humor atual!! ",
                  "Quando quiser conversar é só digitar 'Olá, Vibe' ou 'Oi' (Conversa comigo ao invés de ficar aí 'talking to the moon' :grin:)",
                  "E a qualquer momento que quiser sair, só digitar 'Stop' ('Não me deixe só... Eu tenho medo do escuro...' :pleading_face: )"]
                  
	channel = message.channel
	for frase in introducao:
		await channel.send(f"{frase}")