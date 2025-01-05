# Título: Calculando a área de um triangulo pelos seus lados
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

a = float(input('Digite o comprimento do lado a: '))
b = float(input('Digite o comprimento do lado b: '))
c = float(input('Digite o comprimento do lado c: '))

# Atendendo às condições estabelecidas pelo problema. Enquanto um dos valores for
# inválido, deverá repetir a entrada de dados
# Além disso adicioneio condicionais para validar se o tamanho de cada lado 
# é válido com relação aos demais
while a <= 0 or b <= 0 or c <= 0 or (a+b <= c) or (a+c <= b) or (b+c <= a):
    print('Medidas inválidas. Insira novamente.')
    a = float(input('Digite o comprimento do lado a: '))
    b = float(input('Digite o comprimento do lado b: '))
    c = float(input('Digite o comprimento do lado c: '))

# Utilizando a fórmula de cálcular a área pelos lados
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print('A área do triângulo é:', area)