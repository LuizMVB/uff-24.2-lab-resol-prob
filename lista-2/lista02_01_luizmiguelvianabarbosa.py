# Título: Lê 50 valores de temperaturas em graus Celssius, tranforma em Farenheit 
# e imprime e média em Celssius e Farenheit e quantas temperaturas acima da média em 
# Farenheit
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

n = 50
temp_celssius_list = [float(input('Temperatura em Celssius: ')) for _ in range(n)]
temp_faranheit_list = [c * 1.8 + 32 for c in temp_celssius_list]
media_temp_celssius = sum(temp_celssius_list) / len(temp_celssius_list)
media_temp_faranheit = sum(temp_faranheit_list) / len(temp_faranheit_list)

print('Média em Celssius:', media_temp_celssius)
print('Média em Faranheit:', media_temp_faranheit)
print('Temperaturas em Faranehit acima da média:')
[print('\t-', f) for f in temp_faranheit_list if f > media_temp_faranheit]