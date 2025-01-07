# Título: Lê uma frase e imprime o total de vogais, o total de brancos e o total do resto.
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

VOGAIS = 'AEIOU'
BRANCO = ' '

frase = input('Frase: ').upper()

total_vogais = sum(1 for letra in frase if letra in VOGAIS)
total_brancos = frase.count(BRANCO)
total_resto = len(frase) - total_vogais - total_brancos

print('Total de Vogais:', total_vogais)
print('Total de Brancos:', total_brancos)
print('Total de Resto:', total_resto)