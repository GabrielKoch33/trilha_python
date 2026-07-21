
class Usuario():

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_em_uso = []
        # Um user não pode ter mais que 3 livros emprestados ao mesmo tempo
    
    def set_nome_user(self,nome_usuario):
        self.nome = nome_usuario

    def get_nome_user(self):
        return self.nome

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula

    def set_livros_usados(self,obj_livro):
        if len(self.get_livros_usados()) < 3:
            self.livros_em_uso.append(obj_livro)
            return True
        else:
            return False
    
    def get_livros_usados(self):
        return self.livros_em_uso
    
    def remover_livro(self, obj_livro):
        if obj_livro not in self.livros_em_uso:
            return False
        else:
            self.livros_em_uso.remove(obj_livro)
            return True