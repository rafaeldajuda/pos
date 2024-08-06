# FASE 3 - IA GENERATIVAS - FUNDAMENTOS DA IA GENERATIVA

A natureza inspirou muitas criações para os seres humanos, tais como as aves nos inspiraram a voar com os aviões, a planta bardana inspirou a criação do velcro e o cérebro humano inspirou a criação das chamadas “Redes Neurais Artificiais” (RNA), consideradas como aprendizado profundo. As redes neurais artificiais são poderosas e escaláveis, sendo muito utilizadas para lidar com grandes tarefas altamente complexas do aprendizado de máquina, tais como classificação de imagens, reconhecimento de fala, criação de imagens, chats poderosos e até mesmo o aprendizado de jogar videogames.

Para aprender sobre IA generativa, é preciso conhecer muito bem os fundamentos de deep learning e processamento de linguagem natural. Conhecer os fundamentos possibilita compreender como os modelos generativos são criados e como chegamos nessa evolução. Nesta aula, você vai aprender sobre as principais técnicas que possibilitaram a evolução desses modelos. Vamos lá? 

Que tal aprender na prática como funciona um modelo de deep learning? Nessas aulas, você vai aprender na prática com o python como funcionam os embeddings e as deep learnings.

## Entendendo a motivação

**Motivação Biológica**

![imagem](./img/fase3_ia_aula2_1.png)

![imagem](./img/fase3_ia_aula2_2.png)

![imagem](./img/fase3_ia_aula2_3.png)

## Redes neurais - multilayer perceptron

![imagem](./img/fase3_ia_aula2_4.png)

![imagem](./img/fase3_ia_aula2_5.png)

![imagem](./img/fase3_ia_aula2_6.png)

![imagem](./img/fase3_ia_aula2_7.png)

![imagem](./img/fase3_ia_aula2_8.png)

![imagem](./img/fase3_ia_aula2_9.png)

![imagem](./img/fase3_ia_aula2_10.png)

![imagem](./img/fase3_ia_aula2_11.png)

![imagem](./img/fase3_ia_aula2_12.png)

**Critérios de parada da rede:**

**Epochs:** São o total de vezes que são executadas as redes neurais. (Número máximo de épocas).<br/>
**Batch:** Conjunto de instâncias de rede neural (número de exemplos de treinamento utilizados). Valor limite à **taxa de erro mínima** previamente estabelecida.

## Funcionamento matemático

![imagem](./img/fase3_ia_aula2_13.png)

![imagem](./img/fase3_ia_aula2_14.png)

![imagem](./img/fase3_ia_aula2_15.png)

![imagem](./img/fase3_ia_aula2_16.png)

![imagem](./img/fase3_ia_aula2_17.png)

![imagem](./img/fase3_ia_aula2_18.png)

## Funções de ativações

![imagem](./img/fase3_ia_aula2_19.png)

O objetivo de uma função de ativação é realizar a **transformação não linear** dos neurônios, aliás uma rede neural sem a função de ativação é essencialmente um modelo de regressão linear.

A função de ativação permite que as mudanças realizadas nos pesos e bias causam uma alteração na saída final do modelo (output).

### Sigmóide

![imagem](./img/fase3_ia_aula2_20.png)

### Tangente hiperbólica (tanh)

![imagem](./img/fase3_ia_aula2_21.png)

### ReLU (unidade linear retificada)

![imagem](./img/fase3_ia_aula2_22.png)

### Leaky ReLU

![imagem](./img/fase3_ia_aula2_23.png)

### Softmax

![imagem](./img/fase3_ia_aula2_24.png)

## Gradiente descendente

A descida do gradiente é um algoritmo de otimização para encontrar os valores de parâmetros (pesos) de uma função que minimizar uma função de custo.

![imagem](./img/fase3_ia_aula2_25.png)

Pensando na questão de matemática por trás dos gradientes, podemos dizer que o gradiente descendente é a **derivada da função do erro** em relação a nosso peso.

![imagem](./img/fase3_ia_aula2_26.png)

## Taxa de aprendizagem

Taxa de aprendizagem controla o tamanho do passo em cada iteração.

![imagem](./img/fase3_ia_aula2_27.png)

## Tipos de gradiente

**Momentum:** O Momentum é uma técnica que visa melhorar o desempenho do Gradiente Descendente, adicionando um componente de inércia ao algoritmo. Isso significa que as atualizações dos parâmetros consideram não apenas o gradiente atual, mas também as atualizações anteriores.

**AdaGrad (Adaptive Gradient):** O AdaGrad é um algoritmo que ajusta automaticamente o passo de aprendizagem para cada parâmetro do modelo. Isso significa que os parâmetros com gradientes mais suaves recebem passos de aprendizagem menores, enquanto os parâmetros com gradientes mais acentuados recebem passos maiores.

**Adaptative moment estimation (Adam):** Combina as ideia do Momentum e do RMSProp: assim como a otimização de momentum, o Adam acompanha uma média exponencialmente decadente de gradientes passados, e assim como o RMSProp, controla um média exponencialmente decadente de gradiente quadrados passados.

O otimizador Adam requer menos configurações de hiperparâmetros da taxa de aprendizagem, então um valor padrão n=0,001 pode ser uma boa opção.

![imagem](./img/fase3_ia_aula2_28.png)
