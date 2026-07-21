class Personagem:

    def __init__(self,nome):
        self.__name = nome
        self.__life = 100
        self.__basic_attack = 20
        

    def get_name(self):
        return self.__name
    

    def get_life(self):
        return self.__life
    

    def get_basic_attack(self):
        return self.__basic_attack


    def is_alive(self):
        if self.__life > 0:
            return True
        else:
            return False
        
    def take_damage(self,num_damage):
        self.__life -= num_damage

        if self.__life < 0:
            self.__life = 0

        return self.get_life()
    

    def attack(self,target):
        pass