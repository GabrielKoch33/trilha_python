class Cliente:

    lista_veiculo = []

    def __init__(self, nome, cpf, telefone):
        self.nome     = nome
        self.cpf      = cpf
        self.telefone = telefone 
        
    def __str__(self):
        return f'NOME: {self.nome} - CPF: {self.cpf} - TELEFONE: {self.telefone}'
    
    
    
