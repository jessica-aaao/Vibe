from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from unsplash import retImages
from spotify import retSpotifyPlaylist
from musicovery import retPlaylist
import json
import sys
from time import sleep
from tkinter import *
from tkinter import scrolledtext
import webbrowser
import urllib.parse
from PIL import Image, ImageTk
from io import BytesIO
from chatterbot import preprocessors
import sqlalchemy.sql.default_comparator
import sqlalchemy.ext.baked
import encodings

global hasPlaylist
global tag

def introducao():
	global conversation

	texto = ["Amigo, estou aqui! Se a fase é ruim... E são tantos problemas que não tem fim... Não se esqueça que ouviu de mim... Amigo, estou aqui!\n\n",
			  "Oh, olha, um amigo!! lol\n\n",
			  "Olá, eu me chamo Vibe!! Posso te indicar músicas e imagens de acordo com o seu humor atual!!\n\n",
			  "Quando quiser conversar é só digitar 'Olá, Vibe' ou 'Oi' (Conversa comigo ao invés de ficar aí 'talking to the moon';P)\n\n",
			]

	for frase in texto:
		conversation['state'] = 'normal'
		conversation.insert(END, str(vibe.name) + ": " + frase)
		conversation.yview(END)
		conversation['state'] = 'disabled'


def send_message():
	global conversation

	message = messageWindow.get("1.0", END)
	message = message.lower()
	
	conversation['state'] = 'normal'
	conversation.insert(END, "Eu: " + str(message) +"\n")	
	conversation.yview(END)
	conversation['state'] = 'disabled'
	
	messageWindow.delete("1.0", END)

	get_answer(message=str(message))


def get_answer(message:str):
	global hasPlaylist
	global vibe
	global conversation
	global tag

	if ("feliz" in message):
		tag = message = "feliz"
		hasPlaylist = 1

	if ("triste" in message):
		tag = message = "triste" 
		hasPlaylist = 1

	if ("ansios" in message):
		tag = message = "ansiose"
		hasPlaylist = 1

	if ("raiva" in message):
		tag = message = "com raiva"
		hasPlaylist = 1

	if ("estressad" in message):
		tag = message = "estressade"
		hasPlaylist = 1

	if (("nostalgic" or "nostálgic")in message):
		tag = message = "nostalgicx"
		hasPlaylist = 1

	if ("tens" in message):
		tag = message = "tense"
		hasPlaylist = 1

	if (("tranquil" in message) or ("calm" in message)):
		tag = message = "calme"
		hasPlaylist = 1

	if ("relaxad" in message):
		tag = message = "relaxade"
		hasPlaylist = 1

	if ("cansad" in message):
		tag = message = "cansade"
		hasPlaylist = 1

	if (("animad" or "euforic" or "eufóric") in message):
		tag = message = "animade"
		hasPlaylist = 1

	if ("preocupad" in message):
		tag = message = "preocupade"
		hasPlaylist = 1

	if ("pensativ" in message):
		tag = message = "pensative"
		hasPlaylist = 1

	#Se a pessoa responder que quer escutar a playlist	
	if (hasPlaylist == 1 and  "sim" in message):
		response = "Opa! Já estou te enviando!\n"

		conversation['state'] = 'normal'
		conversation.insert(END, str(vibe.name) + ": " + str(response)+"\n\n")
		conversation.yview(END)
		conversation['state'] = 'disabled'
		
		hasPlaylist = 0

		playlist_labels = retPlaylist(tag)

		playlist_link = retSpotifyPlaylist(playlist_labels)

		mood_image = retImages(tag)

		raw_data = urllib.request.urlopen(mood_image[0]).read()
		open_data = Image.open(BytesIO(raw_data))
		
		playlist_screen = Toplevel()
		playlist_screen.title("Playlist - " + tag.capitalize())
		playlist_screen.geometry("400x500")
		playlist_screen.resizable(width=FALSE, height=FALSE)

		window = Canvas(playlist_screen)
		
		scroll=Scrollbar(playlist_screen, orient=VERTICAL, command=window.yview)

		frame = Frame(window)

		image = ImageTk.PhotoImage(open_data)
		cover = Label(frame, image=image)
		cover.image = image
		cover.pack(side=TOP)


		button_row=0
		
		for song, link in zip(playlist_labels, playlist_link):
			song_button = Button(frame, text=str(song[0])+"-"+str(song[1]), command=lambda:webbrowser.open(link))
			song_button.pack(side=TOP, fill=X)

		window.create_window(0,0,anchor=NW, window=frame)

		window.update_idletasks()

		window.configure(scrollregion=window.bbox(ALL),
						 yscrollcommand=scroll.set)

		window.pack(fill=BOTH, expand=TRUE, side=LEFT)

		scroll.pack(side=RIGHT, fill=Y)
		
	else:
		try:
			response = vibe.get_response(message)

			if float(response.confidence) < 0.5:
				response = "Desculpa, eu ainda não sei como responder isso!"
			
			conversation['state'] = 'normal'
			conversation.insert(END, str(vibe.name) + ": " + str(response)+"\n\n")
			conversation.yview(END)
			conversation['state'] = 'disabled'
			
		except(KeyboardInterrupt, EOFError, SystemExit):
			print("Erro: Não foi possível obter reposta")









#Start

root = Tk()

vibe = ChatBot(
	name = 'Vibe',
	read_only = False,
	storage_adapter = "chatterbot.storage.SQLStorageAdapter",
	logic_adapters = ["chatterbot.logic.BestMatch"],
	database_uri = "sqlite:///database.sqlite3"
)

trainer = ListTrainer(vibe)

data_file = open('Bot.json').read()
learn = json.loads(data_file)

for topic in learn:
	for compliment in learn[topic]:
		trainer.train(compliment)
		
root.title("Vibe")
root.geometry("500x500")
root.resizable(width=FALSE, height=FALSE)

chatWindow = Text(root, bd=1, width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6.0, y=6.0, height=385, width=370)

conversation = scrolledtext.ScrolledText(chatWindow, wrap=WORD)
conversation.yview(END)

conversation.pack(fill=X, side=LEFT)

test= Button(chatWindow, text="ok")
test.pack()

messageWindow = Text(root, bd=0, bg="white",width="30", height="4", font=("Arial", 15), foreground="black")
messageWindow.place(x=6, y=400, height=88, width=260)

messageWindow.focus()

send_button= Button(root, text="Send", height=5, bd=0, bg="#0080ff", command=send_message, activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
send_button.place(x=270, y=400, height=88, width=120)

hasPlaylist = 0

introducao()

root.mainloop()