from cBiblioteca import Biblioteca
from cLivro import Livro
from cUsuario import Usuario

pessoas = [
    Usuario('Gabriel', 1024),
    Usuario('Daniele', 1452),
    Usuario('Taís', 2343),
    Usuario('Andrei',4741)
]

livros = [
    Livro("Dom Casmurro", "Machado de Assis", "001"),
    Livro("1984", "George Orwell", "002"),
    Livro("O Hobbit", "Tolkien", "003"),
    Livro("Duna", "Frank Herbert", "004"),
    Livro("A Revolução dos Bichos", "Orwell", "005"),
    Livro('IT: A coisa', 'Stephen King',100)
]

biblioteca = Biblioteca()

for l in livros:
    biblioteca.cadastrar_livro(l)
    print(f'Livro: "{l}" - Cadastrado!')

print('-'*30)

for p in pessoas:
    biblioteca.cadastrar_usuario(p)
    print(f'Pessoa: "{p}" - Cadastrado(a)!')

pessoa_ = pessoas[0]
livro_ = livros[3]

if biblioteca.emprestar_livro(livro_,pessoa_):
    print(f'{pessoa_} pegou o livro: {livro_}')
else:
    print(f'{pessoa_} não conseguiu o livro: {livro_} pois o mesmo já está emprestado')

pessoa_2 = pessoas[2]

if biblioteca.emprestar_livro(livro_,pessoa_2):
    print(f'{pessoa_2} pegou o livro: {livro_}')
else:
    print(f'{pessoa_2} não conseguiu o livro: {livro_} pois o mesmo já está emprestado')