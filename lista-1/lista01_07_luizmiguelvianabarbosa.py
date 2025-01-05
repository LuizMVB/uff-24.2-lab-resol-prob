# Título: Somando todos os números múltiplos de 4 entre A e B, exclusive os próprios
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

a = int(input('1o número: '))
b = int(input('2o número: '))

# Condição de exceção para exibição de mensagem de erro
if a > b:
    print('O 1o número é maior que o 2o: a soma não será realizada')
else:
    soma = int()
    # Realiza a iteração dentro do range requerido e adiciona cada item 
    # ao valor da soma caso este item seja múltiplo de 4
    for i in range(a+1, b):
        if i % 4 == 0:
            soma += i
    print('Soma dos múltiplos de 4 entre ' + str(a) + ' e ' + str(b) + ' é', soma)