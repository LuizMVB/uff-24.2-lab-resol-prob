# Título: Converte um número inteiro em algarismo romano
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

def inteiro_para_romano(numero: int):
    valores_romanos = {
        1000: "M",
        900: "CM",
        500: "D", 
        400: "CD",
        100: "C", 
        90: "XC", 
        50: "L", 
        40: "XL", 
        10: "X",
        9: "IX",
        5: "V", 
        4: "IV", 
        1: "I", 
    }

    resultado = str()

    while numero > 0:

        # Análogo a solução do execício das moedas (a idéia de subtrair)
        for valor in valores_romanos.keys():
            while numero >= valor:
                resultado += valores_romanos[valor]
                numero -= valor

    return resultado

n = int(input('N: '))
print(inteiro_para_romano(n))