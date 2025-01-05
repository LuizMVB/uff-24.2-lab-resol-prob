# Objetivo do Programa: Realizar operações dado um conjunto de dados de alunos contendo nome e nota
# Nome da Dupla: Luiz Miguel Viana Barbosa e Wesley Ferreira
# Turma: EA
# Data da Criação: 28/12/2024

import statistics

MSG_SELECAO_OPCAO = '''
Digite a sua opção:
1. Máxima; Mínima; Média; Desvio Padrão; Mediana; Primeira Moda;
2. Apresentar relação de alunos e notas (ordenado por notas) dentro de faixa de valores (máximo e mínimo);
3. Apresentar relação de alunos e respectivas notas (ordenado por nomes) cujos nomes contenham um certa string (caso a entrada seja vazia, obterá todos os nomes);
4. Apresentar uma relação de notas e o número de suas ocorrência para uma faixa de valores (máximo e mínimo);
5. Incluir um novo aluno/nota
6. Sair

Opção: '''

nome_aluno_list = []
nota_aluno_list = []
nome_aluno_list_ord_nota = []
nota_aluno_list_ord_nota = []
nome_aluno_list_ord_nome = []
nota_aluno_list_ord_nome = []

nome_aluno = input('Aluno: ')
nota_aluno = float(input('Nota: '))

while nota_aluno >= 0:
    nome_aluno_list.append(nome_aluno.upper())
    nota_aluno_list.append(nota_aluno)
    
    nome_aluno = input('Aluno: ')
    nota_aluno = float(input('Nota: '))

MAX_ALUNOS_REGISTRADOS = len(nome_aluno_list)

opcao = int(input(MSG_SELECAO_OPCAO))

while opcao != 6:
    if opcao == 1:    
        if nome_aluno_list_ord_nota == [] or nota_aluno_list_ord_nota == []:
            nome_aluno_list_ord_nota = nome_aluno_list
            nota_aluno_list_ord_nota = nota_aluno_list

            for i in range(MAX_ALUNOS_REGISTRADOS - 1):
                for j in range(i + 1, MAX_ALUNOS_REGISTRADOS):
                    if nota_aluno_list_ord_nota[j] < nota_aluno_list_ord_nota[i]:
                        tmp = nota_aluno_list_ord_nota[i]
                        nota_aluno_list_ord_nota[i] = nota_aluno_list_ord_nota[j]
                        nota_aluno_list_ord_nota[j] = tmp

                        tmp = nome_aluno_list_ord_nota[i]
                        nome_aluno_list_ord_nota[i] = nome_aluno_list_ord_nota[j]
                        nome_aluno_list_ord_nota[j] = tmp   

        print('Máximo:',
                '\n\tNome:', nome_aluno_list_ord_nota[MAX_ALUNOS_REGISTRADOS - 1], 
                '\tNota:', nota_aluno_list_ord_nota[MAX_ALUNOS_REGISTRADOS - 1])
    
        print('Mínimo:',
                '\n\tNome:', nome_aluno_list_ord_nota[0], 
                '\tNota:', nota_aluno_list_ord_nota[0])

        somatorio_notas = 0.0
        
        for nota in nota_aluno_list_ord_nota:
            somatorio_notas += nota
        
        print('Média:', somatorio_notas / MAX_ALUNOS_REGISTRADOS)

        if MAX_ALUNOS_REGISTRADOS > 1:
            print('Desvio Padrão:', statistics.stdev(nota_aluno_list_ord_nota))
        else:
            print("Desvio Padrão: ATENÇÃO! Para se calcular o desvio padrão é necessário ao menos 2 alunos registrados!")

        mediana = 0
        indice_med_1 = int(MAX_ALUNOS_REGISTRADOS / 2) - 1
        if MAX_ALUNOS_REGISTRADOS % 2 == 0:
            indice_med_2 = indice_med_1 + 1
            mediana = (nota_aluno_list_ord_nota[indice_med_1] + 
                       nota_aluno_list_ord_nota[indice_med_2]) / 2
        else:
            mediana = nota_aluno_list_ord_nota[indice_med_1 + 1]

        print('Mediana:', mediana)
        print('Primeira(s) Moda(s):')
        
        nota_anterior = nota_aluno_list_ord_nota[0]
        primeira_moda = 0
        notas_primeira_moda_list = []
        modas_primeira_moda_list = []

        for nota in nota_aluno_list_ord_nota:
            if nota_anterior == nota:
                primeira_moda += 1
            else:
                notas_primeira_moda_list.append(nota_anterior)
                modas_primeira_moda_list.append(primeira_moda)
                nota_anterior = nota
                primeira_moda = 1
        
        notas_primeira_moda_list.append(nota_anterior)
        modas_primeira_moda_list.append(primeira_moda)

        for i in range(len(modas_primeira_moda_list) - 1):
            for j in range(i + 1, len(modas_primeira_moda_list)):
                if modas_primeira_moda_list[j] > modas_primeira_moda_list[i]:
                    tmp = modas_primeira_moda_list[i]
                    modas_primeira_moda_list[i] = modas_primeira_moda_list[j]
                    modas_primeira_moda_list[j] = tmp

                    tmp = notas_primeira_moda_list[i]
                    notas_primeira_moda_list[i] = notas_primeira_moda_list[j]
                    notas_primeira_moda_list[j] = tmp

        moda_anterior = modas_primeira_moda_list[0]
        contador_modas = 1

        for i in range(1, len(modas_primeira_moda_list)):
            if moda_anterior == modas_primeira_moda_list[i]:
                contador_modas += 1

        for i in range(contador_modas):
            print('\tNota:', notas_primeira_moda_list[i],
                  '\tPrimeira Moda:', modas_primeira_moda_list[i])

    elif opcao == 2:
        if nome_aluno_list_ord_nota == [] or nota_aluno_list_ord_nota == []:
            nome_aluno_list_ord_nota = nome_aluno_list
            nota_aluno_list_ord_nota = nota_aluno_list

            for i in range(MAX_ALUNOS_REGISTRADOS - 1):
                for j in range(i + 1, MAX_ALUNOS_REGISTRADOS):
                    if nota_aluno_list_ord_nota[j] < nota_aluno_list_ord_nota[i]:
                        tmp = nota_aluno_list_ord_nota[i]
                        nota_aluno_list_ord_nota[i] = nota_aluno_list_ord_nota[j]
                        nota_aluno_list_ord_nota[j] = tmp

                        tmp = nome_aluno_list_ord_nota[i]
                        nome_aluno_list_ord_nota[i] = nome_aluno_list_ord_nota[j]
                        nome_aluno_list_ord_nota[j] = tmp  

        min = float(input("Mínimo: "))
        max = float(input("Máximo: "))

        nota_aluno_list_filtrada = []
        nome_aluno_list_filtrada = []

        for i in range(len(nota_aluno_list_ord_nota)):
            nota = nota_aluno_list_ord_nota[i]
            nome = nome_aluno_list_ord_nota[i]
            if nota >= min and nota <= max:
                nota_aluno_list_filtrada.append(nota)
                nome_aluno_list_filtrada.append(nome)

        if nota_aluno_list_filtrada != [] and nome_aluno_list_filtrada != []:
            for i in range(len(nota_aluno_list_ord_nota)):
                nome = nome_aluno_list_ord_nota[i]
                nota = nota_aluno_list_ord_nota[i]
                
                if nota >= min and nota <= max:
                    print('\tAluno:', nome, '\tNota:', nota)
        else:
            print('Nenhum resultado encontrado para a faixa especificada.')

    elif opcao == 3:
        if nome_aluno_list_ord_nome == [] or nota_aluno_list_ord_nome == []:
            nome_aluno_list_ord_nome = nome_aluno_list
            nota_aluno_list_ord_nome = nota_aluno_list

            for i in range(MAX_ALUNOS_REGISTRADOS - 1):
                for j in range(i + 1, MAX_ALUNOS_REGISTRADOS):
                    if nome_aluno_list_ord_nome[j] < nome_aluno_list_ord_nome[i]:
                        tmp = nome_aluno_list_ord_nome[i]
                        nome_aluno_list_ord_nome[i] = nome_aluno_list_ord_nome[j]
                        nome_aluno_list_ord_nome[j] = tmp

                        tmp = nota_aluno_list_ord_nome[i]
                        nota_aluno_list_ord_nome[i] = nota_aluno_list_ord_nome[j]
                        nota_aluno_list_ord_nome[j] = tmp
                    
        padrao = input("Padrão: ").upper()

        nome_aluno_list_filtrada = []
        nota_aluno_list_filtrada = []

        for i in range(len(nome_aluno_list_ord_nome)):
            nome = nome_aluno_list_ord_nome[i]
            nota = nota_aluno_list_ord_nome[i]
            if padrao in nome:
                nome_aluno_list_filtrada.append(nome)
                nota_aluno_list_filtrada.append(nota)
        
        if nome_aluno_list_filtrada != [] and nota_aluno_list_filtrada != []:
            for i in range(len(nome_aluno_list_filtrada)):
                nome = nome_aluno_list_filtrada[i]
                nota = nota_aluno_list_filtrada[i]
                print('\tAluno:', nome, '\tNota:', nota)
        else:
            print('Nenhum resultado encontrado para a faixa especificada.')

    elif opcao == 4:
        if nome_aluno_list_ord_nota == [] or nota_aluno_list_ord_nota == []:
            nome_aluno_list_ord_nota = nome_aluno_list
            nota_aluno_list_ord_nota = nota_aluno_list

            for i in range(MAX_ALUNOS_REGISTRADOS - 1):
                for j in range(i + 1, MAX_ALUNOS_REGISTRADOS):
                    if nota_aluno_list_ord_nota[j] < nota_aluno_list_ord_nota[i]:
                        tmp_nota = nota_aluno_list_ord_nota[i]
                        nota_aluno_list_ord_nota[i] = nota_aluno_list_ord_nota[j]
                        nota_aluno_list_ord_nota[j] = tmp_nota

                        tmp_nome = nome_aluno_list_ord_nota[i]
                        nome_aluno_list_ord_nota[i] = nome_aluno_list_ord_nota[j]
                        nome_aluno_list_ord_nota[j] = tmp_nome
        
        min = float(input("Mínimo: "))
        max = float(input("Máximo: "))

        nota_aluno_list_filtrada = []

        for nota in nota_aluno_list_ord_nota:
            if nota >= min and nota <= max:
                nota_aluno_list_filtrada.append(nota)

        if nota_aluno_list_filtrada != []:
            frequencia = 0
            nota_anterior = nota_aluno_list_filtrada[0]

            for nota in nota_aluno_list_filtrada:
                if nota == nota_anterior:
                    frequencia += 1
                else:
                    print('\tNota:', nota_anterior, '\tFrequência:', frequencia)
                    frequencia = 1
                    nota_anterior = nota
            
            print('\tNota:', nota_anterior, '\tFrequência:', frequencia)
        else:
            print('Nenhum resultado encontrado para a faixa especificada.')

    elif opcao == 5:
        nome = input('Nome: ')
        nota = float(input('Nota: '))
        nome_aluno_list.append(nome.upper())
        nota_aluno_list.append(nota)
        nome_aluno_list_ord_nota = []
        nota_aluno_list_ord_nota = []
        nome_aluno_list_ord_nome = []
        nota_aluno_list_ord_nome = []

    else:
        print("Opção inválida! Tente novamente, por gentileza...")

    
    opcao = int(input(MSG_SELECAO_OPCAO))