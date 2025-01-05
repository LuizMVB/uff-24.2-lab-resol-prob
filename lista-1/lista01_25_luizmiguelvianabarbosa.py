# Título: Verificando se é possível formar um polígono dado N números
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

n = int(input('Número: '))
somatorio_lados = float()
maior_lado = float()
quantidade_lados = int()

# Itera sobre os números de 0 até n, exclusive
for i in range(n):
    lado = float(input('Lado: '))

    # Caso o lado seja maior que o maior lado até o momento, o maior lado
    # passa a valer o que o lado vale
    if lado > maior_lado:
        maior_lado = lado
        
    # adiciona o lado ao somatório de valores dos lados
    somatorio_lados += lado
    
    # adicionando uma unidade a quantidade de lados
    quantidade_lados += 1
    
# Caso maior lado menor que o somatório (excluindo o mesmo) e a quantidade de lados seja maior que 2, é possível formar polígono
if maior_lado < (somatorio_lados - maior_lado) and quantidade_lados > 2:
    print('É possível montar um polígono')
# Caso contrário, não é possível formar polígono
else:
    print('Não é possível montar um polígono')
        
        
    
