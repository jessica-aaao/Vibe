import discord
from discord.ext import commands

__prefix__ = '.'
__token__ = '<TOKEN_DISCORD>'

bot = commands.Bot(command_prefix = __prefix__)
bot.remove_command("help")