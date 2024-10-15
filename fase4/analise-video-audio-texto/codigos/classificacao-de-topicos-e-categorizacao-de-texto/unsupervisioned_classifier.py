import gensim
from gensim import corpora
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

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

# Carregar arquivo
# file = open("frases_classificadas_sem_repeticao.txt", "r")
# frases = file.read()
# file.close()

# Formatar frases
# frases = frases.split("\n")
# frases_classificadas = [frase.split(" - ") for frase in frases]

# Enriquecer dados
# for frase, _ in frases_classificadas:
#     documents.append(frase)
# print(f"documents: {len(documents)}")

stop_words = stopwords.words("portuguese")
texts = [[word for word in document.lower().split() if word not in stop_words] for document in documents]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
