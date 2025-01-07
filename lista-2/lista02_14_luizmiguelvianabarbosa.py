# Título: Realiza saques em um caixa eletrônico com o mínimo de notas possíveis e
# exibe a quantidade de notas utilizadas ao final
# Nome: Luiz Miguel Viana Barbosa
# Data de Criação: 05/01/2025

import copy

opcao_msg = '''
Escolha Sua Opção
1. Sacar Dinheiro
2. Sair
Opção: '''

notas_no_caixa = [
    {'valor': 100, 'quantidade': 10},
    {'valor': 50, 'quantidade': 10},
    {'valor': 20, 'quantidade': 10},
    {'valor': 10, 'quantidade': 10},
    {'valor': 5, 'quantidade': 10},
    {'valor': 1, 'quantidade': 10},
]

def deve_subtrair_nota(notas_no_caixa_copy, total_a_sacar, i):
    quantidade_disp = notas_no_caixa_copy[i]['quantidade']
    valor_atual = notas_no_caixa_copy[i]['valor']
    diff = total_a_sacar - valor_atual
    return 0 <= diff and quantidade_disp > 0

def exibe_notas_disponiveis():
    print('Notas Disponíveis:')
    [print(f'\tValor: R$ {nota["valor"]}\tQuantidade: {nota["quantidade"]}') for nota in notas_no_caixa if nota['quantidade'] > 0]

def exibe_notas_sacadas(notas_no_caixa, notas_no_caixa_copy):
    print('Notas Sacadas:')
    [print(f'\tValor: R$ {notas_no_caixa[i]["valor"]}\tQuantidade: {notas_no_caixa[i]["quantidade"] - notas_no_caixa_copy[i]["quantidade"]}') for i in range(len(notas_no_caixa)) if notas_no_caixa[i]["quantidade"] - notas_no_caixa_copy[i]["quantidade"] > 0]

opcao = int(input(opcao_msg))

while opcao != 2:
    if opcao == 1:
        exibe_notas_disponiveis()
        total_a_sacar = int(input('Total a Sacar: '))
        notas_no_caixa_copy = copy.deepcopy(notas_no_caixa)
        for i in range(len(notas_no_caixa_copy)):
            if total_a_sacar == 0:
                break

            while deve_subtrair_nota(notas_no_caixa_copy, total_a_sacar, i):
                total_a_sacar -= notas_no_caixa_copy[i]['valor']
                notas_no_caixa_copy[i]['quantidade'] -= 1

        if total_a_sacar > 0:
            print('Não há notas suficientes para realizar esta operação, escolha outro valor!')
            exibe_notas_disponiveis()
        else:
            print('Saque realizado com sucesso!')
            exibe_notas_sacadas(notas_no_caixa, notas_no_caixa_copy)
            notas_no_caixa = notas_no_caixa_copy
            
    elif opcao == 2:
        print('Operação Encerrada!')

    else:
        print('Opção Inválida: tente novamente!')

    opcao = int(input(opcao_msg))