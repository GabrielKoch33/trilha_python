from cBiblioteca import Biblioteca

class Livro(Biblioteca):

    # __init__ serve para atribuirmos valores aos atributos 
    # durante cada instancia do objeto
    # se definíssimos fora do init, o valor seria global para todo objeto
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
        pass

    def emprestar():
        pass

    def devolver():
        pass
    
    