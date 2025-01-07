# Título: Cria uma matriz transposta a partir de uma matriz bidimensional (sem altera-la)
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

def mat_transposta(matriz):
    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

# def ler_matriz():
#     matriz = []
#     linhas = int(input("Número de linhas: "))
#     colunas = int(input("Número de colunas: "))
    
#     print("Valores, linha por linha:")
#     for i in range(linhas):
#         linha = []
#         for j in range(colunas):
#             valor = float(input(f"Valor da Posição [{i}][{j}]: "))
#             linha.append(valor)
#         matriz.append(linha)
    
#     return matriz

# matriz_original = ler_matriz()
# matriz_transposta = mat_transposta(matriz_original)

# print("\nMatriz Original:")
# for linha in matriz_original:
#     print(linha)

# print("\nMatriz Transposta:")
# for linha in matriz_transposta:
#     print(linha)