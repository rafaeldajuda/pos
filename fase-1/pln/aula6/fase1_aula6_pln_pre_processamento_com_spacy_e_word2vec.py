# -*- coding: utf-8 -*-
"""fase1_aula6_pln_pre_processamento_com_spacy_e_word2vec.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vc_PHt6Hu2J-KRXW9n0DNJhxa6uHHMp1

Iremos utilizar a biblioteca SpaCy no lugar do NLTK e criar um modelo Word2Vec do zero sem uma base pré-treinada, assim você vai conseguir criar um classificador com o seu próprio modelo.

# SpaCy

**SpaCy** é uma biblioteca de processamento de linguagem natural (NLP) de código aberto para Python. É amplamente utilizada para construir aplicações que processam e "compreendem" textos escritos, como análise de sentimento, reconhecimento de entidades nomeadas (NER), segmentação de frases, lematização, e muito mais. SpaCy é conhecida por ser rápida, eficiente e fácil de usar.

## Características principais do spaCy

1. **Desempenho**: Projetada para ser eficiente e rápida, spaCy é capaz de processar grandes volumes de texto com rapidez, tornando-a adequada para aplicações em produção.

2. **Modelos pré-treinados**: Oferece uma série de modelos pré-treinados para várias línguas, o que facilita a implementação de tarefas comuns de NLP sem a necessidade de treinamento manual de modelos.

3. **Funcionalidades avançadas**: Suporta uma ampla gama de tarefas de NLP, incluindo:
   - Tokenização
   - POS tagging (marcação de partes do discurso)
   - Lematização
   - Reconhecimento de entidades nomeadas (NER)
   - Análise de dependência sintática
   - Vetores de palavras (word vectors)

4. **Extensibilidade**: Permite a integração com outras bibliotecas de aprendizado de máquina e NLP, como TensorFlow, PyTorch, e scikit-learn, facilitando a criação de pipelines complexas de processamento de texto.

5. **Comunidade e suporte**: Tem uma comunidade ativa e uma boa documentação, com tutoriais e exemplos que ajudam novos usuários a começar rapidamente.

## Resumo

SpaCy é uma poderosa biblioteca de NLP que oferece ferramentas eficientes e robustas para processamento de texto, com suporte a modelos pré-treinados e integração com outras tecnologias de aprendizado de máquina, tornando-a uma escolha popular entre desenvolvedores e pesquisadores.

# Inicio
"""

import pandas as pd

artigo_treino = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Word2Vec/treino.csv')
artigo_teste = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Word2Vec/teste.csv')

"""## Instalação do spacy

https://spacy.io/usage

pip install -U pip setuptools wheel (obs: já instalado no colab)<br/>
pip install -U spacy (obs: já instalado no colab)<br/>
python -m spacy download pt_core_news_sm (obs: pacote em portugues)
"""

!python -m spacy download pt_core_news_sm

"""OBS:  após baixar o pacote irá ter a seguinte mesangem, "Restart to reload dependencie". Para fazer isso ir em "Ambiente de execução" -> "Reiniciar sessão"
"""

import spacy
nlp = spacy.load('pt_core_news_sm')

texto = 'Adoro a cidade de caldas novas!'
doc = nlp(texto)

type(doc)

doc.ents

doc[1].is_stop

doc[0].is_stop

doc[1].is_alpha

def trata_textos(doc):
  tokens_validos = []

  for token in doc:
    e_valido = not token.is_stop and token.is_alpha
    if e_valido:
      tokens_validos.append(token.text)

  if len(tokens_validos) > 2:
    return " ".join(tokens_validos)

texto = 'Adoro a 23424342 #$#$#$#$#$ cidade de caldas novas!'
doc = nlp(texto)
trata_textos(doc)

textos_para_tratamento = (titulos.lower() for titulos in artigo_treino.title)

# batch_size -> tamanho do bloco de processamento
# n_process -> quantidade de núcleos do processador
textos_tratados = [trata_textos(doc) for doc in nlp.pipe(textos_para_tratamento,
                                                         batch_size=1000,
                                                         n_process=-1)]

titulos_tratados = pd.DataFrame({'titulo': textos_tratados})
titulos_tratados.head()

"""## CBOW"""

from gensim.models import Word2Vec

# sg - 0 -> cbow - 1 -> skipgram
# window - quantidade de palavras antes e depois da palavra central
# vector_size - tamanho do vetor a ser gerado
# min_count - numero de vezes que uma palavra deve aparecer
# alpha - taxa de aprendizagem da rede neural
# min_alpha - mínimo de convergência da rede neural
w2v_modelo = Word2Vec(sg=0,
                      window=2,
                      vector_size=300,
                      min_count=5,
                      alpha=0.03,
                      min_alpha=0.007)

print(len(titulos_tratados))

titulos_tratados = titulos_tratados.dropna().drop_duplicates()

print(len(titulos_tratados))

lista_lista_tokens = [titulo.split(" ") for titulo in titulos_tratados.titulo]

w2v_modelo.build_vocab(lista_lista_tokens)

"""## Treinando o modelo"""

# lista todas as propriedas e métodos
dir(w2v_modelo)

# quantidade de corpus textual
w2v_modelo.corpus_count

from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec

# iniciando a chamada callback
class callback(CallbackAny2Vec):
  def __init__(self):
    self.epoch = 0

  def on_epoch_end(self, model):
    loss = model.get_latest_training_loss()
    if self.epoch == 0:
      print('Loss após a época {}:{}'.format(self.epoch, loss))
    else:
      print('Loss após a época {}:{}'.format(self.epoch, loss - self.loss_previus_step))
    self.epoch += 1
    self.loss_previus_step = loss

w2v_modelo.train(lista_lista_tokens,
                 total_examples=w2v_modelo.corpus_count,
                 epochs=30,
                 compute_loss=True,
                 callbacks=[callback()])

w2v_modelo.wv.most_similar('google')

"""## Skip Gram"""

# o skip gram tabralha melhor com mais dados, então nesse caso seria melhor aumentar o valor do window de 2 para 5
w2v_modelo_sg = Word2Vec(sg=1,
                      window=5,
                      vector_size=300,
                      min_count=5,
                      alpha=0.03,
                      min_alpha=0.007)

w2v_modelo_sg.build_vocab(lista_lista_tokens)

w2v_modelo_sg.train(lista_lista_tokens,
                 total_examples=w2v_modelo.corpus_count,
                 epochs=30,
                 compute_loss=True,
                 callbacks=[callback()])

w2v_modelo_sg.wv.most_similar('google')

"""# Exportando modelos"""

w2v_modelo.wv.save_word2vec_format('/content/drive/MyDrive/Colab Notebooks/Word2Vec/modelo_cbow.txt', binary=False)
w2v_modelo_sg.wv.save_word2vec_format('/content/drive/MyDrive/Colab Notebooks/Word2Vec/modelo_sg.txt', binary=False)

"""# Criando o classificador com o nosso modelo"""

import numpy as np

def combinacao_de_vetores_por_soma(palavras_numeros, modelo):
  vetor_resultante = np.zeros(300)
  for pn in palavras_numeros:
    try:
      vetor_resultante =+ modelo.wv.get_vector(pn)
    except KeyError:
      pass
  return vetor_resultante

def tokenizador(texto):
  tokens_validos = []
  doc = nlp(texto)

  for token in doc:
    e_valido = not token.is_stop and token.is_alpha
    if e_valido:
      tokens_validos.append(token.text.lower())

  return tokens_validos

def matriz_vetores(textos, modelo):
  x = len(textos)
  y = 300
  matriz = np.zeros((x, y))

  for i in range(x):
    palavras = tokenizador(textos.iloc[i])
    matriz[i] = combinacao_de_vetores_por_soma(palavras, modelo)
  return matriz

matriz_vetores_treino_cbow = matriz_vetores(artigo_treino.title, w2v_modelo)
matriz_vetores_teste_cbow = matriz_vetores(artigo_teste.title, w2v_modelo)

matriz_vetores_treino_sg = matriz_vetores(artigo_treino.title, w2v_modelo_sg)
matriz_vetores_teste_sg = matriz_vetores(artigo_teste.title, w2v_modelo_sg)

print(matriz_vetores_treino_cbow.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def classificador(x_treino, y_treino, x_teste, y_teste):
  RL = LogisticRegression(max_iter=800)
  RL.fit(x_treino, y_treino)
  categorias = RL.predict(x_teste)
  resultados = classification_report(y_teste, categorias)
  print(resultados)
  return RL

RL_cbow = classificador(matriz_vetores_treino_cbow,
                        artigo_treino.category,
                        matriz_vetores_teste_cbow,
                        artigo_teste.category)

RL_sg = classificador(matriz_vetores_treino_sg,
                        artigo_treino.category,
                        matriz_vetores_teste_sg,
                        artigo_teste.category)