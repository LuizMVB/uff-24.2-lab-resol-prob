# Título: Pesquisa da firma sobre a satisfação com um determinado produto
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

total_sim = int()
total_nao = int()
total_homens_nao = int()
total_homens = int()

# Iterando entre as 20 pessoas que participaram da pesquisa
for i in range(20):
    sexo = input('Sexo: ')
    resposta = input('Gosta do produto?')
    
    # Caso resposta seja sim, adiciona uma unidade a quantidade de pessoas que
    # responderam sim
    if resposta == 'S':
        total_sim += 1
        
    # Caso a resposta não seja sim e seja não, adiciona uma unidade a quantidade
    # de pessoas que responderam não
    elif resposta == 'N':
        total_nao += 1
        
        # Caso a resposta seja não e a pessoa seja homem, adiciona uma unidade
        # a quantidade de pessoas homens que responderam não
        if sexo == 'M':
            total_homens_nao += 1
    
    # Caso a resposta seja dada por um homem, adiciona uma unidade a quantidade
    # de homens que responderam
    if sexo == 'M':
        total_homens += 1

# Trata o caso de divisão por zero para o cálculo de percentual de homens 
# que responderam não
if total_homens > 0:
    porcentagem_homens_nao = (total_homens_nao / total_homens) * 100
else:
    porcentagem_homens_nao = 0

print('Número de pessoas que responderam sim', total_sim)
print('Número de pessoas que responderam não:', total_nao)
print('Porcentagem de pessoas do sexo masculino que responderam não:', porcentagem_homens_nao, '%')