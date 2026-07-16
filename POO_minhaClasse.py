class Pessoa: # Declaração de CLASSE

    x = 5
    # Variaveis declaradas dentro de Classes se tornam ATRIBUTOS
    # X vale 5 para todas as instâncias de objetos

    def __init__(self,name,age=18):
        self.nome = name # ambos os métodos são criados, e cada um assume um valor próprio
        self.idade = age # de acordo com o valor fornecido na chamada da classe

        # O método (função) __init__ é o método construtor do Python...
        # ele nos ajuda a criar atributos e definir valores automaticamente...
        # sempre que chamamos a Classe para criar um objeto

    def __str__(self):
        return f"({self.nome})({self.idade})"
    
        # Normalmente, quando damos print(objeto) o python retorna o endereço na memória
        # Com o __str__ podemos formatar a forma que será o retorno do print(objeto)

    def saudacoes(self):
        print(f'Olá, {self.nome}! Você possui {self.idade}!')
        # self (por convênção) será sempre o primeiro parâmetro a ser passado...
        # para o método, ele serve para acessar o valor do atributo do atual objeto



# Podemos instânciar uma mesma Classe várias vezes, tendo assim vários Objetos ativos
# Cada objeto recebe uma cópia dos atributos e métodos das classes

# Ao atribuirmos uma classe a uma variavel a variavel se torna um OBJETO
pessoa1 = Pessoa()
print(pessoa1.x)

pessoa2 = Pessoa()
pessoa2.x = 67
print(pessoa2.x)
# Aqui a cópia do atributo X relacionada ao obj2 passa a valer 67, mas somente nesse 
# objeto

pessoa3 = Pessoa("Gabriel",19)
# Podemos omitir um dos argumentos, mas para isso é necessário que seja definido
# um valor 'default' no parâmetro da função

pessoa4 = Pessoa("Mano Véio")
# Criando e deletando Atributos fora da classe
pessoa4.cidade = 'Trombudo Central'
del pessoa4.cidade

# Métodos também podem ser deletados com o del

# ==========================================================
# HERANÇA- Criando classes filhas
# ==========================================================

# -> Classe Pai: Aquele que é referênciada
# -> Classe Filha: Aquela que usa como base atributos e métodos da Pai
class Estudante(Pessoa):
    pass

aluno1 = Estudante("Julio",24)
print(aluno1)
