# Título: Calculando a soma dos N primeiros números inteiros ímpares e positivos
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Reutilizando o código de cálculo da PA

n = int(input('Quantidade de números ímpares: '))

# Definindo o primeiro termo como -1
primeiro_termo = -1

# Definindo a razão como 2
razao = 2

soma = int()
termo_atual = primeiro_termo

# Definindo a iteração de zero até n, exclusive
# Com o primeiro temro como -1 e a razão 2 teremos o somatório dos n 
# primeiros termos impares positivos: 1, 3, 5, 7, 9, 11, ...
for i in range(n):
    termo_atual = termo_atual + razao
    soma += termo_atual

print('Soma:', soma)