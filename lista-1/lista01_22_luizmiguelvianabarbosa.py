# Título: Calculando a menor quantidade de notas necessárias para um saque em caixa eletrônico
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

# Solicita o valor do saque ao usuário
valor = int(input('Valor do saque: '))

# Inicializa as quantidades de cada tipo de nota
notas_50 = int()
notas_20 = int()
notas_10 = int()
notas_5 = int()
notas_1 = int()

# Calcula a quantidade de notas de 50 necessárias
notas_50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20 necessárias
notas_20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10 necessárias
notas_10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5 necessárias
notas_5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 1 necessárias
notas_1 = valor // 1
valor = valor % 1

# Exibe a quantidade de cada tipo de nota
print('Notas de 50:', notas_50)
print('Notas de 20:', notas_20)
print('Notas de 10:', notas_10)
print('Notas de 5:', notas_5)
print('Notas de 1:', notas_1)