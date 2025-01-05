# Título: Calculando a raíz inteira de um número
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 17/11/2024

n = int(input("N: "))
r = 0

# Enquanto 
while (r + 1) * (r + 1) <= n:
    r += 1

# Exibindo o resultado
print("Raiz inteira:", r)