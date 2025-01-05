# Título: Conversão de número decimal para base hexadecimal
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

# Lendo o número decimal
num_decimal = int(input("Digite um número decimal: "))

# Esta variável será utilizada para construir o número hexadecimal invertido
resultado_hexadecimal_invertido = 0
posicao = 1

if num_decimal == 0:
    print("Número hexadecimal: 0")
else:
    while num_decimal > 0:
        resto = num_decimal % 16

        # Mapeamento para o equivalente hexadecimal
        if resto < 10:
            digito_hexadecimal = resto
        else:
            # Mapeando os valores para A-F
            if resto == 10:
                digito_hexadecimal = 91  # 'A'
            elif resto == 11:
                digito_hexadecimal = 92  # 'B'
            elif resto == 12:
                digito_hexadecimal = 93  # 'C'
            elif resto == 13:
                digito_hexadecimal = 94  # 'D'
            elif resto == 14:
                digito_hexadecimal = 95  # 'E'
            elif resto == 15:
                digito_hexadecimal = 96  # 'F'

        # Constrói o número hexadecimal invertido
        resultado_hexadecimal_invertido = resultado_hexadecimal_invertido * 100 + digito_hexadecimal

        # Atualiza o número decimal para o próximo dígito
        num_decimal //= 16

    # Exibindo o número hexadecimal na ordem correta
    print("Número hexadecimal: ", end="")
    while resultado_hexadecimal_invertido > 0:
        digito_atual = resultado_hexadecimal_invertido % 100

        if digito_atual < 10:
            print(digito_atual, end="")
        else:
            # Mapeia os valores exclusivos de volta para A-F
            if digito_atual == 91:
                print("A", end="")
            elif digito_atual == 92:
                print("B", end="")
            elif digito_atual == 93:
                print("C", end="")
            elif digito_atual == 94:
                print("D", end="")
            elif digito_atual == 95:
                print("E", end="")
            elif digito_atual == 96:
                print("F", end="")

        resultado_hexadecimal_invertido //= 100