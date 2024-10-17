# FASE 4 - ANALISE VIDEO AUDIO TEXTO - SUMARIZAÇÃO AUTOMÁTICA DE DOCUMENTOS E ARTIGOS

Nesta aula, você explorará o conceito de sumarização, que envolve a criação de versões mais curtas de textos longos, mantendo as informações essenciais. Você também aprenderá a implementar um projeto prático que utiliza a biblioteca Transformers para sumarizar textos em documentos. 

Por meio  deste projeto, você desenvolverá um sistema que automaticamente gera resumos concisos, aplicando técnicas modernas de processamento de linguagem natural (NLP).
            
Nesta aula entenderemos como sumarizar documentos utilizando a biblioteca Transformers em conjunto com a biblioteca python-docx para manipulação de arquivos de tipo.docx. Para esse projeto, precisaremos instalar três bibliotecas, sendo a torch como dependência obrigatória da transformers.

```sh
pip install python-docx transformers torch
```

Código do script chamado “summarization.py”:

```python
from docx import Document
from transformers import pipeline
import os

# Inicializar o pipeline de sumarização
summarizer = pipeline("summarization")

def read_docx(docx_path):
    """
    Lê o texto de um documento .docx.
    :param docx_path: Caminho para o documento .docx
    :return: Texto completo do documento
    """
    document = Document(docx_path)
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return "
".join(full_text)

def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    """
    Função para sumarizar um texto.
    :param text: Texto a ser sumarizado
    :param max_length: Comprimento máximo do resumo
    :param min_length: Comprimento mínimo do resumo
    :param do_sample: Se True, usar amostragem; se False, usar truncagem
    :return: Resumo do texto
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']

def save_summary_to_txt(summary_text, txt_path):
    """
    Salva o resumo em um arquivo .txt.
    :param summary_text: Texto do resumo
    :param txt_path: Caminho para salvar o arquivo .txt
    """
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(summary_text)

if __name__ == "__main__":
    # Caminho para o documento .docx
    docx_path = 'documento.docx'  # Arquivo .docx
    txt_path = 'resumo.txt'  # Nome do arquivo de saída .txt

    # Ler o texto completo do documento
    full_text = read_docx(docx_path)
    
    # Sumarizar o texto completo
    summary = summarize_text(full_text, max_length=200, min_length=50)
    
    # Salvar o resumo em um arquivo .txt
    save_summary_to_txt(summary, txt_path)
    
    print("Sumarização completa. O resumo foi salvo em 'resumo.txt'.")
```

Lembrando que é necessário que o arquivo esteja na mesma pasta e caso ele tenha algum outro nome, você pode renomeá-lo ou alterar o código na variável “docx_path”.

Após isso, rode o projeto com o comando:

```sh
python summarization.py
```

Podemos observar que será gerado um arquivo de tipo .txt na pasta e que lá se encontrará o resumo do seu documento.
        
Lembre-se: caso queira que o seu resumo seja maior, altere os parâmetros “max_length” e “min_length” de acordo com sua necessidade. “Max_length” é a quantidade máxima de caracteres e “min_length” a quantidade mínima de caracteres Assim, o modelo vai entender esses limites.
        
Não deixe de praticar!
            