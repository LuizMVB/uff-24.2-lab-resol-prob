# Título: Verificando se um número é primo
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

n = int(input('Número: '))
divisores = 0

# Iterando entre 1, inclusive, e o próprio número, inclusive
for i in range(1, n + 1):
    # Adiciona uma unidade a quantidade de divisores para cada divisor desse número
    if n % i == 0:
        divisores += 1
        
# Se o número possui 2 divisores (ele mesmo e 1) ele é primo
if divisores == 2:
    print('O número', n, 'é primo.')
# Caso contrário, não é primo
else:
    print('O número', n, 'não é primo.')
    
    
    