
# Exemplo básico: Coletar os títulos de notícias de um site. Vamos começar com um exemplo simples: extrair manchetes do site da Mobi.

import requests
from bs4 import BeautifulSoup

url = 'https://www.mobibrasil.com.br/'


resposta = requests.get(url) # pega o HTML da página.

soup = BeautifulSoup(resposta.text, 'html.parser') # transforma esse HTML em uma estrutura navegável.

titulos = soup.find_all('a', class_='feed-post-link')


