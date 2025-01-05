# Título: Calculando o valor atual de um financiamento
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

r = float(input('Taxa de juros: '))
pmt = float(input('Valor das parcelas: '))
n = int(input('Número de parcelas: '))

vr_presente = float()

# Itera para calcular o somatório segundo a formula do valor atual
for i in range(1, n+1):
    # Define o valor atual através da fórmula que se aplica a cada item
    vr_presente += pmt / ((1 + r) ** i)

print('Valor presente do financiamento: ', vr_presente)