# -*- coding: utf-8 -*-
"""fase3_fine_tuning_aula2_1_entendendo-llms.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sNDhDvEnl94SW1SNgDJQju-aZnZtzd3S
"""

!pip install spacy
!python -m spacy download en_core_web_md

import spacy

# Carregar o modelo pré-treinado do spaCy
nlp = spacy.load('en_core_web_md')

def tokenize_sentence(sentence):
    doc = nlp(sentence)
    return [token.text for token in doc]

def generate_embeddings(sentence):
    doc = nlp(sentence)
    return [token.vector for token in doc]

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Exemplo de uso
sentence = "Let's generate the embeddings for this sentence."

# Tokenizar a frase
tokens = tokenize_sentence(sentence)
print("Tokens:", tokens)

# Gerar embeddings
embeddings = generate_embeddings(sentence)

# Mostrar a matriz de embeddings
print("Embedding Matrix:")
print_matrix(embeddings)