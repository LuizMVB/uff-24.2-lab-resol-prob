# Título: Verifica se uma palavra é um palindromo
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

BRANCO = ' '
VAZIO = ''

def palindromo(palavra: str):
    if palavra == palavra[::-1]:
        return True
    return False

# palavra = input('Palavra: ').upper().replace(BRANCO, VAZIO)

# if palindromo(palavra):
#     print('É palindromo')
# else:
#     print('Não é palindromo')