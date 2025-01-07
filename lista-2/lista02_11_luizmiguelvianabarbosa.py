# Título: Para um dado número N, realiza a implementação da série indicada para se obter
# o número referente a PI
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

import math

n = int(input('n: '))
serie = serie = [-1 / x ** 2 if x % 2 == 0 else 1 / x ** 2 for x in range(1, n)]
print('PI: ', math.sqrt(12 * sum(serie)))