# Título: Recebe uma matriz e retorna a quantidade de elementos maiores que dez
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

def mat_maior_10(matriz):
    return sum(sum([1 for j in i if j > 10]) for i in matriz)

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
# len_elemen_maior_10 = mat_maior_10(matriz_original)

# print("\nMatriz Original:")
# for linha in matriz_original:
#     print(linha)

# print("\nQuantidade de elementos maior que 10:", len_elemen_maior_10)