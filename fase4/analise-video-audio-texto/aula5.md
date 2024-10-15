# FASE 4 - ANALISE VIDEO AUDIO TEXTO - CLASSIFICAÇÃO DE TÓPICOS E CATEGORIZAÇÃO DE TEXTO

Nesta aula, você explorará conceitos fundamentais de categorização e classificação de dados. Primeiro, você entenderá o conceito de categorização, que envolve agrupar dados em categorias distintas com base em características comuns. 
            
Em seguida, aprenderá sobre a classificação supervisionada, em que modelos são treinados com dados rotulados para prever categorias de novos dados. Também abordaremos a classificação não supervisionada, que envolve agrupar dados não rotulados em clusters com base em suas similaridades. 

E, finalmente, você implementará um projeto prático que utiliza esses conceitos para classificar textos, aplicando técnicas de machine learning para agrupar e identificar diferentes tipos de conteúdo textual. Esta experiência prática consolidará seu entendimento teórico e fornecerá habilidades aplicáveis a diversas áreas de análise de dados e inteligência artificial.

Nesta aula entenderemos como classificar e categorizar textos de acordo com uma técnica supervisionada e uma técnica não supervisionada. Agora, vamos repassar os dois projetos que fizemos e entender suas saídas. Para esses projetos vamos precisar instalar três bibliotecas.

Código 1:
```sh
pip install scikit-learn
pip install gensim
pip install nltk
```

supervisioned_classifier.py
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

# Dados de exemplo mais robustos
texts = [
    "Eu amo programar em Python", "A máquina de lavar está quebrada", "Eu gosto de pizza", 
    "Python é uma linguagem de programação", "Eu preciso consertar minha máquina de lavar",
    "Pizza é minha comida favorita", "Estou aprendendo a programar", "O forno está quebrado",
    "Eu amo pizza de pepperoni", "A geladeira parou de funcionar", "O curso de Python é ótimo",
    "Preciso de um técnico para consertar minha geladeira", "A pizza de marguerita é deliciosa",
    "Eu gosto de aprender novas linguagens de programação", "O conserto do micro-ondas foi caro"
]

labels = [
    "tecnologia", "doméstico", "comida", "tecnologia", "doméstico", "comida", 
    "tecnologia", "doméstico", "comida", "doméstico", "tecnologia", "doméstico",
    "comida", "tecnologia", "doméstico"
]

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Criar um pipeline de transformação de texto e classificação
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predicted_labels = model.predict(X_test)

# Avaliar o modelo
print(metrics.classification_report(y_test, predicted_labels, zero_division=0))

# Classificar novos textos
new_texts = ["Eu preciso aprender Python", "A pizza está deliciosa"]
predicted_new_labels = model.predict(new_texts)
print(predicted_new_labels)
```

unsupervisioned_classifier.py
```python
import gensim
from gensim import corpora
import nltk
from nltk.corpus import stopwords

# Baixar stopwords se ainda não tiver feito
nltk.download('stopwords')

# Dados de exemplo
documents = [
    "Eu amo programar em Python",
    "A máquina de lavar está quebrada",
    "Eu gosto de pizza",
    "Python é uma linguagem de programação",
    "Eu preciso consertar minha máquina de lavar",
    "Pizza é minha comida favorita",
    "Estou aprendendo a programar",
    "O forno está quebrado",
    "Eu amo pizza de pepperoni",
    "A geladeira parou de funcionar",
    "O curso de Python é ótimo",
    "Preciso de um técnico para consertar minha geladeira",
    "A pizza de marguerita é deliciosa",
    "Eu gosto de aprender novas linguagens de programação",
    "O conserto do micro-ondas foi caro"
]

# Pré-processamento de texto
stop_words = stopwords.words('portuguese')
texts = [[word for word in document.lower().split() if word not in stop_words] for document in documents]

# Criar um dicionário e corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Treinar o modelo LDA
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

# Exibir os tópicos
for idx, topic in lda_model.print_topics(-1):
    print('Tópico: {} 
Palavras: {}'.format(idx, topic))
```
            
            