# -*- coding: utf-8 -*-
"""fase3_fine_tuning_aula1_generate-output-for-news.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B37dKt__qOdiIgKLHWTvgqo6-TQTQd3e
"""

#Conexão com o Google Drive

from google.colab import drive
drive.mount('/content/drive')

!pip install openai

import requests
import json
from openai import OpenAI
# Substitua 'your_openai_api_key' pela sua chave de API da OpenAI
client = OpenAI(api_key='*********')

import time

def summarize_news(news_file):
    # Carrega o conteúdo das notícias de um arquivo JSON
    with open(news_file, 'r') as file:
        news_data = json.load(file)
        news_contents = news_data['news_content']

    summaries = []

    for content in news_contents:
        # Define os dados para enviar para a API da GPT-3.5-turbo

        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          response_format={ "type": "json_object" },
          messages=[
            {
              "role": "system",
              "content": "Summarize this news article and return in the following JSON format containing only summary."
            },
            {
              "role": "user",
              "content": f"{content}\n###"
            }
          ],
          temperature=0.3,
          max_tokens=64,
          top_p=1
        )

        summary_text = response.choices[0].message.content.strip()
        print(summary_text)
        summaries.append({
            "story": content,
            "summary": summary_text.replace('{\n    \"summary\": \"', "")
        })
        time.spleep(25)


    # Salva os resultados em um arquivo JSON
    with open('news_summaries.json', 'w') as json_file:
        json.dump({"news_summaries": summaries}, json_file)

# Chame a função com o caminho para seu arquivo de conteúdo de notícias
summarize_news('/content/drive/MyDrive/news_contents.json')

"""A porcaria da openia não funciona pq fica ramelando as requisições😠"""

!pip install -U -q google-generativeai

import google.generativeai as genai
from google.colab import userdata

api_key = userdata.get('API_KEY')
genai.configure(api_key=api_key)

import time

generation_config = {
  "temperature": 0.5, # Esse parâmetro controla a aleatoriedade do texto gerado
  # "candidate_count": 1, # Especifica o número de tentativas independentes de geração de texto (candidatos) a serem consideradas.
  "top_p": 0.90, # Controla a distribuição de probabilidade usada para amostrar a próxima palavra.
  "top_k": 10, # Limita o tamanho do vocabulário considerado para gerar a próxima palavra
  "max_output_tokens": 64 # Define o número máximo de tokens (palavras) que o texto gerado pode ter.
}

def summarize_news(news_file):
    # Carrega o conteúdo das notícias de um arquivo JSON
    with open(news_file, 'r') as file:
        news_data = json.load(file)
        news_contents = news_data['news_content']

    summaries = []
    count = 0

    for content in news_contents:
        # Define os dados para enviar para a API do genai

        # prompt = f"Summarize this news article and return in the following JSON format containing only summary.: {content}"
        layout = '{"summary": ""}'
        prompt = f'Summarize this news and return it in the following JSON format containing just a summary ({layout}). The news: {content}'
        model_RAG = genai.GenerativeModel("gemini-1.0-pro",
                                          generation_config=generation_config)
        response = model_RAG.generate_content(prompt)

        summary_text = response.text
        print(summary_text)
        summaries.append({
            "story": content,
            "summary": summary_text.replace('{\n    \"summary\": \"', "")
        })
        count = count + 1
        if count == 5:
          break
        time.sleep(15)

    # Salva os resultados em um arquivo JSON
    with open('news_summaries.json', 'w') as json_file:
        json.dump({"news_summaries": summaries}, json_file)

# Chame a função com o caminho para seu arquivo de conteúdo de notícias
summarize_news('/content/drive/MyDrive/news_contents.json')