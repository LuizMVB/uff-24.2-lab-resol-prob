# Título: Verifica se uma palavra é anagrama da outra
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

BRANCO = ' '
VAZIO = ''

def anagrama(frase1: str, frase2: str):
    if set(frase1) == set(frase2):
        return True
    return False

# frase1 = input('Frase 1: ').upper().replace(BRANCO, VAZIO)
# frase2 = input('Frase 2: ').upper().replace(BRANCO, VAZIO)

# if anagrama(frase1, frase2):
#     print('É um Anagrama')
# else:
#     print('Não é um Anagrama')