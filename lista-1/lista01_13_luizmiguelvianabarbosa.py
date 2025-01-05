# Título: Calculando e mostrando a idade média e o percentual de pessoas
# com idade entre 21 e 65 anos inclusive
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

idade = int(input('idade: '))
somatorio = int()
quantidade_total = int()
quantidade_entre_21_e_65 = int()
idade_media = float()
percentual_entre_21_e_65 = float()

# Definindo condição de parada como -1
while idade != -1:
    
    # Adicionando a idade ao somatório de idade do grupo
    somatorio += idade
    # Adicionando uma unidade para cada pessoa do grupo
    quantidade_total += 1 
    
    # Caso a idade seja entre 21 e 65 inclusive, adiciona uma unidade para 
    # a quantidade de pessoas nessas condições
    if idade >= 21 and idade <= 65:
        quantidade_entre_21_e_65 += 1
    
    idade = int(input('idade: '))

# Atendendo cenário de exceção em que a quantidade total é zero para 
# evitar erros de divisão por zero
if quantidade_total > 0:
    # Definindo a idade média e o percentual entre 21 e 65 inclusive
    idade_media = somatorio / quantidade_total
    percentual_entre_21_e_65 = quantidade_entre_21_e_65 / quantidade_total

print('Idade média:', idade_media)
print('Percentual de pessoas entre 21 e 65 anos, inclusive, é de ' + str(percentual_entre_21_e_65 * 100) + '%')