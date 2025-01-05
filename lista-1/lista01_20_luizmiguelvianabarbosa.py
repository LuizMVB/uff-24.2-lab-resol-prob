# Título: Definindo os quantro primeiros números perfeitos (soma dos seus divisores é 
# igual a ele mesmo)
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Utilizando código da questão anterior para definir se um número é perfeito

contador = 0
n = 1

# Enquanto contador for diferente de 4, continua na iteração
while contador != 4:
    soma_divisores = 0
    
    # Iterando sobre todos os números anteriores a n para identificar seus divisores
    for i in range(1, n):
        # Caso o item seja um divisor, é adicionado ao somatório de divisores
        if n % i == 0:
            soma_divisores += i
    
    # Se a soma dos divisores é igual ao próprio número, ele é perfeito e exibido
    if soma_divisores == n:
        print('Número perfeito:', n)
        contador += 1
    
    # Vai para o próximo número
    n += 1
    
    