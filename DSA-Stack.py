def cheia (ponteiro):
    if ponteiro > 5:
        return True #Por padrão retorna true
    return False# Senão, falso

def incluir(pilha,ponteiro):
    if cheia(ponteiro):
        return f'Pilha Cheia, {ponteiro} Posições preenchidas'
        #O return serve para devolver um valor de dentro da função para quem a chamou, e também encerra a execução da função naquele ponto.
    else:
        pilha[ponteiro] = input(f'informe um número: ')
        return pilha,ponteiro + 1

def remover (pilha,ponteiro):
    if ponteiro == 1:
        return 'Pilha Vazia, nada a remover'
    else:
       print(f'Número removido: {pilha[ponteiro-1]}')
       return pilha, ponteiro - 1

def escrever (pilha, ponteiro):
    for i in range(ponteiro):
        print(pilha[i])

def checarproximo (pilha,ponteiro):
     print(f'O Próximo a sair da pilha é: {pilha[ponteiro-1]}')

ponteiro = 0
opcao = 10
pilha = [0,0,0,0,0]

while opcao != 0:
    print('---MENU---')
    print('0 - SAIR')
    print('1 - INCLUIR NUMERO')
    print('2 - REMOVER NUMERO')
    print('3 - ESCREVER PILHA')
    print('4 - CONSULTAR ULTIMO')
    print('5 - VAZIA OU CHEIA')

    op = int(input('Digite uma opção: '))
    if op == 0:
        break
    if op == 1:
        pilha, ponteiro = incluir(pilha,ponteiro)
    elif op == 2:
       pilha, ponteiro =  remover (pilha,ponteiro)
    elif op == 3:
        escrever(pilha,ponteiro)
    elif op == 4:
        checarproximo(pilha,ponteiro)
    elif op == 5:
        cheia(ponteiro)
        if ponteiro == 5:
            print('Pilha Cheia')
        elif ponteiro == 1:
            print('Pilha Vazia')
        else:
            print('Pilha Com Espaços Livres')

#Remover não funciona
#Quebra se adicionar na pilha cheia
