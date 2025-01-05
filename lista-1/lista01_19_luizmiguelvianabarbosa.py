# Título: Definindo se um número é perfeito (soma dos seus divisores é 
# igual a ele mesmo)
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

n = int(input('Número: '))
soma_divisores = 0

# Iterando sobre os números de 1 até o n, exclusive
for i in range(1, n):
    
    # Se o item for divisor do número n, realiza sua soma ao somatório de divisores
    if n % i == 0:
        soma_divisores += i
        
print('Soma dos divisores: ', soma_divisores)

# Se o a soma de divisores é igual ao número, é um número perfeito
if soma_divisores == n:
    print('Perfeito')
# Caso contrário, não é um número perfeito
else:
    print('Imperfeito')
    
    
    