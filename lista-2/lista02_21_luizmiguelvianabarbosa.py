# Título: Lê um arquivo entrada.txt e troca todas as letras minúsculas por 
# maiúsculas e vice-versa para grava-las em um arquivo saida.txt
# e cria dois vetores distintos
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(current_dir + '/entrada.txt', 'r') as file:
    conteudo = file.read()
conteudo_tranformado = ''.join([letra.lower() if letra.isupper() else letra.upper() for letra in conteudo])
with open(current_dir + '/saida.txt', 'w') as file:
    conteudo = file.write(conteudo_tranformado)