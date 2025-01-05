# Programa de IMC
# Nome: Wesley Ferreira e Luiz Miguel Viana

peso = float(input("Digite o peso em quilos: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura * altura)

idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

if idade > 20:
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Pré-obesidade")
    elif imc < 35:
        print("Obesidade Grau 1")
    elif imc < 40:
        print("Obesidade Grau 2")
    else:
        print("Obesidade Grau 3")
else:
    if sexo == 'M':
        if idade == 10:
            if imc < 14.42:
                print("Baixo Peso")
            elif imc < 19.60:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 11:
            if imc < 14.83:
                print("Baixo Peso")
            elif imc < 20.35:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 12:
            if imc < 15.24:
                print("Baixo Peso")
            elif imc < 21.12:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 13:
            if imc < 15.73:
                print("Baixo Peso")
            elif imc < 21.93:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 14:
            if imc < 16.18:
                print("Baixo Peso")
            elif imc < 22.77:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 15:
            if imc < 16.59:
                print("Baixo Peso")
            elif imc < 23.63:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 16:
            if imc < 17.01:
                print("Baixo Peso")
            elif imc < 24.45:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 17:
            if imc < 17.31:
                print("Baixo Peso")
            elif imc < 25.28:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 18:
            if imc < 17.54:
                print("Baixo Peso")
            elif imc < 25.95:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 19:
            if imc < 17.80:
                print("Baixo Peso")
            elif imc < 26.36:
                print("Peso Adequado")
            else:
                print("Sobrepeso")

    elif sexo == 'F':
        if idade == 10:
            if imc < 14.23:
                print("Baixo Peso")
            elif imc < 20.19:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 11:
            if imc < 14.60:
                print("Baixo Peso")
            elif imc < 21.18:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 12:
            if imc < 14.98:
                print("Baixo Peso")
            elif imc < 22.17:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 13:
            if imc < 15.36:
                print("Baixo Peso")
            elif imc < 23.08:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 14:
            if imc < 15.67:
                print("Baixo Peso")
            elif imc < 23.88:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 15:
            if imc < 16.01:
                print("Baixo Peso")
            elif imc < 24.29:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 16:
            if imc < 16.37:
                print("Baixo Peso")
            elif imc < 24.74:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 17:
            if imc < 16.59:
                print("Baixo Peso")
            elif imc < 25.23:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 18:
            if imc < 16.71:
                print("Baixo Peso")
            elif imc < 25.56:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 19:
            if imc < 16.87:
                print("Baixo Peso")
            elif imc < 25.85:
                print("Peso Adequado")
            else:
                print("Sobrepeso")

print("Seu IMC é:", imc)
