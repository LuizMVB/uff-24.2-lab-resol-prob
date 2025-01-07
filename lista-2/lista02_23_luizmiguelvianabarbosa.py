# Título: Calcula a área do triangulo a partir de uma matriz 3x2
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

import math

def distancia(p1, p2):
    # obtida a partir de https://mundoeducacao.uol.com.br/matematica/formula-heron.htm
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def area_triangulo(matriz):
    p1, p2, p3 = matriz[0], matriz[1], matriz[2]
    
    a = distancia(p1, p2)
    b = distancia(p2, p3)
    c = distancia(p3, p1)
    s = (a+b+c)/2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    return area

# triangulo = [[0, 0], [6, 0], [3, 6]]
# area = area_triangulo(triangulo)
# print(f"Área: {area:.2f}")