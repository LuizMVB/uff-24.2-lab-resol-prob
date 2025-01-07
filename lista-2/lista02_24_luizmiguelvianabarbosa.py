# Título: Calcula a area do poligono convexo com vertices na matriz (N x 2 - N indeterminado)
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

def area_poligono(matriz):
    if len(matriz) < 3:
        raise ValueError("Um polígono deve ter pelo menos 3 vértices!")
    
    ponto_base = matriz[0]
    area_total = 0
    
    for i in range(1, len(matriz) - 1):
        triangulo = [ponto_base, matriz[i], matriz[i + 1]]
        area_total += area_triangulo(triangulo)
    
    return area_total

# poligono_1 = [[0, 0], [4, 0], [4, 3], [0, 3]] 
# poligono_2 = [[0, 0], [5, 0], [6, 4], [3, 7], [0, 4]]
# poligono_3 = [[0, 0], [3, 0], [0, 4]] 
# poligono_4 = [[0, 0], [2, 0], [3, 1.5], [1, 3], [-1, 1.5]]
# poligono_5 = [[0, 0], [4, 0], [4, 4], [0, 4]]

# print(f"Área do polígono 1: {area_poligono(poligono_1):.2f}") 
# print(f"Área do polígono 2: {area_poligono(poligono_2):.2f}")  
# print(f"Área do polígono 3: {area_poligono(poligono_3):.2f}")
# print(f"Área do polígono 4: {area_poligono(poligono_4):.2f}")
# print(f"Área do polígono 5: {area_poligono(poligono_5):.2f}") 