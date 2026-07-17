from cBiblioteca import Biblioteca

class Usuario(Biblioteca):

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_em_uso = []
# Um user não pode ter mais que 3 livros emprestados ao mesmo tempo

