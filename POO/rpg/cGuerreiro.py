from cPersonagem import Personagem

class Guerreiro(Personagem):

    def __init__(self, nome, ataque_basico):
        super().__init__(nome)