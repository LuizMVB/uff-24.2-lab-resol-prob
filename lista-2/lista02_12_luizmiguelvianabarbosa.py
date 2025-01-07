# Título: Recebe uma lista ordenada e devolve uma lista contendo uma representação
# com o número sendo elevado a quantidade de vezes que ele aparece
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

def add_valor(anterior, contador, lista_saida):
    if contador <= 1:
        lista_saida.append(anterior)
    else:
        lista_saida.append(anterior + '^' + str(contador))

def condensar_elementos(lista_entrada_ordenada):
    anterior = lista_entrada_ordenada[0]
    contador = 1
    lista_saida = []

    for i in range(1, len(lista_entrada_ordenada)):
        atual = lista_entrada_ordenada[i]
        if atual == anterior:
            contador += 1
        else:
            add_valor(anterior, contador, lista_saida)
            contador = 1
            anterior = atual

    add_valor(anterior, contador, lista_saida)
    return lista_saida

# tamanho_da_lista = int(input('Tamanho da lista: '))
# lista_entrada_ordenada = [input('Número: ') for _ in range(tamanho_da_lista)]
# lista_saida = condensar_elementos(lista_entrada_ordenada)
# print(lista_saida)