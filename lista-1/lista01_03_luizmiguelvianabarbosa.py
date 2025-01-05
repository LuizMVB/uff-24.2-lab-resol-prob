# Título: Lendo N números inteiros e mostrando a quantidade de números 
# pares, ímpares e a média aritmética dos pares
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

numero = int(input('número inteiro: '))

quantidade_pares = int()
quantidade_impares = int()
somatorio_pares = int()
media_pares = float()

while numero != 0:
    
    if numero % 2 == 0:
        # Caso o resto da divisão por 2 seja zero, trata-se de um número par
        # Adiciona o número ao somatório e adiciona uma unidade à quantidade
        # de números pares
        somatorio_pares += numero
        quantidade_pares += 1
    else: 
        # Caso o resto da divisão por 2 seja diferente de zero, trata-se 
        # de um número par
        # Adiciona uma unidade à quantidade de números ímpares
        quantidade_impares += 1
        
    numero = int(input('número inteiro: '))

# Tratamento para o caso de exceção em que não há números pares
if quantidade_pares > 0:
    # Define a média aritmética dos números pares
    media_pares = somatorio_pares / quantidade_pares

print('quantidade de números pares:', quantidade_pares)
print('quantidade de números ímpares:', quantidade_impares)
print('média dos números pares:', media_pares)





