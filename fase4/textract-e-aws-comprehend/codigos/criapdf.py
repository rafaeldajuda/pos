# pip install reportlab
# pip install boto3

# o acesso ao aws pode dar problema, para resolver vai ser criar um ID do seu aws
# criar id:
# https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/security_credentials
# para instalar o aws:
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
# comandos para configurar:
# aws configure list
# aws configure

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen  import canvas
import boto3

def create_investiment_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Relatório de Investimentos")

    c.setFont("Helvetica", 12)
    investiments = [
        {"Investidor": "João Silva", "Tipo": "Ações", "Valor": "R$ 10.000", "Data": "01/01/2024"},
        {"Investidor": "Maria Oliveira", "Tipo": "Fundos Imobiliários", "Valor": "R$ 5.000", "Data": "15/02/2024"},
        {"Investidor": "Carlos Souza", "Tipo": "Tesouro Direto", "Valor": "R$ 8.000", "Data": "20/03/2024"},
    ]

    y = 720
    for inv in investiments:
        c.drawString(100, y, f"Investidor: {inv['Investidor']}")
        c.drawString(100, y-15, f"Tipo de Investimento: {inv['Tipo']}")
        c.drawString(100, y-30, f"Valor Investido: {inv['Valor']}")
        c.drawString(100, y-45, f"Data do Investimento: {inv['Data']}")
        y -= 75
    
    c.save()

pdf_file_path = "relatorio_investimentos.pdf"

create_investiment_pdf(pdf_file_path)

s3 = boto3.client('s3')
bucket_name = 'rafael-aulafiap'
object_name = pdf_file_path

s3.upload_file(pdf_file_path, bucket_name, object_name)

print(f"PDF {pdf_file_path} carregado com sucesso para s3://{bucket_name}/{object_name}")
