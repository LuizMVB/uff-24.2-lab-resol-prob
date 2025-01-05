# Título: Calculando a soma dos 20 primeiros números pares
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Reutilizando o código utilizado para calcular a PA

# Definindo o primeiro termo como zero
primeiro_termo = 0

# Definindo a razão como 2
razao = 2

soma = int()
termo_atual = primeiro_termo

# Iterando 20 vezes com o primeiro termo como 0 e a razão 2, teremos o somatório
# dos 20 primeiros números
for i in range(20):
    termo_atual = termo_atual + razao
    soma += termo_atual

print('Soma:', soma)