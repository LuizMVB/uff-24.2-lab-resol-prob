# Título: Calculando a quantidade de dias entre duas datas
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

# Lendo as datas
D1 = int(input("D1: "))
M1 = int(input("M1: "))
A1 = int(input("A1: "))

D2 = int(input("D2: "))
M2 = int(input("M2: "))
A2 = int(input("A2: "))

dias_no_mes = 0
total_dias = 0

# Itera incrementando o valor de dias segundo a condição de 
# 1. O primeiro ano é menor que o segundo OU
# 2. Os anos são iguais, porém o primeiro mês é menor que o segundo
# 3. Os anos e os meses são iguais, porém o primeiro mês é menor que o segundo
while A1 < A2 or (A1 == A2 and M1 < M2) or (A1 == A2 and M1 == M2 and D1 < D2):
    # Definindo as condições para atender a quantidade de dias que cada mês contém
    if M1 == 1 or M1 == 3 or M1 == 5 or M1 == 7 or M1 == 8 or M1 == 10 or M1 == 12:
        dias_no_mes = 31
    elif M1 == 4 or M1 == 6 or M1 == 9 or M1 == 11:
        dias_no_mes = 30
    elif M1 == 2:
        # Verificando ano bissexto, adicionando mais um dia ao mês de fevereiro
        # para o caso do ano ser bissexto
        if (A1 % 4 == 0 and A1 % 100 != 0) or (A1 % 400 == 0):
            dias_no_mes = 29 
        else:
            dias_no_mes = 28 

    # Soma uma unidade ao primeiro dia 
    D1 += 1
    total_dias += 1

    # Ajusta mês e ano se necessário
    if D1 > dias_no_mes:
        D1 = 1
        M1 += 1

    if M1 > 12:
        M1 = 1
        A1 += 1

# Exibe o total de dias entre as datas
print("Quantidade de dias entre as datas:", total_dias)