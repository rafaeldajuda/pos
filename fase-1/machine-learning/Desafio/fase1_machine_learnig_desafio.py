# -*- coding: utf-8 -*-
"""fase1-machine-learnig-desafio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QDSebNmqakpPfii-vWcxy95CqSDzHXVv

# Desafio

Utilizando a base de dados "insurance.csv", você tem o desafio de criar um modelo preditivo de regressão para prever o valor dos custos médicos individuais cobrados pelo seguro de saúde.

# Sobre a base de dados

Essa base de dados contém 1338 linhas com informações sobre a idade da pessoa, gênero, índice de massa corporal (IMC), número de filhos, flag de verificação se a possoa é fumante, região residencial do benefício e o valor do custo médico.

# Objetivo

Criar um modelo preditivo e comprovar sua eficácia com métricas estatísticas.

## Importando a base de dados
"""

import pandas as pd

# Importando a base de dados
df = pd.read_csv("insurance.csv")

"""## Informações da base de dados"""

df.head()

df.shape

"""* 1338 linhas
* 7 colunas
"""

df.info()

"""*   Não existe campos vazios
*   3 campos são textos (sex, smoker e region)
*   Os campos sex e smoker são valores binários

## Checando as categorias dos campos tipo texto
"""

set(df['sex'])

df['sex'].value_counts()

set(df['smoker'])

df['smoker'].value_counts()

set(df['region'])

df['region'].value_counts()

"""## Analisando os dados númericos"""

df.describe()

"""# Histogramas"""

df.hist(bins=50, figsize=(20, 15))

"""* Existe uma concentração alta de pessoas com menos de 20 anos
* Existe uma concetranção alta de custos médico de até 10 mil
* Alta concentração de pessoas com IMC altos entre as idades de 25 e 35 anos

# Separando as bases em treino e teste
"""

from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=0.25, random_state=42)
print(len(df_train), "treinamento + ", len(df_test), "teste")

"""## Criando a categoria de custo médico"""

df['charges'].hist()

# Dividindo custos médiso pelo valor 10000 limitar o número de categorias de renda
import numpy as np
np.random.seed(42)

df['charges_cat'] = np.ceil(df['charges'] / 10000.) # ceil para arredondar valores para cima
df['charges_cat'].where(df['charges_cat'] < 5, 5.0, inplace=True)

# cut do Pandas, que é comunente usada para dividir um conjunto de dados em intervalos discretos chamados de "bins" (intervalos ou faixas)
df['charges_cat'] = pd.cut(df['charges'],
       bins=[0., 15000., 30000., 45000., 60000., np.inf],
       labels=[10000, 20000, 30000, 40000, 50000])

df['charges_cat'].value_counts()

df['charges_cat'].hist()

"""## Amostragem estratificada com base na categoria de custs médicos"""

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
for train_index, test_index in split.split(df, df['charges_cat']):
  strat_train_set = df.loc[train_index]
  strat_test_set = df.loc[test_index]

# Analisando proporções
strat_test_set['charges_cat'].value_counts() / len(strat_test_set)

# Analisando proporções
df['charges_cat'].value_counts() / len(df)

"""Depois de garantir que os valores dos custos médico estão distribuídos de forma estratificada, podemos remover a coluna charges_cat que foi utilizada como variável auxiliar."""

# Removendo a coluna charges_cat
for set_ in (strat_train_set, strat_test_set):
  set_.drop('charges_cat', axis=1, inplace=True)

"""# Buscando Correlações"""

charges = strat_train_set.copy()
charges.head()

charges_matrix = charges.corr(numeric_only=True)

charges_matrix['charges'].sort_values(ascending=False)

"""*   Não considerando os campos sex, smoker e region parece que os dados possuem pouc correlação
* Os campos age e bmi (IMC) possuem maior correlação com os custos médico
"""

from pandas.plotting import scatter_matrix

attributes = ['age', 'bmi', 'children']
scatter_matrix(charges[attributes], figsize=(12, 8))

"""*   Parece que a idade (age) possui maior correlação para prever os custos médicos
*   O IMC (bmi) também possui uma forte correlação, porém menor comparado a idade
"""

# Commented out IPython magic to ensure Python compatibility.
# Para plots bonitinhos
# permite a exibição de gráficos gerados pelo Matplotlib diretamente dentro do notebook ou ambiente de desenvolvimento, sem a necessidade de chamar explicitamente a função plt.show()
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Plotando as colunas charges e age
charges.plot(kind='scatter', x='charges', y='age', alpha=0.1)
plt.axis([0, 50000, 0, 70])

"""Observações:
*   Quanta mais velha a pessoa maior é o valor de custo médico
*   Maior parte dos custos médicos fica em torno de 10000

# Preparando os dados para colocar no algoritmo
"""

charges = strat_train_set.drop('charges', axis=1) # Apagando a target para a base de treino (X)
charges_labels = strat_train_set['charges'].copy() # Armazenando a target (X)

charges_num = charges.drop(['sex', 'smoker', 'region'], axis=1)
charges_num.head()

"""# Pré-processando as categorias

Tratando as categorias de textos.
"""

charges_cat_ordinal = charges[['region']]
charges_cat_ordinal.head(10)

charges_cat_bin_sex = charges[['sex']]
charges_cat_bin_sex.head(10)

charges_cat_ordinal_smoker = charges[['smoker']]
charges_cat_ordinal_smoker.head(10)

"""## Valores Ordinais"""

try:
  from sklearn.preprocessing import OrdinalEncoder
except:
  from future_encoders import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
charges_cat_region_encoded = ordinal_encoder.fit_transform(charges_cat_ordinal)
charges_cat_region_encoded[:10]

ordinal_encoder.categories_

ordinal_encoder_smoker = OrdinalEncoder()
charges_cat_smoker_encoded = ordinal_encoder_smoker.fit_transform(charges_cat_ordinal_smoker)
charges_cat_smoker_encoded[:10]

ordinal_encoder_smoker.categories_

"""## Valores binários"""

try:
  from sklearn.preprocessing import OneHotEncoder
except:
  from future_encoders import OneHotEncoder

cat_encoder_sex = OneHotEncoder(sparse=False)
charges_cat_1hot_bin_sex = cat_encoder_sex.fit_transform(charges_cat_bin_sex)
charges_cat_1hot_bin_sex

cat_encoder_sex.categories_

"""# Criando a pipeline de pré-processamento dos dados

Agora vamos construir uma pipeline para pré-processar os atributos numéricos
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler # funções que retorna a média e o desvio padrão dos dados

num_pipeline = Pipeline([
    ('std_scaler', StandardScaler()), # padronizando as escalas dos dados
])

charges_num_tr = num_pipeline.fit_transform(charges_num)

charges_num_tr

"""Agora vamos tratar os valores categóricos"""

try:
  from sklearn.compose import ColumnTransformer
except:
  from future_encoders import ColumnTransformer # Scikit-Learn < 0.20

from sklearn.compose import ColumnTransformer

num_attribs = list(charges_num)
cat_attribs_ordinal = ['region']
cat_attribs_bin_sex = ['sex',]
cat_attribs_ordinal_smoker = ['smoker']

full_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_attribs), # tratando as variáveis numéricas (chamada a pipeline de cima)
    ('cat_ordinal', OrdinalEncoder(), cat_attribs_ordinal), # tratando as variáveis categóricas, region
    ('cat_bin_sex', OneHotEncoder(), cat_attribs_bin_sex), # tratando as variáveis categóricas, sex
    ('cat_ordinal_smoker', OrdinalEncoder(), cat_attribs_ordinal_smoker), # tratando as variáveis categóricas, smoker
])

charges_prepared = full_pipeline.fit_transform(charges)

charges_prepared

charges_prepared.shape

type(charges_prepared)

"""Perceba que o resultado é uma matriz multidimensional. Precisamos transforma-lá em datarrame."""

column_names = ['age', 'bmi', 'children', 'region', 'female', 'male', 'smoker']

# Transformar o array em DataFrame
charges_df = pd.DataFrame(data=charges_prepared, columns=column_names)

# Exibir o DataFrame resultante
print(charges_df.shape)

charges_df.head(10)

"""# Escolhendo o melhor modelo de regressão

## Regreção Linear

*   Equação do 1° grau.
*   A Regreção Linear busca entender o padrão de um valor dependendo de outro ou outros, e assim encontrar uma função que expressa esse padrão.
*   **Foco**: busca o melhor valor que os coeficientes possam atingir, de maneira que a diferença entre o valor predito pela função e o real,sejam menores.
"""

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(charges_prepared, charges_labels)

# Vamos tentar o pipeline de pré-processamento completo em algumas intâncias de treinamento
some_data = charges.iloc[:5]
some_labels = charges_labels.iloc[:5]

some_data_prepared = full_pipeline.transform(some_data)

predictions = lin_reg.predict(charges_prepared)

print('Predictions:', lin_reg.predict(some_data_prepared))

"""Compare com os valores reais:"""

print('Labels:', list(some_labels))

print('predictions:', predictions[:5])

"""# Avaliando o modelo

O **MSE** mede a média dos quadrados das diferenças entre os valores previstos pelo modelo e os valores reais observados no conjunto de dados.

Quando menor o valor do MSE, melhor o ajuste do medelo de dados.
"""

from sklearn.metrics import mean_squared_error
# erro médio quadrático eleva ao quadrado a média do erro médio absoluto.
# Estou avaliando se os erros não são tão grandes, esses erros são penalizados.
# penaliza muito mais valores distantes da média

charges_predictions = lin_reg.predict(charges_prepared)
lin_mse = mean_squared_error(charges_labels, charges_predictions)
lin_rmse = np.sqrt(lin_mse) # raiz quadrada
lin_rmse

# erro absoluto
from sklearn.metrics import mean_absolute_error

lin_mae = mean_absolute_error(charges_labels, charges_predictions)
lin_mae

from sklearn.metrics import r2_score

r2 = r2_score(charges_labels, charges_predictions)
print('r²', r2)

# Função para calcular o MAPE (Mean Absolute Percentage Error)

def calculate_mape(labels, predictions):
  errors = np.abs(labels - predictions)
  relative_errors = errors / np.abs(labels)
  mape = np.mean(relative_errors)
  return mape

# Calcular MAPE
mape_result = calculate_mape(charges_labels, charges_predictions)

# Imprimir o resultado
print(f'O MAPE é: {mape_result:.2f}%')

"""# Outro modelo: Árvore de decisão"""

from sklearn.tree import DecisionTreeRegressor

# Criando o modelo de DecisionTreeRegressor
model_dtr = DecisionTreeRegressor(max_depth=10)
model_dtr.fit(charges_prepared, charges_labels)

# vamos tentar o pipeline de pré-processamento completo em algumas instâncias de treinamento
some_data = charges.iloc[:5]
some_labels = charges_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)
predictions = model_dtr.predict(some_data_prepared)

print('Predictions:', predictions)

"""Comparando com os valores reais:"""

print('Labels:', list(some_labels))

# mean_squared_error
charges_predictions = model_dtr.predict(charges_prepared)
lin_mse = mean_squared_error(charges_labels, charges_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse

# mean_absolute_error
lin_mae = mean_absolute_error(charges_labels, charges_predictions)
lin_mae

# r2_score
r2 = r2_score(charges_labels, charges_predictions)
print('r²', r2)

# Calcular o MAPE
mape_result = calculate_mape(charges_labels, charges_predictions)

# Imprimir o resultado
print(f'O MAPE é: {mape_result:.2f}%')