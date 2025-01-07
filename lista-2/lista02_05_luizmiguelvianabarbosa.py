# Título: Lê um vetor de 16 posições e troca as 8 primeiras posições pelas 8 últimas
# posições. Imprime o vetor original e o vetor trocado
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

n = 16
vetor = [input('Número: ') for _ in range(n)]
print('Original:', vetor)
tmp = vetor[:8]
vetor[:8] = vetor[8:]
vetor[8:] = tmp
print('Trocado:', vetor)