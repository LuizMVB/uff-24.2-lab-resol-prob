# Título: Apuração de votos de eleição municipal
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

total_votos_joao = int()
total_votos_jose = int()
total_votos_maria = int()
total_votos_pedro = int()
total_votos_brancos = int()
total_votos_nulos = int()

# Iterando para cada votante
for i in range(20000):
    voto = int(input('Digite seu voto: '))
    
    # Verificando as condições para cada voto
    if voto == 1:
        total_votos_joao += 1
    elif voto == 2:
        total_votos_jose += 1
    elif voto == 3:
        total_votos_maria += 1
    elif voto == 4:
        total_votos_pedro += 1
    elif voto == 0:
        total_votos_brancos += 1
    else:
        total_votos_nulos += 1

print('Total de votos para João da Silva: ', total_votos_joao)
print('Total de votos para José Ramalho: ', total_votos_jose)
print('Total de votos para Maria Mattos: ', total_votos_maria)
print('Total de votos para Pedro Américo: ', total_votos_pedro)
print('Total de votos em branco: ', total_votos_brancos)
print('Total de votos nulos: ', total_votos_nulos)