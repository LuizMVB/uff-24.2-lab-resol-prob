# Título: Pesquisa de satisfação de novo produto
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

resposta = input('Você está satisfeito com o produto?')

porcentagem_sim = int()
porcentagem_nao = int()
total_respostas = int()
total_sim = int()
total_nao = int()

# Condição de parada é a seleção de "F", enquanto isto não ocorrer
# deve realizar a iteração
while resposta != 'F':
    
    # Adiciona uma unidade para cada tipo de resposta
    if resposta == 'S':
        total_sim += 1
    elif resposta == 'N':
        total_nao += 1
    
    # Adiciona uma unidade para o total de respostas
    total_respostas += 1
    resposta = input('Você está satisfeito com o produto?')

# Certifica-se de que o total de respotas é maior que zero para não haver
# erro de divisão por zero
if total_respostas > 0:
    # Calcula os percentuais de sims e nãos
    porcentagem_sim = (total_sim / total_respostas) * 100
    porcentagem_nao = (total_nao / total_respostas) * 100
    
print('Satisfeitos (%):', porcentagem_sim, '%')
print('Insatisfeitos (%):', porcentagem_nao, '%')