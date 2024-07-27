# OPERADORES GENÉTICOS: SELEÇÃO, CRUZAMENTO E MUTAÇÃO

Nesta aula, continuaremos nossa exploração prática criando os operadores genéticos de cruzamento e mutação. Além disso, trabalharemos na visualização dos resultados utilizando gráficos e uma interface gráfica para visualizar a melhor rota em tempo real usando Pygame.

Abordaremos o crossover, com destaque para o método Ordered (ox) aplicado ao “Problema do Caixeiro Viajante”, mostrando como os filhos são gerados. Discutiremos a customização da função de crossover, ressaltando sua dependência do indivíduo. Em seguida, exploraremos a mutação, focando no método Swap. Além disso, examinaremos a condição de término de um algoritmo genético.

Utilizaremos o Pygame para criar visualizações interativas dos resultados. Apresentaremos o Pygame, suas funções de criação de tela, controle de frames e as funções para desenhar as cidades e a melhor trajetória na tela.

Prepare-se para uma aula prática e dinâmica, explorando os detalhes dos operadores genéticos e visualizando os resultados em tempo real.

## OBSERVAÇÕES

**Função calculate_distance**: Está função calcula a distancia entre duas cidades (ou dois pontos). Existe uma forma mais eficiênte de calcular as distâncias, que é a "matriz de distância".