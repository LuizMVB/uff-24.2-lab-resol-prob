# Título: Convertendo para base decimal um número menor que 10
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

# Lendo a base numérica
base = int(input('Base numérica: ')) 

# Lendo o número especificado como inteiro
num = int(input('Número especificado: '))

vr_decimal = 0

numero_valido = True

# Utilizada para calcular a posição dos digítos
potencia = 1
while num > 0:
    # Último dígito do número
    digito = num % 10

    # Caso o dígito seja maior ou igual a base, o número é inválido
    if digito >= base:
        numero_valido = False

    # Somando o valor decimal relacionado ao dígito
    vr_decimal = vr_decimal + digito * potencia

    # Atualiza a potência da base
    potencia *= base

    # Remove o último dígito do número
    num = num // 10

# Exibindo o resultado apenas se o número for válido
if numero_valido:
    print(vr_decimal)
else:
    print("Dígito inválido para a base informada.") 