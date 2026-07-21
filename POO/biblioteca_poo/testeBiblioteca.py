import cBiblioteca as lib
import cUsuario as usr
import cLivro as liv

obj_gabriel = usr.Usuario('Gabriel', 1024)
obj_daniele = usr.Usuario('Daniele', 1452)
obj_thais = usr.Usuario('Taís', 2343)
obj_andrei = usr.Usuario('Andrei',4741)

obj_it = liv.Livro('IT: A coisa', 'Stephen King',100)
obj_1984 = liv.Livro('1984','George Orwell',101)
obj_hobbit = liv.Livro('O Hobbit', 'Tolkien', 102),
obj_duna = liv.Livro('Duna', 'Frank Herbert', 103),
obj_rev_bichos = liv.Livro('A Revolução dos Bichos', 'George Orwell', 104),


obj_biblioteca = lib.Biblioteca()
if obj_biblioteca.cadastrar_livro(obj_it):
    print(f'Livro: {obj_it.get_titulo} cadastrado!')