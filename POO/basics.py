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
pessoa1 = Pessoa("Julio")
print(pessoa1.x)

pessoa2 = Pessoa("Marcos")
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

# ============================================================================
# HERANÇA- Criando classes filhas
# Determina que uma classe pode existir por si mesma, porém, também pode possuir
# outra classe em sua essência.
# A classe que herda poderá ter seus próprios dados, porém vai herdar os 
# métodos e funções da classe superior. (Conta -> ContaBancária -> ContaPoupança)
# ============================================================================

# -> Classe Pai: Aquele que é referênciada
# -> Classe Filha: Aquela que usa como base atributos e métodos da Pai
class Estudante(Pessoa):

# A classe filha vai herdar todos os métodos e atributos da classe pai
   # x = 5
   # nome = Julio
   # idade = 24
   # def __str__(self):
   # def saudacoes(): 

    def __init__(self, name, age, cod_aluno, media_final):# construtor da classe Estudante
        super().__init__(name,age) # chama construtor da classe pai (super referencia a classe pai)
        self.cod_aluno = cod_aluno 
        self.media_final = media_final # atributos criados exclusivamente para Estudante (pelo init externo)

    def bemvindo(self):
        print(
            f'Bem vindo Aluno: {self.name}, seu código é {self.cod_aluno}\n'
            f'Sua última média foi {self.media_final}.'
            )


aluno1 = Estudante("Julio",24, 1041044, 8.8)
print(aluno1.x)
aluno1.saudacoes()
print(aluno1)

# ============================================================================
# POLIMORFISMO 
# Capacidade de subclasses reutilizarem métodos e atributos de outras classes,
# comumente usado em  classes pais/abstratas.
# Usada para definir regras que serão reutilizadas e que são bases de N subclasses
# Cachorro.late() --->  Salsicha.late() -> Pinscher.late()
# ============================================================================

class Veiculo:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Carro(Veiculo):
   pass # classe Carro (filha) usa do 'move()' da classe Veiculo

class Barco(Veiculo):
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):  # classes filhas que implementam os métodos da classe pai
    print("Sail!") # porém caso definida explicitamente na classe filha
                   # ela sobreescreve o método da classe pai
class Aviao(Veiculo):
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

carro1 = Carro("Ford", "Mustang")   
barco1 = Barco("Ibiza", "Touring 20") 
aviao1 = Aviao("Boeing", "747")     

for x in (carro1, barco1, aviao1):
  x.move()

# Todas as Classes possuem o método 'move()'
# O polimorfismo nos permite que um mesmo Método seja reutilizado em diversas Classes

# ============================================================================
# ENCAPSULAMENTO  
# Forma de manter dados seguros e com restrição de acesso dentro de uma classe.
# Previne alterações acidentais de variaveis.
# Permite validar entradas de dados antes de settar
# O código de implementação e validação é interno, não presente fora da classe.
# uso do prefixo: __cpf
# ============================================================================

# getter: função que retorna um valor
# setter: função que atribui um valor
# __.atr : privado, so poderá ser alterado através de função, não diretamente
# _.atr : protegido, apenas uma convenção, transmite a outros programadores que
# se possível não alterar a variável, porém o python não impede isso.

class Cachorro:
  
  __raca_cachorro = ''

  def __init__(self, name, sexo):
    self.nome = name
    self._sexo = sexo
    
  def get_raca(self): # getter
    return self.__raca_cachorro
  
  def set_raca(self,raca_cachorro): #setter
    if not raca_cachorro:
        return 'Nomes vazios não são válidos'
    else:
        self.__raca_cachorro = raca_cachorro
        return 'Raça definida!'

c1 = Cachorro("Tobias","Macho")
print(c1.set_raca("Pastor Alemão"))
print(c1.get_raca())