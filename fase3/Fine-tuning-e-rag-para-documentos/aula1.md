# FASE 3 - FINE-TUNING E RAG PARA DOCUMENTOS - PREPARANDO OS DADOS PARA FINE-TUNING

Já parou para pensar que os grandes modelos de linguagem conhecidos como LLMs (Large Language Models) são treinados com uma quantidade imensa de dados? O GPT-4 da OpenAI, por exemplo, foi treinado com praticamente todo o conteúdo da internet aberta. Mas não basta coletar os dados brutos, é preciso também realizar a limpeza e preparação para que o conteúdo esteja no formato de dados exigido pelo modelo escolhido.

Nesta aula, vamos abordar o tópico de pré-processamento de dados brutos, para formatá-los de maneira que o modelo escolhido possa compreender e aprender a partir do dataset.  

Então, vamos à prática! Nosso objetivo nesta aula será extrair os conteúdos dos artigos de notícias deste site (https://edition.cnn.com/world) e tratar esses dados para construir o dataset e para que o nosso modelo aprenda com base neles. Mas, para facilitar o processo, também vamos utilizar um dataset complementar, com mais de 10 mil artigos de diversas fontes. 

Primeiramente, é necessário configurar nosso ambiente de desenvolvimento. Para essa disciplina, vamos usar o Google Colab, uma ferramenta do Google baseada em Jupyter Notebooks, onde é possível utilizar diferentes hardwares, como CPU e GPU, para impulsionar nossa eficiência e tempo de processamento computacional. Se você nunca usou o Google Colab, acesse o link (https://colab.research.google.com/) e crie sua conta. Caso deseje ainda mais processamento, o Colab oferece um plano “Pro”, que disponibiliza hardwares mais avançados e que diminuem o tempo de execução. 

Recomendo que já realize o download do repositório da disciplina aqui (https://github.com/enricoferraz/fine-tuning-rag-documentos-fiap), bem como do dataset complementar (https://huggingface.co/datasets/glnmario/news-qa-summarization) e estude sua estrutura.

Com o Colab configurado, crie um arquivo e execute os seguintes comandos para instalar as dependências que vamos utilizar nessa aula. As demais bibliotecas utilizadas já são built-in da linguagem Python.

```sh
!pip install beautifulsoup4
!pip install openai
!pip install requests
```

Pronto! Seu ambiente já contém tudo que será preciso para esta aula. Agora, assista aos vídeos dessa aula para executar os scripts disponibilizados e vamos extrair e estruturar nossos dados para preparar o dataset!
            
