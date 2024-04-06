from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Dados de exemplo
textos = [
    "Novo jogo de RPG",
    "Conheça esses alongamentos",
    "Aprenda a fazer bolos",
    "Chegou o campeonato de jogos",
    "Alongamentos para pernas",
    "Receitas gostosas",
]
categorias = ["games", "saúde", "culinária", "games", "saúde", "culinária"]

# Convertendo textos em uma matriz de contagens de tokens
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, categorias, test_size=0.5, random_state=42)
print(X_train, X_test, y_train, y_test)
print(X_train.toarray())

X_string = vectorizer.inverse_transform(X_train)
print("X_train", X_string)
X_string = vectorizer.inverse_transform(X_test)
print("X_test", X_string)

# Treinando o classificador
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Predição e Avaliação
y_pred = clf.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")


