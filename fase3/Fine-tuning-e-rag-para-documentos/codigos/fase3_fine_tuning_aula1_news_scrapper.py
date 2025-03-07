# -*- coding: utf-8 -*-
"""fase3_fine_tuning_aula1_news-scrapper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XCbcz5eBbgketjCYfbTt3cq5EAhaqdPI
"""

#Conexão com o Google Drive

from google.colab import drive
drive.mount('/content/drive')

#Importar bibliotecas
import requests
from bs4 import BeautifulSoup

#Definindo a função que retornará os links

def scrape_cnn_links(url):
    response = requests.get(url)

    # Se a request tiver retorno com sucesso
    if response.status_code == 200:
        # Parsing do conteúdo da página
        soup = BeautifulSoup(response.text, 'html.parser')

        valid_links = []

        # Encontrar os links de notícias
        for a in soup.find_all('a', href=True):
            href = a['href']
            # Checagem se o link encontrado é um documento HTML
            if href.startswith('/') and href.endswith('.html'):
                # Concatenar com a URL padrão do site
                full_link = f"https://www.cnn.com{href}"
                valid_links.append(full_link)
            else: pass

        return valid_links
    else:
        return f"Falha ao extrair o conteúdo da notícia: {response.status_code}"

# Definindo a URL padrão
url = "https://edition.cnn.com/world"

# Chama a função de scrap dos dados e salva as URLs em um arquivo
links = scrape_cnn_links(url)
with open('CNN_Links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')



