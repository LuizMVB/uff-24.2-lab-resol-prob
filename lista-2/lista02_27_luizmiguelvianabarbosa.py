# Título: Gera uma representação da decomposição do número em fatores primos
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

def fat_primo(num):
    fatores = []
    divisor = 2

    while num > 1:
        expoente = 0

        while num % divisor == 0:
            num //= divisor
            expoente += 1

        if expoente > 0:
            fatores.append(f"{divisor}^{expoente}")
        
        divisor += 1
    
    return fatores

# print(fat_primo(564))
# print(fat_primo(56475768481089153821883027))
# print(fat_primo(56475))
# print(fat_primo(5647576848))