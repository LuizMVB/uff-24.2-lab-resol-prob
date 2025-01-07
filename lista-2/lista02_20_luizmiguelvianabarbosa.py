# Título: Cria um vetor de 100 posições com 100 números aleatórios (de 0 a 100) e ordena
# sem usar o método sort
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

import random

n = 100
vetor_gago = [random.randint(0, n) for _ in range(n)]

for i in range(len(vetor_gago) - 1):
    for j in range(i + 1, len(vetor_gago)):
        if vetor_gago[j] < vetor_gago[i]:
            tmp = vetor_gago[i]
            vetor_gago[i] = vetor_gago[j]
            vetor_gago[j] = tmp

print(vetor_gago)