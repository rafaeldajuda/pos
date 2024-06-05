# FASE 2 - AULA 1 - INTRODUÇÃO AO DESENVOLVIMENTO DE APRENDIZADO DE MÁQUINA (ML) NA NUVEM

* Aprendizado de máquina é estudado desde do século XX.
* O aprendizado de máquina está em tudo lugar, mesmo que seja só em uma parte de um processo. Pode estar no seu celular, casa ou carro. Por exemplo, em fábricas onde é produzido parafusos é possível utilizar o aprendizado de máquina para checar a qualidade dos parafusos que estão sendo produzidos.
* Empresas de todos os tamanhos utilizam o ML, como Google, Amazon, Microsift, ... Utlizando para melhorar seus produtos e serviços. 
* O aprendizado de máquina entra onde não é possível (ou viável) utilizar um sotfware mais tradicional. Por exemplo, fazer um programa para identificar uma maçã. Uma maçã possui várias características difícies de se programar, como tamanho, formato e variação da cor vermelha.
* Quando algo possui padrões complexos é interessante utilizar o ML. Exemplos de padrões complexos:
    * Padrões Complexos
        - Detecções
            - Spam
            - Fraudes
            - Doenças
        - Reconhecimentos
            - Imagens
            - Voz
        - Previsões
            - Demandas
            - Climática

* Ambiente de desenvolviemnto local, normalmente é o ambiente de inicial para se desenvolver, porém possui limitações, como por exemplo, potência da máquina, risco de perder os dados coletados, dependência da infraestrutura local onde existe o risco de cair a internet, e entre outros.

## Etapas para desenvolvimento de máquina

Para o desenvolvimento de máquina é preciso seguir vários passos, onde podem váriar de acordo com as circunstâcias, para conseguir chegar no modelo. Esse é um exemplo que etapas para criar um modelo.

* Coletar dados
    - Banco de dados
    - Websites
    - Arquivos Locais
* Pré-processamento
    - Limpeza dos dados
    - Conversão de formato
* Modelo
    No modelo é preciso escolher qual o melhor tipo de modelo se encaixa no problema.
    - Configução dos hiperparametros
    - Definição Tipo
        No exemplo da aula, onde um engenheiro precisa criar um modelo de tradução de inglês para português, o melhor tipo seria **Sequence-to-Sequence (Redes Recorrentes, Transformers)**
        
        |Sequência de entrada| -> |Sequence-to-Sequence| -> |Sequência de saída|
* Treinar e avaliar o modelo
    - Métricas de desempenho
        * Tradicionais:
            - Acurácia
            - Precisão
            - Recall
        * Textos
            - BLEU
            - METEOR
* Implantação
    - Disponibilizar para consumo
        * EX: Google Translate
* Monitoramento
    - Garantir
        * Sistema está online
        * Tempo de resposta
        * Qualidade dos resultados
            - Se as respostas estão corretas
* Necassárias iterações
    - É preciso passar pelas etapas novamente várias vezes pra checar no modelo ideal de acordo com as necessidades. Então é possível que para chegar no modelo ideal seja preciso coletar mais dados, utilizar um tipo de modelo diferente, mexer no hiperparametros, fazer novas avaliações.

## Ambiente de desenvolvimento na nuvem

* O que é a nuvem: é um conjunto de servidores disponibilizados por grandes empresas de tecnologias que podem ser alugados por terceiros. A importância é a disponibilidade de recurso computacional, por exemplo, em determinadas taferas de IA é possível que precise de muito recurso, mas após realização o recurso extra não é mais necessário. Nesse caso podemos alugar uma máquina na nuvem e depois delisga-la após o processo. Um outro exemplo é quando sites de ecommerce que precisam de servidores mais robustos em determinadas épocas do ano onde a movimentação dos sites é maior.
* Os recursos nomalmente são armazenamentos, processamento, rede (melhor conexão), e outros.
* Os Armazenamentos e processamentos são feitas de forma elástica, ou seja, quando a demanda é maior os recursos são aumentados, porém quando não são mais necessários os recursos voltam a diminuir.
* A nuvem também permite hardwares especializados, onde podemos ter uma máquina com recursos específicos. Por exemplo, podemos ter um modelo onde é necessário ter 16Gb de mémoria, mas a nossa máquina só possui 8Gb, a nuvem permite ter uma máquina específica para esse problema. Existem máquinas com foco em processamentos (GPUs ou TPUs), permitindo processar os dados de forma muita mais rápida.
* TPUs também são focados em processamnto paralelo (que nem as GPUs), porém seu foco é para apredizagem de máquina.
* A nuvem é um ótima solução para aprendizagem de máquina.

## Em que a nuvem ajuda no aprendizado de máquina

* Coleta de dados e armazenamento: Após coletar os dados para o modelo é preciso armazena-los em algum lugar. Armazenar em um ambiente local é confortável, porém existe riscos, como, podemos perde-los, custo em compra de HDs/SSDs, ocupação física, etc. Na nuvem normalmente não precisamos nos preocupar com isso, pois tudo está centralizado, possui espaço "infinito" e existencia de backups.
    - coleta de dados
        * bando de dados
        * websites
        * arquivos locais
    - armazemanto
        * resistência a falhas
            - backup
        * espaço suficiente
        * centralizado
* Pré-processamento: Na fase de pré-processamento normalmente precisamtos fazer limpeza de dados, conversão de formatos e outras tarefas. Esses passos podem ser muitos custosos na parte de processamento em um ambiente local. Na nuvem os recurosos são escalaveis, aumentando quando for necessários. Também existe o ETL, que são um conjunto de ferramentas que permite trabalhar com um conjunto de dados de formatos diferentes em um só formato de dado.
* Modelo:  ao treinar o modelo precisamos seguir os seguintes passos (exemplo):
    - definição tipo
        * árvores de decisão
        * KNN
        * redes neurais
            - treinamento
    - hiperparametros
        * ajustes
    
    Todos esses passos são tarefas custosas, dependendo do tipo de modelo escolhido e como os hiperparametros estão configurados o custo de processamento podem ser muito altos e tempo de processamento também pode alto. Nesse caso ter um hardware mais especializado pouparia tempo para resolver esse problema.

    - nuvem
        * processamento paralelo
        * hardwares especilizado
            - GPUs
            - TPUs
        * alta disponibilidade

* Avalição: Apoós treinar o modelo é preciso aplicar métricas de desempenho. A avalição do modelo também pode ser bastante custoso, já que avalição precisa passar pelo modelo. Ao desenvolver na nuvem temos alguns benefícios no processo de avalição, como por exemplo, processamento paralelo, hardwares especializados, alta disponibilidade, centralizado, etc. 

    - métricas de desempenho
        * tradicionis
            - acurácia
            - precisão
            - recall
        * textos
            - BLEU
            - METEOR
        * tradicionis/textos
            - podem ser custosos, nesse caso a nuvem oferece as seguintes vantagens
                * processamento paralelo
                * hardwares especializados
                * alta disponibilidade
                * centralizado

* Implatação: Depois de passar pelas fases de desenvolvimento do modelo é preciso implantar e deixar o modelo disponível para uso. Nesse caso é fácil de entender o porque deixar o modelo na nuvem, pois ao deixar na nuvem o modelo vai estar 24h disponível, terá processos de pipeline para facilitar o deploy, pode ter interfaces e APIs, etc...

    - disponibilizar para consumo
        * exportar
        * API
        * interface
        * CI/CD

        * custoso
            - processamento paralelo
            - hardwares especializados
            - alta disponibilidade
            - segurança
            - armazenagem de dados

* Monitoramento: Com a implantação é preciso fazer depois, de forma constante, o monitoramento do modelo, avaliando como está as metricas de desempenho, se o serviço está online, o tempo de resposta ao cliente, se o modelo está atendendo o propósito inicial, a qualidade dos resultados, os drifts (é quando o modelo perde eficácia com o tempo com os novos dados ou pelo um novo conceito dos dados).

    - métricas
        * desempenho
            - sistema online
            - tempo de resposta
        * negócio
            - qualidades dos resultados
            - drifts
                * dados
                * conceito
        * centralizado

* Necessárias Interações: É muito importante repassar pelas fases novamente para sempre ter revisar o modelo criado e fazer ajustes para melhora-lo.
