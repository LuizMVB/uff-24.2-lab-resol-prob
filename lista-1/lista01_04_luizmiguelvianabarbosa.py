# Título: Lendo o nome e preço de cada produto e exibindo o mais caro
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

nome_produto = input('Nome do produto: ')
preco_produto = float(input('Preço do produto: '))

nome_produto_mais_caro = str()
maior_preco = float()

# Definindo via while, pois não é definido um limite de número de 
# produtos estaticamente
while nome_produto != 'XXX':
  
    # Caso o preco do produto seja maior que o maior preco, define 
    # um novo produto mais caro
    if preco_produto > maior_preco:
        maior_preco = preco_produto
        nome_produto_mais_caro = nome_produto
    
    nome_produto = input('Nome do produto: ')
    
    # Condição de saída pelo nome do produto restringindo a entrada de 
    # um novo preço desnecessariamente 
    if nome_produto != 'XXX':
        preco_produto = float(input('Preço do produto: '))

print('Produto mais caro:', nome_produto_mais_caro)





