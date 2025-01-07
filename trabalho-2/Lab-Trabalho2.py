# Objetivo do Programa: Realizar operações dado um conjunto de dados de alunos contendo nome e nota
# Nome da Dupla: Luiz Viana e Wesley Ferreira
# Turma: EA
# Data da Criação: 28/12/2024

import statistics, copy

MSG_SELECAO_OPCAO = "\nDigite a sua opção:\n" \
    "1. Máxima; Mínima; Média; Desvio Padrão; Mediana; Primeira Moda;\n" \
    "2. Apresentar relação de alunos e notas (ordenado por notas) dentro de faixa de valores (máximo e mínimo);\n" \
    "3. Apresentar relação de alunos e respectivas notas (ordenado por nomes) cujos nomes contenham uma certa string (caso a entrada seja vazia, obterá todos os nomes);\n" \
    "4. Apresentar uma relação de notas e o número de suas ocorrências para uma faixa de valores (máximo e mínimo);\n" \
    "5. Incluir um novo aluno/nota\n" \
    "6. Sair\n\n" \
    "Opção: "

# Inicializa as listas que serão utilizadas ao longo do programas
matriz_alunos = [[],[]]
matriz_alunos_ord_nota = []
matriz_alunos_ord_nome = []

# Obtem a primeira nota do aluno
nota_aluno = float(input('Nota: '))

# Só obtem o nome do aluno caso a nota seja positiva
if nota_aluno >= 0:
    nome_aluno = input('Aluno: ')

# Loop de adição de notas e nomes de alunos
while nota_aluno >= 0:
    matriz_alunos[0].append(nota_aluno)
    matriz_alunos[1].append(nome_aluno.upper())
    
    nota_aluno = float(input('Nota: '))

    if nota_aluno >= 0:
        nome_aluno = input('Aluno: ')

# Permite que as opções sejam executadas somente se o número máximo de alunos
# seja maior que zero
if len(matriz_alunos[0]) > 0:

    # Exibe e lê as opções possíveis
    opcao = int(input(MSG_SELECAO_OPCAO))

    # Enquanto a opção for diferente de 6 (Sair) permanece no loop
    while opcao != 6:

        # Máxima; Mínima; Média; Desvio Padrão; Mediana; Primeira Moda;
        if opcao == 1:

            # Verifica se já houve ordenação por nota para as notas e nomes dos alunos
            if not matriz_alunos_ord_nota:

                # Copia os valores da matriz de alunos para serem ordenados em outra matriz
                matriz_alunos_ord_nota = copy.deepcopy(matriz_alunos)

                # Realiza a ordenação por seleção
                for i in range(len(matriz_alunos_ord_nota[0]) - 1):
                    for j in range(i + 1, len(matriz_alunos_ord_nota[0])):

                        # Caso o valor atual seja maior que um valor futuro, realiza a operação
                        # de troca de posições
                        if matriz_alunos_ord_nota[0][j] < matriz_alunos_ord_nota[0][i]:

                            # Troca o valor maior pelo menor baseando-se nas notas
                            tmp = matriz_alunos_ord_nota[0][i]
                            matriz_alunos_ord_nota[0][i] = matriz_alunos_ord_nota[0][j]
                            matriz_alunos_ord_nota[0][j] = tmp
                            
                            # Realiza a mesma operação para o nome para se ater a conformidade
                            # entre a posição das listas
                            tmp = matriz_alunos_ord_nota[1][i]
                            matriz_alunos_ord_nota[1][i] = matriz_alunos_ord_nota[1][j]
                            matriz_alunos_ord_nota[1][j] = tmp   

            # Definindo o valor máximo das notas a partir do último item da lista ordenada
            maximo = matriz_alunos_ord_nota[0][len(matriz_alunos_ord_nota[0]) - 1]

            # Definindo o valor mínimo das notas a partir do primeiro item da lista ordenada
            minimo = matriz_alunos_ord_nota[0][0]

            # Definindo o valor inicial do somatório de notas
            somatorio_notas = 0.0

            # Obtendo o somatório de todas as notas para o cálculo da média
            for nota in matriz_alunos_ord_nota[0]:
                somatorio_notas += nota

            # Definindo a média aritmética das notas
            media = somatorio_notas / len(matriz_alunos_ord_nota[0])

            # Inicializando o desvio padrão como zero para o caso de haver 
            # somente uma nota registrada
            desvio_padrao = 0.0

            # Obtendo o desvio padrão através da lib statistics caso haja mais de
            # uma nota registrada
            if len(matriz_alunos_ord_nota[0]) > 1:
                desvio_padrao = statistics.stdev(matriz_alunos_ord_nota[0])
            
            # Inicializando o valor da mediana
            mediana = 0

            # Definindo o primeiro índice utilizado para o cálculo da mediana
            indice_med_1 = int(len(matriz_alunos_ord_nota[0]) / 2) - 1

            # Verificando se o total de notas é par
            if len(matriz_alunos_ord_nota[0]) % 2 == 0:

                # Adicionando um seguindo índice para o cálculo da mediana em 
                # séries com quantidades de itens par
                indice_med_2 = indice_med_1 + 1

                # Calculando a média aritmética entre as notas referentes aos
                # índices centrais
                mediana = (matriz_alunos_ord_nota[0][indice_med_1] + 
                           matriz_alunos_ord_nota[0][indice_med_2]) / 2
                
            else:
                # Calculando a mediana para séries com quantidades de itens
                # ímpares
                mediana = matriz_alunos_ord_nota[0][indice_med_1 + 1]

            # Definindo os valores que serão utilizados para realização do 
            # cálculo da(s) primeira(s) moda(s)
            nota_anterior = matriz_alunos_ord_nota[0][0]
            primeira_moda = 0
            matriz_primeira_moda = [[],[]]

            # Itera sobre as notas registradas
            for nota in matriz_alunos_ord_nota[0]:
                if nota_anterior == nota:
                    # Caso a nota anterior seja IGUAL a nota atual, incrementa a
                    # moda em +1 (indicando repetição de itens)
                    primeira_moda += 1
                else:
                    # Caso a nota anterior seja DIFERENTE da nota atual, adiciona
                    # novos itens às listas de notas, atualiza a nota anterior e
                    # inicializa a primeira moda com 1 incrementado
                    matriz_primeira_moda[0].append(nota_anterior)
                    matriz_primeira_moda[1].append(primeira_moda)
                    nota_anterior = nota
                    primeira_moda = 1
            
            # Adiciona o último registro referente a primeira moda
            matriz_primeira_moda[0].append(nota_anterior)
            matriz_primeira_moda[1].append(primeira_moda)


            # Realiza a ordenação dos registros de todas as modas
            for i in range(len(matriz_primeira_moda[1]) - 1):
                for j in range(i + 1, len(matriz_primeira_moda[1])):
                    if matriz_primeira_moda[1][j] > matriz_primeira_moda[1][i]:
                        tmp = matriz_primeira_moda[1][i]
                        matriz_primeira_moda[1][i] = matriz_primeira_moda[1][j]
                        matriz_primeira_moda[1][j] = tmp

                        tmp = matriz_primeira_moda[0][i]
                        matriz_primeira_moda[0][i] = matriz_primeira_moda[0][j]
                        matriz_primeira_moda[0][j] = tmp


            # Coleta TODAS primeiras modas
            moda_anterior = matriz_primeira_moda[1][0]
            contador_modas = 1
            for i in range(1, len(matriz_primeira_moda[1])):
                if moda_anterior == matriz_primeira_moda[1][i]:
                    contador_modas += 1

            # Exibindo os resultados
            print('Máximo:', maximo)
            print('Mínimo:', minimo)
            print('Média:', media)
            print('Desvio Padrão:', desvio_padrao)
            print('Mediana:', mediana)
            print('Primeira(s) Moda(s):')

            # Itera sobre o resultado da(s) primeira(s) moda(s) e as exibe
            for i in range(contador_modas):
                print('\tNota:', matriz_primeira_moda[0][i],
                    '\tPrimeira Moda:', matriz_primeira_moda[1][i])
                
        # Apresentar relação de alunos e notas (ordenado por notas) dentro de faixa de valores (máximo e mínimo);
        elif opcao == 2:
            
            # 🚨 Por que repetir código aqui? Pensando em realizar somente as operações necessárias
            # e na restrição quanto ao uso de funções, decidimos repetir este código para que
            # o usuário só realize a ordenação que for necessária para opção selecionada

            # Verifica se já houve ordenação por nota para as notas e nomes dos alunos
            if not matriz_alunos_ord_nota:

                # Copia os valores da matriz de alunos para serem ordenados em outra matriz
                matriz_alunos_ord_nota = copy.deepcopy(matriz_alunos)

                # Realiza a ordenação por seleção
                for i in range(len(matriz_alunos_ord_nota[0]) - 1):
                    for j in range(i + 1, len(matriz_alunos_ord_nota[0])):

                        # Caso o valor atual seja maior que um valor futuro, realiza a operação
                        # de troca de posições
                        if matriz_alunos_ord_nota[0][j] < matriz_alunos_ord_nota[0][i]:

                            # Troca o valor maior pelo menor baseando-se nas notas
                            tmp = matriz_alunos_ord_nota[0][i]
                            matriz_alunos_ord_nota[0][i] = matriz_alunos_ord_nota[0][j]
                            matriz_alunos_ord_nota[0][j] = tmp
                            
                            # Realiza a mesma operação para o nome para se ater a conformidade
                            # entre a posição das listas
                            tmp = matriz_alunos_ord_nota[1][i]
                            matriz_alunos_ord_nota[1][i] = matriz_alunos_ord_nota[1][j]
                            matriz_alunos_ord_nota[1][j] = tmp   

            # Recebe os valores referentes ao mínimo e ao máximo da faixa desejada
            min = float(input("Mínimo: "))
            max = float(input("Máximo: "))

            # Inicializa variável condicional para exibição de mensagem de erro caso não existam valores
            # na faixa recebida pelo terminal
            possui_valores_na_faixa = False

            # Itera pelas notas ordenadas registrada
            for i in range(len(matriz_alunos_ord_nota[0])):

                # Caso a nota esteja na faixa desejada, exibe o registro
                if matriz_alunos_ord_nota[0][i] >= min and matriz_alunos_ord_nota[0][i] <= max:
                    print('\tNota:', matriz_alunos_ord_nota[0][i], '\tNome:', matriz_alunos_ord_nota[1][i])
                    possui_valores_na_faixa = True

            if not possui_valores_na_faixa:
                print('Nenhum resultado encontrado para a faixa especificada')

        # Apresentar relação de alunos e respectivas notas (ordenado por nomes) cujos nomes contenham uma certa string (caso a entrada seja vazia, obterá todos os nomes);
        elif opcao == 3:

            # Verifica se já houve ordenação por nome para as notas e nomes dos alunos
            if not matriz_alunos_ord_nome:

                # Copia os valores da matriz de alunos para serem ordenados em outra matriz
                matriz_alunos_ord_nome = copy.deepcopy(matriz_alunos)

                # Realiza a ordenação por seleção
                for i in range(len(matriz_alunos_ord_nome[1]) - 1):
                    for j in range(i + 1, len(matriz_alunos_ord_nome[1])):

                        # Caso o valor atual seja maior que um valor futuro, realiza a operação
                        # de troca de posições
                        if matriz_alunos_ord_nome[1][j] < matriz_alunos_ord_nome[1][i]:

                            # Troca o valor maior pelo menor baseando-se nos nomes
                            tmp = matriz_alunos_ord_nome[1][i]
                            matriz_alunos_ord_nome[1][i] = matriz_alunos_ord_nome[1][j]
                            matriz_alunos_ord_nome[1][j] = tmp
                            
                            # Realiza a mesma operação para a nota para se ater a conformidade
                            # entre a posição das listas
                            tmp = matriz_alunos_ord_nome[0][i]
                            matriz_alunos_ord_nome[0][i] = matriz_alunos_ord_nome[0][j]
                            matriz_alunos_ord_nome[0][j] = tmp   
                        
            padrao = input("Padrão: ").upper()
            possui_valores_na_faixa = False

            for i in range(len(matriz_alunos_ord_nome[1])):
                nome = matriz_alunos_ord_nome[1][i]
                nota = matriz_alunos_ord_nome[0][i]
                if padrao in nome:
                    print('\tNota:', nota, '\tNome:', nome)
                    possui_valores_na_faixa = True
            
            if not possui_valores_na_faixa:
                print('Nenhum resultado encontrado para a faixa especificada')

        # Apresentar uma relação de notas e o número de suas ocorrências para uma faixa de valores (máximo e mínimo);
        elif opcao == 4:
            
            # 🚨 Por que repetir código aqui? Pensando em realizar somente as operações necessárias
            # e na restrição quanto ao uso de funções, decidimos repetir este código para que
            # o usuário só realize a ordenação que for necessária para opção selecionada

            # Verifica se já houve ordenação por nota para as notas e nomes dos alunos
            if not matriz_alunos_ord_nota:

                # Copia os valores da matriz de alunos para serem ordenados em outra matriz
                matriz_alunos_ord_nota = copy.deepcopy(matriz_alunos)

                # Realiza a ordenação por seleção
                for i in range(len(matriz_alunos_ord_nota[0]) - 1):
                    for j in range(i + 1, len(matriz_alunos_ord_nota[0])):

                        # Caso o valor atual seja maior que um valor futuro, realiza a operação
                        # de troca de posições
                        if matriz_alunos_ord_nota[0][j] < matriz_alunos_ord_nota[0][i]:

                            # Troca o valor maior pelo menor baseando-se nas notas
                            tmp = matriz_alunos_ord_nota[0][i]
                            matriz_alunos_ord_nota[0][i] = matriz_alunos_ord_nota[0][j]
                            matriz_alunos_ord_nota[0][j] = tmp
                            
                            # Realiza a mesma operação para o nome para se ater a conformidade
                            # entre a posição das listas
                            tmp = matriz_alunos_ord_nota[1][i]
                            matriz_alunos_ord_nota[1][i] = matriz_alunos_ord_nota[1][j]
                            matriz_alunos_ord_nota[1][j] = tmp   
            
            # Recebe os valores referentes ao mínimo e ao máximo da faixa desejada
            min = float(input("Mínimo: "))
            max = float(input("Máximo: "))

            # Inicializa a lista de notas filtradas
            nota_aluno_list_filtrada = []

            # Para cada nota, caso esteja na faixa escolhida, adiciona um valor para a nota filtrada
            for nota in matriz_alunos_ord_nota[0]:
                if nota >= min and nota <= max:
                    nota_aluno_list_filtrada.append(nota)

            # Verifica se existe itens na lista filtrada
            if nota_aluno_list_filtrada != []:

                # Inicializa a frequência e a nota anterior
                frequencia = 0
                nota_anterior = nota_aluno_list_filtrada[0]

                # Itera pelas notas filtradas
                for nota in nota_aluno_list_filtrada:
                    if nota == nota_anterior:
                        # Verifica se a nota é igual à nota anterior e incremente 1 a frequência caso seja
                        frequencia += 1
                    else:
                        # Exibe a nota seguida da frequência, inicializa a frequência com 1 incrementado
                        # e atualiza o valor da nota anterior
                        print('\tNota:', nota_anterior, '\tFrequência:', frequencia)
                        frequencia = 1
                        nota_anterior = nota
                
                # Exibe o último par nota-frequência que restou
                print('\tNota:', nota_anterior, '\tFrequência:', frequencia)
            else:
                # Caso não acha notas dentro da faixa, exibe uma mensagem de erro
                print('Nenhum resultado encontrado para a faixa especificada.')

        # Incluir um novo aluno/nota
        elif opcao == 5:

            # Recebe uma nota do terminal e converte para ponto flutuante
            nota_aluno = float(input('Nota: '))

            if nota > 0:
                # Caso a nota seja maior que zero, inicaliza os valores necessários 
                # tal qual o ínicio do programa
                nome_aluno = input('Nome: ')
                matriz_alunos[0].append(nota_aluno)
                matriz_alunos[1].append(nome_aluno.upper())
                matriz_alunos_ord_nota = []
                matriz_alunos_ord_nome = []
            else:
                print('Opção inválida! Não é possível criar um novo registro com nota negativa. Tente novamente com uma opção válida!')
        else:
            print("Opção inválida! Tente novamente, por gentileza...")
        
        opcao = int(input(MSG_SELECAO_OPCAO))
else:
    # Tratamento para o caso da primeira entrada de nota do aluno ser negativa
    print('Atenção! Nenhum aluno cadastrado, não é possível realizar nenhuma operação!')