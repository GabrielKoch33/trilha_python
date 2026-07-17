class Biblioteca():

    acervo = [] #lista de livros
    usuarios = [] #lista de usuarios


    def cadastrar_livro():
        pass

    def cadastrar_usuario():
        pass

    def emprestar_livro():
        '''
Verifica se o livro existe e está disponível
Verifica se o usuário existe e não passou do limite de 3 livros
Se tudo ok: marca o livro como indisponível e adiciona à lista do usuário
Se algo falhar: deve avisar o motivo
        '''
        pass

    def devolver_livro():
        pass

    def listar_disponiveis():
        pass

while True:
    print(
        '1 - CADASTRAR LIVRO'
        '2 - CADASTRAR USUÁRIO'
        '3 - EMPRESTAR LIVRO'
        '4 - DEVOLVER LIVRO'
        '5 - LISTAR LIVROS DISPONÍVEIS'
         )
    opcao = int(input('Digite uma opção:'))

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        pass
    else:
        print('Opção Inválida!')