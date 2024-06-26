# FASE 2 - AULA 2 - CRIANDO UM MODELO NO AZURE

## Criando um modelo no notebook na nuvem

1. Criar um conta no azure - https://portal.azure.com
2. Criar um grupo de recursos - É uma coleção de recursos que são agrupados em diferetes áreas. Então é ideal que para cada área de projeto se crie um grupo novo.
3. Criar um workspace - é onde fica todos os recursos do azure para o desenvolvimento.
    - Azure Machine Learning -> Criar -> Novo workspace -> examinar+criar -> criar -> Inicar Modelo
4. Criar um máquina virtual - computação -> instâncias de computação -> novo -> examinar+criar -> criar
5. Criar um notebook -> arquivos -> (+) sémbolo de mais -> criar
6. Seguir a video aula (ou pdf)

## Utilzando as ferramentas da nuvem

### Criando um script de treinamento

1. No workspace clicar em Dados -> Criar -> Avançar -> De um URI -> Avançar -> Preencher com o endereço com os dados -> Avançar -> Criar
2. Uma das vantagens de carregar os dados no Azure é que os dados sempre vão estar lá, assim podendo acessa-lo de forma remota.
3. Na aba Dados -> Consumir temos um exemplo de como acessar os dados.
4. Na aba Dados -> Explorar temos algumas informções do dados, como tamanho do arquivo, formato, campos nulos, etc.
5. Na aba Dados -> Trabalhos referência todos os modelos que estão utilizando os dados.
6. Para utlizar os dados para treinar modelos temos que criar as tarefas (ou jobs). Uma tarefa é um script que vai rodar em uma máquina virtual para treinar modelos e esses modelos terão um histórico de como eles foram treinados.
7. Antes de criar a tarefa é preciso criar o script de treinamento
8. Criar script de treinamento -> Notebooks -> arquivos -> (+) sémbolo de mais -> arquivo tipo python -> criar

### Criando uma tarefa

1. Antes de criar uma tarefa é preciso definir qual script vai ser usado e como o modelo vai ser treinado, além de outras definições.
2. A tarefa por der criado pela interface do azure (Tarefas) ou por código.
3. Criar uma tarefa -> Notebooks -> arquivo -> criar
4. Após a tarefa ser executada é preciso checar os dados logados
5. Na aba Visão Geral podemos os dados de entrada e sáida, as classes utilizadas, os parâmetros das funções, etc.
6. Na aba Métricas podemos ver as métricas de desempenho que foram calculadas durante o treinamento.
7. Na aba Imagens podemos ver todas as imagens que foram geradas, como gráficos por exemplo.
8. Na aba Saídas + logs é onde fica os logs do processo e qualquer outro tipo de saída, como o modelo.
9. Na aba código mostra os códigos utilizados durante o treinamento.

### Disponibilizando o modelo para consumo

1. Ir para opção Modelos.
2. Clicar no modelo desejado.
3. Implantar -> Ponto de estremidade em tempo real -> ajustar as configurações (se necessário) -> implantar
4. Ir para Pontos de extremidade para ver os modelos implantados.
5. Na aba Teste podemos testar o modelo
6. Na aba Consumir é onde tem instruções em como podemos integrar o modelo em sistemas externos através de uma API rest. 

### Limpeza de recursos

1. Remover dados ir para Dados -> selecionar os dados -> Arquivo morto -> Arquivo morto
2. Remover modelo ir para Pontos de extremidade -> selecionar modelo -> Excluir -> Excluir
3. Remover modelo que foi treinado ir para Modelos -> selecionar o modelo -> Excluir -> 
    O modelo só será removido quando o pontos de extremidade terminar sua exclusão.
4. Remover tarefas ir para Tarefas -> selecionar as tarefas -> Excluir -> Excluir
5. Remover a máquina ir para Computação -> selecionar a máquina -> Interromper
 
OBS:
* a função mlflow.start_run diz para o azure que uma nova experimentação está sendo feita. A partir dessa função tudo será registrado.
* A máquina de implantação tende a ser menor do que a máquina de treinamento, para treinar é preciso realizar vários testes.

## Dados

https://raw.githubusercontent.com/lucolivi/sentiment_analysis_dataset/main/dataset.csv

