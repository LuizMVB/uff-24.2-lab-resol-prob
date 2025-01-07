# Título: Enumera todas as subsequências não contínuas de uma dada sequência
# Nome: Luiz Miguel Viana Barbosa
# Data de criação: 05/01/2025

def gerar_sequencias_nao_continuas(sequencia, passo = 0):
    if sequencia:
        atual = sequencia[:1]
        faltantes = sequencia[1:]
        passo_par = passo % 2
        passo_impar = not passo_par

        subsequencia_com_atual_list = []
        for subsequencia in gerar_sequencias_nao_continuas(faltantes, passo + passo_impar):
            subsequencia_com_atual_list .append(atual + subsequencia)

        subsequencia_sem_atual_list = gerar_sequencias_nao_continuas(faltantes, passo + passo_par)

        return subsequencia_com_atual_list + subsequencia_sem_atual_list
    else:
        return [[]] if passo >= 3 else []

res = gerar_sequencias_nao_continuas([1, 2, 3, 4])

for subsequence in res:
    print(" ".join(map(str, subsequence)))
