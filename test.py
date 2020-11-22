import requests

URL_TELEGRAM_BASE = "https://api.telegram.org/bot1459276720:AAHHFCfxQ_V2nsyc9b0kIgk6Fw1LfsqPgbc"

resposta = requests.post(URL_TELEGRAM_BASE + "/getUpdates")

resposta = resposta.json()

print(resposta)

for item in resposta['result']:
	if 'photo' in item['message']:
		print('foto encontrada')
	else:
		conteudo = [
			'chat_id': item['message']['chat']['id'],
			'text': 'você é linde',
			'reply_to_message_id': item['message']['message_id']
            ]

		requests.post(URL_TELEGRAM_BASE + "/sendMessage")
		print('texto encontrado')
