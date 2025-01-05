# Título: Realiza a fatoração de um número intiero em fatores primos
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

# Lendo o valor de A
a = int(input("A: "))

numero_atual = a

# Inicializando o divisor
divisor = 2

print("Fatoração de", a)

# Executando a fatoração
while numero_atual > 1:
    expoente = 0  # Contador para o número de vezes que o divisor divide o número atual
    
    # Contabiliza o expoente do divisor atual
    while numero_atual % divisor == 0:
        numero_atual //= divisor
        expoente += 1
    
    # Se o divisor é um fator, exibe o resultado
    if expoente > 0:
        print(str(divisor) + ' ^ ' + str(expoente))
    
    # Incrementa o divisor para o próximo número primo
    divisor += 1