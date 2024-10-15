from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

# Carregar arquivo
# file = open("frases_classificadas_sem_repeticao.txt", "r")
# frases = file.read()
# file.close()

# Formatar frases
# frases = frases.split("\n")
# frases_classificadas = [frase.split(" - ") for frase in frases]

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

# Enriquecer dados
# for frase, classificacao in frases_classificadas:
#     texts.append(frase)
#     labels.append(classificacao)
# print(f"texts: {len(texts)}\nlabels: {len(labels)}")

# Dividir os dados em conjuntos de treinamento e tes
X_train, X_test, y_train, y_test = train_test_split(texts, labels, random_state=42)

# Criar um pipeline de transformação de texto e classificação/Treinar o modelo/# Fazer previsões no conjunto de teste
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
labels_predicted = model.predict(X_test)

# Avaliar o modelo
print(metrics.classification_report(y_test, labels_predicted, zero_division=0))

# Classificar novos texto
new_texts = ["Eu preciso aprender Python", "Eu quero aprender Python", "A pizza está deliciosa", "O online do jogo crash é demais"]
new_labels_predicted = model.predict(new_texts)
print(new_labels_predicted)