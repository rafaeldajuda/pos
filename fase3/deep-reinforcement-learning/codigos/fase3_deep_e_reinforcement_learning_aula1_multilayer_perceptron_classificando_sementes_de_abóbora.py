# -*- coding: utf-8 -*-
"""fase3_deep_e_reinforcement_learning_aula1_Multilayer_Perceptron_Classificando_sementes_de_abóbora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ftDyBYkF0S5Cbl3-cTckLazriYfi341k

# Classificando diferentes tipos de semente de abóbora 🎃🌱

As sementes de abóbora são frequentemente consumidas como confeitos em todo o mundo devido à sua quantidade adequada de proteínas, gorduras, carboidratos e teores minerais. A base de dados **"SementesAbobora.xlsx"** possui um estudo foi realizado nos dois tipos de sementes de abóbora mais importantes e de qualidade, **“Ürgüp Sivrisi” e “Çerçevelik”**, geralmente cultivadas nas regiões de Ürgüp e Karacaören na Turquia.

Muitas espécies de sementes têm semelhanças visuais, o que torna a classificação manual difícil e sujeita a erros. Redes neurais podem ser treinadas para identificar padrões que não são facilmente perceptíveis pelo olho humano, aumentando a precisão da classificação.

Imagine que foi proposto para você o desafio de criar uma **inteligência para identificar os tipos de sementes para ajudar a equipe de engenheiros e engenheiras Agrícolas**. Para trabalhar com a precisão dos resultados x complexidade das características de sementes, você optou em utilizar as redes neurais multilayer perceptron. Vamos para a aplicação?

## Features

*  Perímetro
*  Maior_Eixo_Comprimento
*  Comprimento_Eixo_Menor
*  Área_Convexa
*  Equiv_Diâmetro
*  Excentricidade
*  Solidez
*  Extensão
*  Redondeza
*  Proporcao
*  Compacidade

## Target

Classes: ((A)Çerçevelik, (B)Ürgüp Sivrisi)

Vamos colocar a mão na massa. Vamos importar a base de dados "SementesAbobora.xlsx" utilizando a biblioteca pandas. E analisar a dimensão dos dados.
"""

import pandas as pd

df = pd.read_excel('SementesAbobora.xlsx')

df.head()

df.shape

"""Observe que essa base de dados possui os dados de classes de forma ordenada, isso pode ser um problema para o aprendizado de máquina. Vamos começar a já embaralhar os dados com o comando shuffle."""

from sklearn.utils import shuffle

df = shuffle(df)

df.head(10)

"""Muito bem, agora temos os dados embaralhados. Próximo passo, vamos conhecer o equilíbrio das nossas classes (já que temos um problema de classificação a ser resolvido)."""

df['Class'].value_counts()

"""Base está equilibrada, ótimo! Caso não estivesse, teríamos que aplicar técnicas de reamostragem de dados ou até mesmo coletar mais dados para a criação de nossa rede neural.

Vamos analisar os dados com uma análise exploratória? 📊
"""

# Visualização
import seaborn as sns
import matplotlib.pyplot as plt

# Potando histogramas para analisar a simetria dos dados
df.hist(bins=100, figsize=(12, 12))
plt.show()

"""Podemos observar que existem muitas variáveis com a distribuição quase que normal, ou seja, não temos muitos outliers exeto para as variáveis: Proporcao, Redondeza e Compacidade que possuem distribuição assimétrica muito forte.

Que tal analisarmos as correlações?
"""

correlation_matrix = df.corr(numeric_only=True).round(2)

fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)

"""A correlação é muito importante para entendermos as relações das variáveis (ou seja, a associação entre duas variáveis). Podemos identificar aqui que temos variáveis altamente correlacionadas e sabemos que isso pode ser um problema para o modelo.

Area, Area_convexa, Equiv_Diâmetro e Maior_Eixo_Comprimento possuem correlação maior que **0.90** quando analisadas com a variável **Perímetro**, isso se deve pelo motivo que que todas essas variáveis são relacionadas ao tamanho das sementes. Já sabemos que não precisamos colocar todas no modelo.

Vamos passar um pouco rápido pela etapa de análise exploratória pois não é o foco dessa aula, mas eu sempre gosto de relembrar a importância de uma boa análise exploratória nos dados.

# Tratando a variável target
"""

df.info()

# Utilizadno Label Enconder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df.Class = le.fit_transform(df['Class'])

set(df['Class'])

"""## Separando os dados

Como todo aprendizado de máquina, precisamos separar as bases de treino e teste! Vamos incluir todas as variáveis do modelo exceto as que estão altamente correlacionadas entre si (Area, Area_convexa, Equiv_Diâmetro e Maior_Eixo_Comprimento). Dentre as variáveis com muita correlação, vamos selecionar apenas a Area.
"""

df.info()

X = df[['Area','Perímetro', 'Comprimento_Eixo_Menor','Excentricidade','Solidez','Extensão','Redondeza', 'Proporcao', 'Compacidade']]
y = df['Class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

"""## Pré-processamento dos dados

Apesar de deep learning não requerer distribuições normais, é comum aplicar **técnicas de pré-processamento de dados para normalizar ou padronizar as características**. Isso pode ajudar a acelerar a convergência do treinamento da rede neural.

A convergência está relacionada com o erro, ou seja, o quanto a sua rede aprende a corrigir os erros durante o processamento.
"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)
scaler.fit(X_test)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

X_train.shape

X_test.shape

"""## Moldando nossas variáveis resposta

Perceba que a nossas classes estão em um formato de estrutura de dados unidimensional (assim como uma coluna) e precisamos moldar para o formato de array -n dimensional(matriz).

O comando reshape é utilizado para reformatar a estrutura de um array multidimensional, como um tensor, que é a estrutura de dados fundamental usada em deep learning e processamento de dados em redes neurais.
"""

type(y_train)

import numpy as np

# reshape() molda uma matriz sem alterar os dados da matriz.
y_train = np.asarray(y_train).astype('float32').reshape((-1,1))
y_test = np.asarray(y_test).astype('float32').reshape((-1,1))

type(y_train)

y_train.shape

"""## Construindo a arquitetura da rede neural multicamadas 🦾

Agora utilizando as bibliotecas tensorflow e keras, vamos construir a arquitetura da nossa primeira rede neural.
"""

!pip install tensorflow

import tensorflow as tf

# keras libraries
from tensorflow import keras
from keras import models
from keras import layers
from keras import metrics
from keras.optimizers import Adam
from keras.metrics import Precision
from tqdm.keras import TqdmCallback

# Semente aleatótia para manter os mesmos dados
tf.random.set_seed(7)

# Definindo entradas da rede + tamanho da batch de processamento
input_shape = X_train.shape[1]    # Variáveis de entrada
output_shape = y_train.shape[1]   # Classe preditora
batch_size = 20

# Abrindo uma sequencia de neuronios
model = models.Sequential()

# input layer
# Entrada da rede
model.add(layers.Dense(
                        batch_size
                       ,input_shape=(input_shape,)
                       ,activation='relu'))

# hidden layer
# Camada oculta
model.add(layers.Dense(
                        12
                       ,activation='relu'))

# hidden layer
# Camada oculta
model.add(layers.Dense(
                        6
                       ,activation='relu'))


# dropout layer
# Aplicando regularização
model.add(layers.Dropout(0.5))

# output layer
# Camada de saída
model.add(layers.Dense(
                        output_shape
                       ,activation='sigmoid'))

# Configurar o otimizador Adam com uma learning rate específica
# Defina a learning rate desejada
learning_rate = 0.001
otimizador = Adam(learning_rate=learning_rate)

# Compilar o modelo com o otimizador configurado
model.compile(loss='binary_crossentropy', optimizer=otimizador, metrics=['accuracy'])

# summmary
model.summary()

"""Agora vamos executar as épocas de processamento para a rede treinar e encontrar o menor erro:"""

# Configurando as épocas de processamento para a convergência do erro da função de custo
epoch = 100

hist = model.fit(X_train
                  ,y_train
                  ,epochs = epoch
                  ,batch_size=batch_size
                  ,shuffle=True
                  ,validation_data=(X_test, y_test)
                  ,verbose=0
                  ,callbacks=[TqdmCallback(verbose=0)]
          )

acc = '{:.2%}'.format(hist.history['accuracy'][-1])
print(f"O modelo possui uma acurácia de {acc} com {epoch} epochs de processamento")

"""## Validando nosso modelo

É muito importante comparar a performance do modelo tanto na base de treinamento quanto de validação. Para isso vamos plotar dois gráficos para acompanhar a performance do modelo pelas épocas de processamento.
"""

# Visualizando os resultados de treino
acc = hist.history['accuracy']
val_acc = hist.history['val_accuracy']

loss = hist.history['loss']
val_loss = hist.history['val_loss']

epochs_range = range(epoch)

# Plot Acurácia
plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Acurácia de Treinamento')
plt.plot(epochs_range, val_acc, label='Acurácia de Validação')
plt.legend(loc='lower right')
plt.title('Acurácia de treino e teste')

# Plot Erro de treinamento
plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Erro de treinamento')
plt.plot(epochs_range, val_loss, label='Erro de Validação')
plt.legend(loc='upper right')
plt.title('Erro de treinamento vs validação')
plt.show()

from sklearn.metrics import classification_report
# Predictions
y_pred = model.predict(X_test)
y_pred_class = [round(x[0]) for x in y_pred]
y_test_class = y_test

# classification report
class_names = []
for i in y.unique():
    class_names.append(le.inverse_transform([i])[0])

print(classification_report(y_test_class, y_pred_class, target_names=class_names))