# pip install python-docx transformers torch

from docx import Document
from transformers import pipeline
import os

summarizer = pipeline("summarization")

def read_docx(docx_path):
    document = Document(docx_path)
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def summarize_text(text, max_length=200, min_length=80, do_sample=False):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]["summary_text"]

def save_summary_to_text(summary_text, txt_path):
    with open(txt_path, "w") as file:
        file.write(summary_text)

if __name__ == "__main__":
    # docx_path = "documento.docx"
    # docx_path = "historia_mario.docx"
    # docx_path = "historia_mario_extenso.docx"
    docx_path = "historia_sapato_ano_novo.docx"
    txt_path = "resumo.txt"

    full_text = read_docx(docx_path)
    summary = summarize_text(full_text)
    save_summary_to_text(summary, txt_path)

    print("Sumarização completa. O resumo foi salvo em 'resumo.txt'.")
