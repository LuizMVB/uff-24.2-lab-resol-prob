# Título: Converte um algarismo romano em número inteiro
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

def romano_para_arabico(romano: str) -> int:
    romano = romano.upper()

    valores_romanos = {
        "M": 1000,
        "CM": 900,
        "D": 500, 
        "CD": 400,
        "C": 100, 
        "XC": 90, 
        "L": 50, 
        "XL": 40, 
        "X": 10,
        "IX": 9,
        "V": 5, 
        "IV": 4, 
        "I": 1, 
    }

    arabico = 0
    contador = 0

    while contador < len(romano):
        if contador + 1 < len(romano) and romano[contador:contador+2] in valores_romanos:
            arabico += valores_romanos[romano[contador:contador+2]]
            contador += 2
        else:
            arabico += valores_romanos[romano[contador]]
            contador += 1
    
    return arabico

n = input('N: ')
print(romano_para_arabico(n))