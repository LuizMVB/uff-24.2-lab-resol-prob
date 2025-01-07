# Título: Lê um vetor de 40 posições e conta quantos elementos pares se encontram no vetor
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

n = 40
vetor = [int(input('Número: ')) for _ in range(n)]
vetor_pares = [item for item in vetor if item % 2 == 0]
print('Quantidade de Elementos Pares:', len(vetor_pares))