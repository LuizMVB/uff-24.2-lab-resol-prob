# Título: Calcular o MDC entre dois números e a quantidade de divisores comuns
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

# Lendo os valores inteiros A e B
a = int(input('A: '))
b = int(input('B: '))

# Calculando o MDC
a_original = a 
b_original = b

while b != 0:
    resto = a % b
    a = b
    b = resto

# Agora, o MDC está em a 
mdc = a

# Encontrando os divisores em comum seguindo a mesma lógica de questões anteriores
quantidade_divisores_comuns = 0
for i in range(1, mdc + 1):
    if a_original % i == 0 and b_original % i == 0:
        quantidade_divisores_comuns += 1

print("MDC:", mdc)
print("Quantidade de divisores comuns:", quantidade_divisores_comuns)