# Título: Lê o arquivo entrada.txt e conta quantas vezes cada letra do alfabeto 
# (independentemente de ser maiúscula ou minúscula) aparece. Grava o resultado em um
# arquivo saida.txt, com a letra e o número de ocorrências em um formato específico
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

import os

CARACTERES_INDESEJADOS = '.!,:;?\'"\n123456789'
VAZIO = ''

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(current_dir + '/entrada.txt', 'r') as file:
    conteudo = file.read()
tabela_traducao = str.maketrans(VAZIO, VAZIO, CARACTERES_INDESEJADOS)
conteudo_limpo_list = conteudo.translate(tabela_traducao).upper().strip().split(' ')

frequencia_palavras_dict = dict()

for palavra_atual in conteudo_limpo_list:
    frequencia_palavras_dict[palavra_atual] = frequencia_palavras_dict.get(palavra_atual, 0) + 1

with open(current_dir + '/saida.txt', 'w') as file:
    for chave, valor in frequencia_palavras_dict.items():
        file.write(chave + ' ' + str(valor) + '\n')