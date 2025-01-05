# Título: Pesquisa salarial da prefeitura por idade e sexo
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

idade = int(input('idade: '))
sexo = input('sexo: ')
salario = float(input('salário: '))

somatorio_salario_homens = float()
quantidade_homens = int()
somatorio_salario_mulheres = float()
quantidade_mulheres = int()
maior_salario_under_30 = float()
salario_anterior = float()
media_salarial_homens = float()
media_salarial_mulheres = float()

while idade > 0:
    # Caso o sexo seja másculino, acrescenta o valor do salário ao 
    # somatório referente ao mesmo
    if sexo == 'M':
        somatorio_salario_homens += salario
        quantidade_homens += 1
    
    # Caso o sexo seja feminino, acrescenta o valor do salário ao 
    # somatório referente ao mesmo
    if sexo == 'F':
        somatorio_salario_mulheres += salario
        quantidade_mulheres += 1
    
    # Definindo o salário maior para pessoas que possuem idade inferior a 30 anos
    if salario > salario_anterior and idade < 30:
        maior_salario_under_30 = salario
        salario_anterior = salario    
    
    idade = int(input('idade: '))
    
    # Restringindo as demais entradas a limitação de saída da iteração
    if idade > 0:
        sexo = input('sexo: ')
        salario = float(input('salário: '))

# Tratando caso de exceção em que nenhum homem respondeu à pesquisa 
if quantidade_homens > 0:    
    media_salarial_homens = somatorio_salario_homens / quantidade_homens

# Tratando caso de exceção em que nenhuma mulher respondeu à pesquisa 
if quantidade_mulheres > 0:
    media_salarial_mulheres = somatorio_salario_mulheres / quantidade_mulheres

print('Média salarial dos homens: ', media_salarial_homens)
print('Média salarial das mulheres: ', media_salarial_mulheres)
print('Maior salário entre as pessoas abaixo de 30 anos: ', maior_salario_under_30)
