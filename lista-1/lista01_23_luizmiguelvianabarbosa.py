# Título: Calculando os N primeiros números primos que fazem parte da 
# série de Fibonacci
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Utilizando o código da questão de definição de núemros primos

n = int(input('Quantidade de números primos na série de Fibonacci: '))

contador_primos = 0
numero_atual = 2

# Enquanto o contador for menor que o próprio N, realiza a iteração
while contador_primos < n:
    divisores = 0
    
    # Utilizando lógica para definir se número é primo
    for i in range(1, numero_atual + 1):
        if numero_atual % i == 0:
            divisores += 1
    
    if divisores == 2:
        # Verifica se o número faz parte da série de Fibonacci
        a = 0
        b = 1
        pertence = False
        
        while b <= numero_atual:
            if b == numero_atual:
                pertence = True
            a_temp = a
            a = b
            b = a_temp + b
        
        if pertence:
            print(numero_atual)
            contador_primos += 1
    
    numero_atual += 1