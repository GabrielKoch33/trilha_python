print('Diga dois numeros:')
n1 = int(input('1º Nº'))
n2 = int(input('2º Nº'))
op = 100000
while op != 0:#Após executar o If, retorna ao inicio do While
    print('---MENU---')
    print(' 1 - SOMAR DOIS NÚMEROS ')
    print(' 2 - Mostrar maior número ')
    print(' 3 - Mostrar tabuada')
    print(' 0 - Sair do programa')
    op = int(input('Digite a opção escolhida: '))

    if  op != 0 and op != 1 and op != 2 and op != 3:
        print('OPÇÃO INVÁLIDA')
        break

    elif op == 0:
        print('Obrigado por utilizar o programa! \n Saindo...')
        break

    elif op == 1:
        soma = n1 + n2
        print(soma)
        yn = input('Deseja continuar? [S/N]')
        if yn == 'n':
            break

    elif op == 2:
        if n1 > n2:
            print(f'Maior Número é:{n1}')
        else:
            print(f'Maior Número é:{n2}')
        yn = input('Deseja continuar? [S/N]')
        if yn == 'n':
            break

    elif op == 3:
        print('Tabuada do N1')
        for i in range(1,11):
            print(f'{i} X {n1} = {i*n1}')
        print('Tabuada do N2')
        for j in range(1,11):
            print(f'{j} X {n2} = {n2*j}')
        yn = input('Deseja continuar? [S/N]')
        if yn == 'n':
            break

