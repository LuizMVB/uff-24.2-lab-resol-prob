# Título: Obtendo o total gasto pela empresa o seu produto mais caro através 
# da sua lista de produtos
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

total_gasto = float()
descricao_produto_mais_caro = str()
maior_preco_unitario = float()

# Condição bem definida de 10 produtos, por isso o uso do for
for i in range(10):
    descricao_produto = input('Descrição do produto: ')
    preco_unitario = float(input('Preço unitário: '))
    quantidade = int(input('Quantidade: '))
    
    # Calculando o total gasto nessa categoria de produto 
    total_gasto += preco_unitario * quantidade
    
    # Caso o preço unitário seja maior que o maior gasto estabelecido, 
    # define um novo maior gasto
    if preco_unitario > maior_preco_unitario:
        maior_preco_unitario = preco_unitario
        descricao_produto_mais_caro = descricao_produto

print('Total gasto pela empresa:', total_gasto)
print('Descrição do produto mais caro:', descricao_produto_mais_caro)






