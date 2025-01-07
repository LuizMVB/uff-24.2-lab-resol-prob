# Título: CGera uma matriz 3 x 3 aleatória e realiza o cálculo do determinante
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

import random

def gera_matriz_aleatoria():
    return [[random.randint(0, 9) for _ in range(3)] for _ in range(3)]

def calcula_determinante(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    # Calculo do determinante realizado 
    # a partir de https://guiadoestudante.abril.com.br/curso-enem/determinantes-propriedades-das-matrizes-quadradas
    det = a * (e * i - f * h)
    det -= b * (d * i - f * g)
    det += c * (d * h - e * g)
    return det

matriz = gera_matriz_aleatoria()

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

determinante = calcula_determinante(matriz)
print("\nDeterminante da matriz:", determinante)