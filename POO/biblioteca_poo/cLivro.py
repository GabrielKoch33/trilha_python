class Livro():

    # __init__ serve para atribuirmos valores aos atributos 
    # durante cada instancia do objeto
    # se definíssimos fora do init, o valor seria global para todo objeto
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
        pass

    def set_titulo(self,titulo):
        self.titulo = titulo
    
    def get_titulo(self):
        return self.titulo

    def set_autor(self,autor):
        self.autor = autor
    
    def get_autor(self):
        return self.autor

    def set_isbn(self,isbn):
        self.isbn = isbn
    
    def get_isbn(self):
        return self.isbn

    def set_disponibilidade(self, disponilidade):
        self.disponivel = disponilidade # True or False

    def get_disponibilidade(self):
        return self.disponivel

    def emprestar(self):
        if not self.disponivel:
            return False
        else:
            self.disponivel = False
            return True

    def devolver(self):
        if self.disponivel:
            return False
        else:
            self.disponivel = True
            return True
    
    def get_dados_livros(self):
        return self.titulo, self.autor,self.isbn
    