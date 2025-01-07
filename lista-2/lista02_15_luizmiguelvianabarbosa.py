# Título: Conversão de número de base menor ou ingual a 10 para base decimal
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

numero_na_base = input("Número: ")
base = int(input("Base: "))

if base >= 10 or base < 2:
    print("Erro: A base deve ser maior ou igual a 2 e menor que 10!")
else:
    numero_decimal = 0
    for i, digito in enumerate(reversed(numero_na_base)):
        valor = int(digito)
        if valor >= base:
            print(f"Erro: Dígito inválido '{digito}' para a base {base}!")
            break
        numero_decimal += valor * (base ** i)
    else:
        print(f"O número {numero_na_base} na base {base} é equivalente a {numero_decimal} na base decimal.")