# -*- coding: utf-8 -*-
"""fase3_ia_aula2_12_criando_um_modelo_com_embeddings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ghDKqDRwJkpOLtBy_6AawQK8GdjzuL4

# Embeddings

A ideia por de trás de Word Embeddings é que é possível representar uma palavra usando um vetor compacto e denso que preserve sua conotação, ou seja, seu **significado inferido a partir de um contexto**.

A técnica que deu início aos Words Embeddings foi divulgada num paper de 2013, do Google. Essa técnica recebeu o nome de Word2Vec e vamos entender seu funcionamento agora.

## Word2Vec

O que significa dizer que uma representação textual deveria capturar a similaridade distribucional entre palavras? Vamos analisar alguns exemplos. Se eu fornecer a palavra “Brasil”, outras palavras com similaridade distribucional a essa poderiam ser outros países (“Chile”, “Uruguai”, etc.). Se eu forneço a palavra “Bela”, poderia pensar em sinônimos ou antônimos como palavras com similaridade distribucional. Ou seja, o que estamos tentando capturar são palavras que possuem alta probabilidade de aparecerem num mesmo contexto.

Ao aprender tais relações semânticas, o Word2Vec garante que a representação aprendida possui baixa dimensionalidade (palavras são representadas por vetores de 50-1000 dimensões) e são densas (a maioria dos valores dos vetores são diferentes de zero). Tais representações tornam as tarefas de modelos de machine learning mais eficientes.

Antes de entrarmos nos detalhes de como o Word2Vec consegue capturar tais relações, vamos construir uma intuição de como ele funciona. Dado um corpus de texto, o objetivo é aprender embeddings de cada palavra no corpus de modo que o vetor da palavra no espaço de embeddings melhor captura o significado da palavra. Para isso, Word2Vec usa similaridade distribucional e hipótese distribucional, ou seja, extrai o significado de uma palavra a partir do seu contexto. Assim, se duas palavras geralmente ocorrem em contextos similares, é altamente provável que seus significados sejam também similares.

Dessa maneira, o Word2Vec projeta o significado das palavras num espaço vetorial onde palavras com significados similares tendem a serem agrupadas juntas e palavras com significados muito diferentes estão longe umas das outras.

Conceitualmente, o que queremos saber é, dada uma palavra e as palavras que aparecem em seu contexto , como encontramos um vetor que melhor representa o significado da palavra? Bom, para cada palavra no corpus, iniciamos um vetor com valores aleatórios. O modelo Word2Vec refina os valores predizendo dados os vetores de palavras no contexto . Isto é feito através de uma rede neural de duas camadas, mas antes de construir a rede neural de duas camadas, vamos ver modelos pré-treinados.

## Prática

A primeira coisa a ser feita é importar os pacotes necessários:
"""

import numpy as np
import pandas as pd
import gensim
from gensim.models import Word2Vec
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import time
import string
import unicodedata
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import multiprocessing

"""Depois, vamos ler o mesmo arquivo que usamos anteriormente, para fazermos uma comparação com os tipos de representação vistos nas aulas passadas."""

df = pd.read_csv("https://dados-ml-pln.s3-sa-east-1.amazonaws.com/produtos.csv", delimiter=";", encoding='utf-8')
df.dropna(inplace=True)
df["texto"] = df['nome'] + " " + df['descricao']
df = df.loc[:, ['categoria', 'texto']]
df.head(3)

df.shape

df.head(20)

"""Agora, precisamos embaralhar os dados. Com isso, evitamos que o modelo aprenda bem somente sobre uma classe, já que ele pode ficar preso em mínimos locais. Para isso, usaremos o método Shuffle, da biblioteca utils da Scikit-Learn. Por fim, reiniciamos o index e eliminamos a nova coluna de índice criada e mostramos as 5 primeiras linhas de nosso dataset."""

df = shuffle(df)
df = df.reset_index(drop=True)
df.head(10)

set(df['categoria'])

df['categoria'].value_counts()

"""Vamos usar o mesmo conjunto de funções para tratamento de texto que escrevemos. Vou colocá-lo aqui e relembrar brevemente o que cada função faz:"""

nltk.download('stopwords')
nltk.download('punkt')

def normalize_accents(text):
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")

def normalize_str(text):
    text = text.lower()
    text = remove_punctuation(text)
    text = normalize_accents(text)
    text = re.sub(re.compile(r" +"), " ",text)
    return " ".join([w for w in text.split()])

def remove_punctuation(text):
    punctuations = string.punctuation
    table = str.maketrans({key: " " for key in punctuations})
    text = text.translate(table)
    return text


def tokenizer(text):
    stop_words = nltk.corpus.stopwords.words("portuguese") # portuguese, caso o dataset seja em português
    if isinstance(text, str):
        text = normalize_str(text)
        text = "".join([w for w in text if not w.isdigit()])
        text = word_tokenize(text)
        text = [x for x in text if x not in stop_words]
        text = [y for y in text if len(y) > 2]
        return [t for t in text] #lista de palavras
    else:
        return None

"""Novamente, aplicamos essas funções para tratar o texto de todas as linhas da coluna Title. O texto tratado estará dentro da nova coluna criada chamada Title_treated."""

df['texto_Treated'] = df['texto'].apply(tokenizer)

df.head() # verificando os resultados

"""Agora vamos criar variáveis que serão os hiperparametros de entrada para a construção do Word2Vec usando o gensim. O gensim é uma biblioteca criada para documentos como um vetor semântico de maneira e menos dolorida possível."""

# parâmetros do word2vec
dim_vec = 300 # dimensão
min_count = 10 # palavras que apareçam pelo menos 10x no dicionário
window = 4 # 4 palavras antes e 4 palavras depois
num_workers = multiprocessing.cpu_count() # cpu disponíveis no computador
seed = np.random.seed(42)

"""Com isso, podemos criar um modelo do Word2Vec a partir dos dados da coluna tratada. Importante notar que esse exemplo não captura tudo aquilo que o Word2Vec pode oferecer, visto que na prática treinamos com uma quantidade muito maior de texto. O objetivo aqui é apenas ilustrar o processo de treinamento de embbedings. Mesmo assim, veremos que os resultados serão muito satisfatórios."""

# instância do Word2Vec
modelo = Word2Vec(df['texto_Treated'],
                  min_count = min_count,
                  vector_size = dim_vec,
                  window = window,
                  seed = seed,
                  workers = num_workers,
                  sg = 1) # sg = 0 -> CBOW e sg = 1 -> skipgram

# sg (Skip-gram): Prever as palavras que estão a uma certa distância (contexto) da palavra central (target).
# cbow (continuous bag of word): Reconstruir a palavra central (target) com base em um contexto de palavras ao seu redor

"""Podemos verificar o tamanho do vocabulário que o modelo criou:"""

print('Tamanho do vocabulário do Word2Vec: ', len(modelo.wv))

"""Treinado o modelo, conseguimos explorar um pouco as relações semânticas que ele consegue estabelecer. Veja os exemplos a seguir:"""

# exemplos das relações semânticas que o word2vec consegue estabelecer
print(modelo.wv.most_similar('mario'), '\n') # palavra mais similar a 'mario'
print(modelo.wv.similarity('mario', 'game'), '\n') # similaridade entre duas palavras
print(modelo.wv.most_similar(positive=['mario', 'luigi'], negative = ['game'], topn = 3)) # similaridade considerando exemplos positivos e negativos

"""O Word2Vec treinado retorna um vetor de 300 dimensões para cada palavra. Entretanto, estamos trabalhando com frases. Dessa maneira, precisamos calcular o vetor das frases. Para isso, considere o seguinte código:"""

# Embedding para ser representado por uma frase

def meanVector(model,phrase):
    vocab = list(model.wv.index_to_key) #Retorna uma lista com as palavras que formam o vocabulário do modelo
    phrase = " ".join(phrase) #Junta as palavras numa string só
    phrase = [x for x in word_tokenize(phrase) if x in vocab] #Mantém na variável apenas palavras que estão no dicionário
    #Quando não houver palavra o vector recebe 0 para todas as posições
    if phrase == []:
        vetor = [0.0]*dim_vec
    else:
        #Caso contrário, calcula um vetor com a média do vetor de cada palavra na frase
        vetor = np.mean([model.wv[word] for word in phrase],axis=0)
    return vetor

"""Agora, criamos outra função que usará a função criada anteriormente para retornar as features que serão imputadas no modelo a ser treinado:"""

# Função para retornar as features para inputar no modelo
def createFeatures(base):  #Cria uma função chamada createFeatures que recebe o dataframe como parâmetro
    #Calcula o vetor médio de cada frase presente na base e retorna num formato de lista de listas
    features = [meanVector(modelo,base['texto_Treated'][i])for i in range(len(base))]
    return features

"""Criaremos uma variável labels, que conterá os rótulos das amostras de treinamento:"""

labels = np.array(df['categoria']) # label para cada uma das frases

df = createFeatures(df)

df

"""Separamos os dados em conjunto de treino e teste, instanciamos e treinamos um modelo SVM, calculando o tempo de treinamento e fazemos a predição do conjunto de teste:"""

X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.3, random_state=42)
clf = svm.SVC(kernel='rbf') # utiliza uma função de base radial como kernel
# SVM com kernel RBF é um escolha sólida quando se lida com conjuntos de dados complexos e não lineares
start_time = time.time()
clf.fit(X_train, y_train)
end_time = time.time()
y_pred = clf.predict(X_test)

import datetime
sec = end_time-start_time
print(str(datetime.timedelta(seconds = sec)))

"""Por fim, imprimimos o valor da acurácia no conjunto de teste:"""

print('Accuracy:', metrics.accuracy_score(y_test, y_pred))

# Frases fornecidas
frases = ['A O Reilly separou alguns dos melhores insights de especialistas em matéria de programação e membros da indústria para que programadores possam mergulhar profundamente no mais recente do que está acontecendo no mundo da engenharia de software, arquitetura e código aberto.',
          'A Maybelline NY criou um Testador Virtual que te ajuda a escolher a tonalidade do seu corretivo, usando a câmera do seu smartphone. Nessa plataforma, é usado recurso de Inteligência Artificial que identifica através da sua foto, o tom da sua pele, sendo assim, sugere o tom ideal para você usar.',
          'A saga Zelda é uma série de jogos de ação e aventura desenvolvida pela Nintendo, que começou em 1986 com o lançamento de “The Legend of Zelda” para o console NES. Ela é centrada em torno de Link, um herói corajoso e destemido que luta contra forças do mal para salvar a Princesa Zelda e o Reino de Hyrule',
          'Mario Bro Nintendo']

# Criar um DataFrame
data = {'texto_Treated': frases}
df_novo_teste = pd.DataFrame(data)

df_novo_teste['texto_Treated'] = df_novo_teste['texto_Treated'].apply(tokenizer)

# Criação dos vetores de média para o novo teste
features_novo_teste = createFeatures(df_novo_teste)

# Realiza as previsões com o modelo treinado
y_pred_novo_teste = clf.predict(features_novo_teste)
print(y_pred_novo_teste)