# -*- coding: utf-8 -*-
"""fase1_machine_learning_avancado_k_means_modelo_nao_supervisionado.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Qzwdcv3lzwFR41Ef7hBkwHOOIg_eQLo

# Clusterização

O agrupamento  é uma técnica para dividir os dados  em diferentes grupos, na qual os registros em cada grupo são semelhantes uns aos outros. Os grupos podem ser usados diretamente, analisando mais a fundo ou passados como uma característica ou resultado para um modelo de regressão ou classificação.
## Grupo de Consumidores

Vamos aprender a realizar um modelo de clusterização utilizando um case de segmentação de clientes de um shopping. Como podemos criar grupos de consumidores dado algumas caracteríticas de perfis?

## Sobre a base de dados:

Esse conjunto de dados ilustra alguns dados dos consumidores de um shopping. A base possui algumas features como: gênero, idade, renda anual e pontuação de gastos.

## Bibliotecas utilizadas
"""

import pandas as pd

# Plot de gráficos
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns

# Algoritmos de Agrupamento
from sklearn.cluster import KMeans, DBSCAN

# Avaliação de Desempenho
from sklearn.metrics import adjusted_rand_score, silhouette_score

"""# Algumas principais técnicas de clusterização"""

dados = pd.read_csv('mall.csv', sep=',')

dados.shape

dados.head()

"""# Limpeza de dados"""

dados.isnull().sum()

"""# Análise exploratória dos dados

*   Conhecer os dados, identificar padrões, encontrar anomalias, etc.


"""

dados.describe()

# Pegar a média de uma coluna específica
dados['Annual Income (k$)'].median()

"""Analisando a distribuição das variáveis:"""

# histograma
dados.hist(figsize=(12, 12))

"""Análisando a correlação entre as variáveis:"""

plt.figure(figsize=(6, 4))
sns.heatmap(dados[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].corr(method='pearson'), annot=True, fmt='.1f')

"""*   Inicialmente notamos que existe uma baixa correlação entre as variávies
*   Baixa correlação significa o quanto as variáveis estão sendo dispersas uma da outra

Analisar a proporção entre gêneros:
"""

dados['Gender'].value_counts()

"""Boa proporção entre os generos que temos disponíveis em nossos dados.

Vamos fazer um gráfico completo com todos os dados para checarmos possíveis agrupamentos que podem ser realizados.
"""

sns.pairplot(dados, hue='Gender')
plt.show()

"""Aparentemente o Annual Income e o Spending Score permitem alguns agrupamentos dos nossos dados.

Podemos trabalhar com eles.

# Feature Scaling

Verificar a necessidade de utilizar a padronização ou normalização dos dados
"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler #Feature Engineer

scaler = StandardScaler()
# scaler = MinMaxScaler()
scaler.fit(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

dados_Escalonados = scaler.transform(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

dados_Escalonados

"""### Criando os agrupamentos
Vamos criar agrupamentos com diferentes metodologias:

### 1 - K-Means

**Sobre o modelo:**
O K-Means parte da ideia de quebrar o espaço multidimensional de dados em partições a partir do centróide dos dados. Após inicializar os centróides de forma aleatória sobre os dados, o K-Means **calcula a distância dos dados para os centros mais próximos**. Esse cálculo da distância é realizado várias vezes até que os dados sejam agrupados da melhor forma possível de acordo com a distância mais próxima de um centróide (ponto centro de dado na qual será formado o grupo).

**Hiperparametros:**
Definição do K. Para definir esse valor de K, é necessário utilizar o **método Elbow** para encontrar o melhor hiperparâmetros de K. O método Elbow consiste no cálculo da soma dos erros quadráticos.

**Vantagens:**
Implementação simplificado e possui uma certa facilidade em lidar com qualquer medida de similaridade entre os dados.

**Desvantagem:**
Difícil definir o melhor K. Sensível a outliers. Não consegue distinguir grupos em dados não-globulares.

Para mais informação: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Executando o algoritmo sem feature scaling
"""

# Definindo o modelo de clusterização. K-MEANS com 6 clusters
kmeans = KMeans(n_clusters=6,random_state=0) # Definindo os hiperparametros do algoritmo (definir o número de grupo = cluster)

# Implementando o K-Means nos dados:
kmeans.fit(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

# Salvando os centroides de cada cluster
centroides = kmeans.cluster_centers_

# Salvando os labels dos clusters para cada exemplo
kmeans_labels = kmeans.predict(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

"""Executando com feature scaling"""

# OBS: Aqui acredito que deveria utilizar a instância do cluster kmeans_escalonados
# OBS: É provável que a professora errou nesse trecho

# Definindo o modelo de clusterização. K-Means com 6 clusters
kmeans_escalonados = KMeans(n_clusters=6,random_state=0)

# Implementando o K-Means nos dados:
kmeans.fit(dados_Escalonados)

# Salvando os centroides de cada cluster
centroides_escalonados = kmeans.cluster_centers_

# Salvando os labels dos clusters para cada exemplo
kmeans_labels_escalonados = kmeans.predict(dados_Escalonados)

dados_Escalonados = pd.DataFrame(dados_Escalonados, columns=['Annual Income (k$)', 'Spending Score (1-100)'])

dados_Escalonados.head()

dados_Escalonados['Grupos'] = kmeans_labels_escalonados
dados_Escalonados.head()

dados['Grupos'] = kmeans_labels
dados.head()

"""Vamos analisar a nossa previsão e os centróides:"""

pd.Series(kmeans_labels).value_counts()

centroides # espaço tridimensional (salário e score de gasto)

"""### Cluster com feature scaling"""

# plotando os dados identificando com seus clusters
plt.scatter(dados_Escalonados[['Annual Income (k$)']], dados_Escalonados[['Spending Score (1-100)']], c=kmeans_labels_escalonados, alpha=0.5, cmap='rainbow')
plt.xlabel('Salário Anual')
plt.ylabel('Pontução de Gastos')

# plotando os centroides
plt.scatter(centroides_escalonados[:, 0], centroides_escalonados[:, 1], c='black', marker='X', s=200, alpha=0.5)
plt.rcParams['figure.figsize'] = (10, 5)
plt.show()

"""### Cluster sem feature scaling"""

# plotando os dados identificando com seus clusters
plt.scatter(dados[['Annual Income (k$)']], dados[['Spending Score (1-100)']], c=kmeans_labels, alpha=0.5, cmap='rainbow')
plt.xlabel('Salário Anual')
plt.ylabel('Pontução de Gastos')

# plotando os centroides
plt.scatter(centroides[:, 0], centroides[:, 1], c='black', marker='X', s=200, alpha=0.5)
plt.rcParams['figure.figsize'] = (10, 5)
plt.show()

"""Escolhendo a quantidade de grupos (k) usando o método do "cotovelo" (elbow):"""

# Lista com a quantidade de clusters que iremos testar
k = list(range(1, 10))
print(k)

# Armazena o SSE (soma dos erros quadráticos) para cada quantidade de k
sse = []

# Roda o K-Means para cada k fornecido
for i in k:
  kmeans = KMeans(n_clusters=i, random_state=0)
  kmeans.fit(dados[['Annual Income (k$)', 'Spending Score (1-100)']])
  sse.append(kmeans.inertia_) # calculo de erro k-means (mudar centroide dos dados)

plt.rcParams['figure.figsize'] = (10, 5)
# Plota o gráfico com a soma dos erros quadraticos
plt.plot(k, sse, '-o')
plt.xlabel(r'Número de clusters')
plt.ylabel('Inércia')
plt.show()

"""(chatgpt)<br/>
O método do cotovelo é uma técnica utilizada para determinar o número ideal de clusters em uma análise de clusterização, especialmente para algoritmos como K-Means. O método baseia-se em observar a relação entre o número de clusters e a soma das distâncias quadradas dentro de cada cluster (inertia).

**Como funciona o método do cotovelo:**

1. **Variar o número de clusters**: Execute o algoritmo de K-Means com um intervalo de números de clusters (por exemplo, de 1 a 10).

2. **Calcular a inércia**: Para cada número de clusters, calcule a inércia, que é a soma das distâncias quadradas dos pontos de dados até seus respectivos centros de cluster.

3. **Criar um gráfico**: Crie um gráfico com o número de clusters no eixo x e a inércia no eixo y.

4. **Identificar o ponto de inflexão**: O "cotovelo" geralmente ocorre quando adicionar mais clusters não resulta em uma melhoria significativa na inércia. Esse ponto de inflexão é chamado de cotovelo porque o gráfico geralmente tem uma forma de "L" invertido.

5. **Escolher o número ideal de clusters**: O número ideal de clusters é o valor de `k` que está no ponto do cotovelo, onde a taxa de diminuição da inércia começa a desacelerar.

Vou gerar um gráfico de exemplo para ilustrar o método do cotovelo. Nele, mostrarei como a inércia muda conforme o número de clusters aumenta. A partir da visualização, você poderá ver como identificar o ponto do cotovelo.

O gráfico acima é um exemplo do método do cotovelo.

- **Eixo X**: Mostra o número de clusters (`k`), variando de 1 a 10.

- **Eixo Y**: Mostra a inércia, que é a soma das distâncias quadradas dentro dos clusters.

Observe como a inércia diminui rapidamente à medida que o número de clusters aumenta. No entanto, após um certo ponto, a taxa de diminuição da inércia começa a desacelerar, formando um "cotovelo" ou ponto de inflexão no gráfico.

Neste exemplo, o ponto de inflexão ocorre em torno de 5 clusters, o que sugere que esse pode ser o número ideal de clusters para usar no algoritmo K-Means com este conjunto de dados.

Você pode usar o método do cotovelo para seus próprios dados para determinar o número ideal de clusters para o K-Means ou outro algoritmo de clusterização.
"""

dados.groupby('Grupos')['Age'].mean()

dados.groupby('Grupos')['Annual Income (k$)'].mean()

"""Podemos notar que após 3 ou 5 clusters a soma do erro quadrático tem uma redução na forma com o qual a função está decrescendo. Assim podemos adotar 5 clusters. Checando os resultados para 5 clusters:"""

# Definindo o modelo de clusterização. K-MEANS com 5 clusters
kmeans = KMeans(n_clusters=5,random_state=0)

# Implementando o K-Means nos dados:
kmeans.fit(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

# Salvando os centroides de cada cluster
centroides = kmeans.cluster_centers_

# Salvando os labels dos clusters para cada exemplo
kmeans_labels = kmeans.predict(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

# plotando os dados identificando com seus clusters
plt.scatter(dados[['Annual Income (k$)']], dados[['Spending Score (1-100)']], c=kmeans_labels, alpha=0.5, cmap='rainbow')
plt.xlabel('Salário Anual')
plt.ylabel('Pontução de Gastos')

# plotando os centroides
plt.scatter(centroides[:, 0], centroides[:, 1], c='black', marker='X', s=200, alpha=0.5)
plt.rcParams['figure.figsize'] = (10, 5)
plt.show()

dados_grupo_1 = dados[dados['Grupos'] == 1]
dados_grupo_1

dados_grupo_2 = dados[dados['Grupos'] == 2]

dados_grupo_3 = dados[dados['Grupos'] == 3]

dados_grupo_4 = dados[dados['Grupos'] == 4]

dados_grupo_1['Annual Income (k$)'].mean() # grupo 1 azul

dados_grupo_2['Annual Income (k$)'].mean() # grupo 2 roxo

dados_grupo_3['Annual Income (k$)'].mean() # grupo 3 laranja

dados_grupo_1['Age'].mean()

dados_grupo_2['Age'].mean() # grupo 2 roxo

dados_grupo_4['Annual Income (k$)'].mean() # grupo 4 vermelho

dados_grupo_3['Spending Score (1-100)'].mean() # grupo 3 laranja

plt.figure(figsize=(6, 4))
sns.heatmap(dados_grupo_1.groupby('Grupos')[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].corr(method = 'pearson'), annot=True, fmt=".1f");

"""### 2 - DBSCAN

**Sobre o modelo:**
O DBSCAN é um algoritmo que agrupa os dados com base em **densidade (alta concentração de dados)**. Muito bom para tirar ruídos. O agrupamentos dos dados é calculado com base nos core (quantidade de pontos mínmos que seja igual ou maior a definição do MinPts), border (ponto de fronteira dos dados) e noise (ruído).

**Hiperparametro:**
Eps (raio ao redor de um dado). MinPts (mínimo de pontos dentro do raio para que seja agrupado).

**Vantagem:**
Capacidade de trabalhar com outliers. Trabalha com base de dados grande.

**Desvantagem:**
Dificuldade para lidar com cluster dentro de cluster. Dificuldade para lidar com dados de alta dimensionalidade. Dificuldade em encontrar o raio de vizinhança ao tentar agrupar dados com distância média muito distinta (clusters mais densos que outros).

Para mais informação: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
"""

# Criando o modelo:
# eps -> raio
# min_samples -> num de pontos
dbscan = DBSCAN(eps=10, min_samples=8)

# Ajustando aos dados
dbscan.fit(dados[['Annual Income (k$)', 'Spending Score (1-100)']])

dbscan_labels = dbscan.labels_
dbscan_labels

"""Labels com -1 foram classificados com outliers"""

# Plotando o gráfico:
plt.scatter(dados[['Annual Income (k$)']], dados[['Spending Score (1-100)']], c=dbscan_labels, alpha=0.5, cmap='rainbow')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

"""*   As bolinhas roxas são consideradas outliers

"""

# Plotando o gráfico sem os outliers:
# máscara para outliners
mascara = dbscan_labels >= 0

# plotando o gráfico
plt.scatter(dados[['Annual Income (k$)']][mascara], dados[['Spending Score (1-100)']][mascara], c=dbscan_labels[mascara], alpha=0.5, cmap='rainbow')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

"""Checando a quantidade de valores que foram classificados como outliers:"""

list(mascara).count(False)

"""## Como validar uma clusterização?

Temos dois tipos:
- Interna: Quanto bom foi o meu agrupamento?
- Externa: Como parecido estão os meus dois algoritmos comparados?

### Avaliando o Desempenho dos Algoritmos

### Tipo Externo:

(a) Usando o **Adjusted Rand Index**

Compara o desempenho quando forem fornecidos datasets com labels geradas de forma aleatória. Quando essas labels estão muito diferente, o valor se aproxima de 0, o que sugere um resultado negativo, ou seja, clusters não próximos.

Comparação entre K-Means e DBSCAN:
"""

adjusted_rand_score(kmeans_labels, dbscan_labels)

"""#### Tipo interno:

(b) Avaliando a métrica de **Silhouette**

Mede o formato do cluster obtido: avalia a distância entre os centros dos clusters, nesse caso, queremos maximizar as distâncias)

Valores próximos a -1, significa clusters ruins, próximo a 1, clusters bem separados.

### KMEANS:
"""

silhouette_score(dados[['Annual Income (k$)', 'Spending Score (1-100)']], kmeans_labels)

"""### DBSCAN:"""

silhouette_score(dados[['Annual Income (k$)', 'Spending Score (1-100)']],dbscan_labels)