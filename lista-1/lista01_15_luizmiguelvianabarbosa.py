# Título: Encontrando a primeira e a segunda maior altura entre as modelos e 
# quantas modelos possuem essas alturas
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

nome = str()
primeira_maior_altura = float()
segunda_maior_altura = float()
quantidade_1a_maior_altura = int()
quantidade_2a_maior_altura = int()

# Definindo que enquanto o nome for diferente de MARIA, a iteração deve continuar 
while nome != 'MARIA':
    nome = input('Nome: ')
    altura = float(input('Altura: '))
    
    # Caso a altura seja maior que a primeira maior altura, realiza a 
    # 1. Atualização da segunda maior altura e da primeira maior altura
    if altura > primeira_maior_altura:
        segunda_maior_altura = primeira_maior_altura
        quantidade_2a_maior_altura = quantidade_1a_maior_altura
        primeira_maior_altura = altura
        quantidade_1a_maior_altura = 1
    # Caso igual, adiciona mais uma unidade a quantidade de 1a maior altura
    elif altura == primeira_maior_altura:
        quantidade_1a_maior_altura += 1
    # Caso altura maior que segunda atualiza segunda maior altura
    elif altura > segunda_maior_altura:
        segunda_maior_altura = altura
        quantidade_2a_maior_altura = 1
    # Caso igual a segunda maior altura, adiciona uma unidade a quantidade de 2a
    # maior altura
    elif altura == segunda_maior_altura:
        quantidade_2a_maior_altura += 1

print('1a maior altura:', primeira_maior_altura)
print('2a maior altura:', segunda_maior_altura)
print('Pessoas que possuem a 1a maior altura:', quantidade_1a_maior_altura)
print('Quantidade de pessoas que possuem a 2a maior altura:', quantidade_2a_maior_altura)