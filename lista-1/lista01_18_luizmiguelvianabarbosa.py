# Título: Lendo um número N e imprimindo os N primeiros números primos
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Utilizando parte do código da questão anterior para definir se um número é 
# primo ou não

n = int(input('Quantidade de números primos: '))

contador_primos = 0
numero_atual = 2

# Enquanto o contados for menor que o próprio N, realiza a iteração
while contador_primos < n:
    divisores = 0
    
    # Utilizando lógica para definir se número é primo da questão anterior
    for i in range(1, numero_atual + 1):
        if numero_atual % i == 0:
            divisores += 1
    
    if divisores == 2:
        print(numero_atual)
        contador_primos += 1
    
    numero_atual += 1