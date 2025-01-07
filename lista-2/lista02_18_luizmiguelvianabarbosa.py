# Título: Implementação de Crammer para uma matriz 3x3 - resolvendo sistemas lineares
# para equações com 3 incógnitas
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

def det(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    # Calculo do determinante realizado 
    # a partir de https://guiadoestudante.abril.com.br/curso-enem/determinantes-propriedades-das-matrizes-quadradas
    det = a * (e * i - f * h)
    det -= b * (d * i - f * g)
    det += c * (d * h - e * g)
    return det

def substitui_coluna(matriz, coluna, vetor):
    matriz_substituida = [linha[:] for linha in matriz]
    for i in range(3):
        matriz_substituida[i][coluna] = vetor[i]
    return matriz_substituida

def Cramer(matriz, vetor):
    # Calculo baseado em https://www.todamateria.com.br/regra-cramer/
    det_principal = det(matriz)
    
    if det_principal == 0:
        print("Erro: determinante principal é zero, ou seja, não há uma solução única!")
        return []

    x_det = det(substitui_coluna(matriz, 0, vetor))
    y_det = det(substitui_coluna(matriz, 1, vetor))
    z_det = det(substitui_coluna(matriz, 2, vetor))

    x = x_det / det_principal
    y = y_det / det_principal
    z = z_det / det_principal

    return [x, y, z]

# def ler_matriz():
#     matriz = []
#     linhas = 3
#     colunas = 3
    
#     print("Valores, linha por linha:")
#     for i in range(linhas):
#         linha = []
#         for j in range(colunas):
#             valor = float(input(f"Valor da Posição [{i}][{j}]: "))
#             linha.append(valor)
#         matriz.append(linha)
    
#     return matriz

# matriz_de_coeficientes = ler_matriz()

# respostas = [float(input(f'Resultado da {i+1}a equanção = ')) for i in range(3)]

# solucao = Cramer(matriz_de_coeficientes, respostas)

# if solucao:
#     print("Solução do sistema:")
#     print(f"x = {solucao[0]:.2f}, y = {solucao[1]:.2f}, z = {solucao[2]:.2f}")