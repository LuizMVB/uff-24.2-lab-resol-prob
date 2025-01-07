# Título: Cria uma lista de tamanho N e diz quais números nessa lista são primos
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

import math

def eh_primo(numero: int):
    if numero < 2:
        return False
    # Não há necessidade de realziar o teste para 
    # números acima de sua raíz quadrada
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

[print(numero) for numero in list(range(int(input('n: ')))) if eh_primo(numero)]