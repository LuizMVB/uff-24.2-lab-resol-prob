# Título: Lê um vetor de números inteiros de 30 posições. Depois, lê um número inteiro X e
# imprime quantas vezes o número X aparece no vetor.
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

n = 30
vetor = [int(input('Número: ')) for _ in range(n)]
x = int(input('x: '))
print('Quantidade de Aparições de x no Vetor:', len([i for i in vetor if i == x]))