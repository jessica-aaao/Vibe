# Vibe
Projeto em Python para a disciplina de "Introdução à Multimídia", semestre 2020.3, do curso de Engenharia da Computação da UFPE.

A ideia do VibeBot é ser um amigo virtual, através de conversa com o usuário, ele traz uma playlist musical inspirada no humor atual da pessoa.

# Subpastas
- A pasta "VibeBOT_discord" apresenta o código fonte do nosso bot integrado com o Discord.

- A pasta "Executável(linux)" possui o arquivo executável para execução do bot em uma GUI simples.

- A pasta "Código-Fonte(chatbot-APIs-gui)" apresenta o código-fonte do bot(utilizamos a biblioteca ChatterBot), a integração com APIs (Musicovery, Spotify e Unsplash) e a interface gráfica simples que fizemos para o executável.

# Como Usar
- Executável(Linux):
    - No terminal abra a pasta "Executável(linux)": cd [path]/Vibe/Executável(linux)
    - Digite ./chat
    - Divirta-se com o nosso bot

- Discord:
    - Caso você deseja rodar o bot do discord por conta própria, será necessário um 'Client ID' e 'Client Secret' gerados ao solicitar uma aplicação no Spotify (https://developer.spotify.com/dashboard/applications). Quando estiver com ambas as keys em mãos, basta ir no código do 'spotify.py' e substituir na chamada da função "SpotifyClientCredentials".
    - Será necessário também um 'Client ID' do Unsplash, para que possa ser feito a coleta de imagens (https://unsplash.com/). Quando estiver com o 'Client ID' em mãos, substitua no arquivo "unsplash.py".
    - E por último será necessário um Token para poder conectar o bot ao discord, para isso basta ir na aba de desenvolvedores do discord e solicitar uma nova aplicação;Feito isso, vá na aba de Bot's e adicione o mesmo criado no passo anterior; Cliquem em "Revelar Token" e pronto, você está pronto pra rodar o bot por conta própria (https://discord.com/developers/applications)
