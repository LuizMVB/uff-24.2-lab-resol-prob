# Título: Escrevendo os N primeiros termos de uma PA
# Nome: Luiz Miguel Viana Barbosa
# Data: 17/11/2024

n = int(input('número de termos: '))
primeiro_termo = int(input('primeiro_termo: '))
razao = int(input('razão: '))

termo_atual = primeiro_termo

print('\nLISTA DE TERMOS\n')

# Iterando a partir do primeiro temro e adicionando a razão a cada iteração
for i in range(n):
    print(str(i + 1) + 'o termo: ', termo_atual)
    termo_atual = termo_atual + razao