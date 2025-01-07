# Título: Recebe duas matrizes e calcula sua múltiplicação
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

def multiplica_matriz(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("Erro: Não é possível realizar o produto das matrizes. Dimensões incompatíveis.")
        return []
    
    resultado = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                resultado[i][j] += mat1[i][k] * mat2[k][j]

    return resultado

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

# matriz1, matriz2 = ler_matriz(), ler_matriz()

# produto = multiplica_matriz(matriz1, matriz2)

# if produto:
#     print("Produto das Matrizes:")
#     for linha in produto:
#         print(linha)