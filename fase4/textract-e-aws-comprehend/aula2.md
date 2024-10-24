# FASE 4 - TEXTRACT + AWS-COMPREHEND - EXTRAÇÃO DE TEXTO COM TEXTRACT

Nesta aula, você aprenderá como utilizar o Textract para automatizar a extração de texto e dados estruturados de documentos digitalizados. Exploraremos a configuração do ambiente, a criação e upload de documentos para o S3, e as boas práticas para garantir a qualidade e segurança dos dados processados.
            
Nesta aula, serão explicadas as etapas de uma extração de texto com a ferramenta Textract, a partir dos seguintes passos:

* Upload do Documento.
* Análise do Documento.
* Processamento da Resposta.
* Armazenamento e Uso dos Dados.

## Textract

**Armazenamento no S3**

* Propósito: Utilizado para guardar documentos de forma mais segura e acessível.
* Aplicação Real: Empresas podem utilizar o serviço para armazenar documentos digitais, como faturas financeiras ou extratos bancários.

**Geração de PDF**

* Propósito: Criação de PDF para simular um relatório de análise de investimento para realizar testes.
* Aplicação Real: Em um ambiente real vai exister documentos importantes, a geração de um documento de testes ajuda a testar o armazenamento no S3.

**Extração de Dados com Textract**

* Propósito: Utilizar os dados do PDF para automatizar a leitura dos documentos.
* Aplicação Real: As empresas podem utilizar o textract para digitalizar os documentos físicos e extrair as informações para realizar análises.

**Criação de Arquivo de Texto**

* Propósito: O arquivo PDF que será passado para texto pode ser utilizado no comprehend para análise de sentimentos.
* Aplicação Real: Os dados extraídos a partir do texto podem ser utilizados para outros processos já automatizados.

**Análise de Texto com Comprehend (próxima aula)**

* Propósito: O Comprehend é utilizado para processamento de linguagem natural (PLN), para analisar sentimentos.

---

Esse processo é uma ilustração de como empresas podem:

* Automatizar a gestão de documentos
* Melhorar a eficiência operacional 
* Aumentar a escabilidade
* Garantir a precisão e consistência
* Gerar insights valiosos
