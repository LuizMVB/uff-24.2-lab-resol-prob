# Título: Achando o boi mais gordo e o mais magro do frigorífico
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

numero_boi = int(input('Identificação do boi: '))
peso_boi = float(input('Peso do boi: '))

numero_boi_mais_gordo = numero_boi
peso_mais_gordo = peso_boi

numero_boi_mais_magro = numero_boi
peso_mais_magro = peso_boi

# Iterando sobre todos os 90 bois (85 no range porque o primeiro 
# é lido externamente a iteração)
for i in range(89):
    numero_boi = int(input('Identificação do boi: '))
    peso_boi = float(input('Peso do boi: '))
    
    # Caso o peso do boi atual seja maior que o peso do boi mais gordo
    # ele passa a ser o boi mais gordo
    if peso_boi > peso_mais_gordo:
        peso_mais_gordo = peso_boi
        numero_boi_mais_gordo = numero_boi
    
    # Caso o peso do boi atual seja menor que o peso do boi mais magro
    # ele passa a ser o boi mais magro
    if peso_boi < peso_mais_magro:
        peso_mais_magro = peso_boi
        numero_boi_mais_magro = numero_boi

print('Número do boi mais gordo:', numero_boi_mais_gordo, ', Peso:', peso_mais_gordo)
print('Número do boi mais magro:', numero_boi_mais_magro, ', Peso:', peso_mais_magro)

# Resposta: o algoritmo responderá com o número do primeiro boi mais 
# gordo ou mais magro. Pois um novo bpi só é considerado caso o seu peso seja
# maior que o anterior mais pesado ou menor que o mais leve