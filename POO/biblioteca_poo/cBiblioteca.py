class Biblioteca():

    def __init__(self):
        self.acervo = [] #lista de livros
        self.usuarios = [] #lista de usuarios


    def cadastrar_livro(self,obj_livro):
        self.acervo.append(obj_livro)
        return True


    def cadastrar_usuario(self, obj_usuario):
        self.usuarios.append(obj_usuario)
        return True


    def emprestar_livro(self, obj_livro, obj_usuario):
        if not obj_livro.get_disponibilidade() or len(obj_usuario.get_livros_usados()) == 3:
            return False
        else:
            obj_usuario.set_livros_usados(obj_livro)
            obj_livro.emprestar()
            return True

    def devolver_livro(self, obj_livro, obj_usuario):
        if obj_livro.get_disponibilidade() or len(obj_usuario.get_livros_usados()) == 0:
            return False
        else:
            if not obj_usuario.remover_livro(obj_livro):
                return False
            else:
                obj_livro.devolver()
                return True
            

    def listar_disponiveis(self):
        for livro in self.acervo:
            if livro.get_disponibilidade():
                result = livro.get_dados_livros()
                print(result[0])
                print(result[1])
                print(result[2])
