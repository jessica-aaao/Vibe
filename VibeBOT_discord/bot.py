from config.setup  import __token__, __prefix__, bot
from functions import info
from event import on_ready, on_member_join, on_member_remove, on_message

bot.run(__token__)