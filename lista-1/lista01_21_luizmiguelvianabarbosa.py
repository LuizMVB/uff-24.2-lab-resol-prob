# Título: Calculando somatório com índice final N, índice inicial 1 e 
# termo do somatório igual ao inverso do índice
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

n = int(input('N: '))

somatorio = float()

# Realiza a iteração para atender ao propósito do somátorio
for i in range(1, n + 1):
    somatorio += 1 / i

print(somatorio)