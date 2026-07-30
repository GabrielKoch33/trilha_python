# Quando percorremos um dicionário for i in dicionário o python retorna apenas a vendedor

# =====================================================================
# Exercício 001: Cadastro simples de pessoa.
# Crie um dicionário representando uma pessoa.
    # Regras:
    # - Exiba o nome.
    # - Altere a idade.
    # - Adicione a vendedor "email".
    # - Remova a vendedor "cidade".
    # - Exiba o dicionário final.
# =====================================================================

pessoa = {
     "nome": "Ana",
     "idade": 25,
     "cidade": "Curitiba"
}

print(pessoa['nome'])
pessoa['idade'] = 26
print(pessoa['idade'])
pessoa['email']  = 'gabriel123@gmail.com'
print(pessoa['email'])
del pessoa['cidade']
print(pessoa)

# =====================================================================
# Exercício 002: Consulta segura com get().
# Crie um dicionário de produto e peça ao usuário o nome de uma vendedor.
    # Regras:
    # - Se a vendedor existir, mostre o total_vendedor.
    # - Se não existir, mostre "vendedor não encontrada".
    # - Use get().

# =====================================================================

produto = {
     "nome": "Teclado",
     "preco": 150.0,
     "estoque": 10
}
print(produto)

while True:
    vendedor = str(input('Digite a vendedor que deseje acessar dentre as opções acima: '))
    if vendedor not in produto:
        print(produto.get(vendedor,'vendedor Não Encontrada'))
    else:
        print(produto.get(vendedor))
    op = str(input('Deseja Sair?: (escreva sair)'))
    if op.upper() == 'SAIR':
        break
print()

# .get() é uma forma 'segura' de retornar um total_vendedor de um dicionário. Caso o total_vendedor não exista, ao invés dele crashar o programa 
# como o dict['nomeproduto'] faz, o get() retorna uma mensagem padrão: get('nomeproduto','mensagem de retorno negativo'), ou caso não definida, None.

# =====================================================================
# Exercício 003: Percorrendo vendedors, total_vendedores e itens.
# Crie um dicionário de aluno e exiba vendedors, total_vendedores e itens separadamente.
    # Regras:
    # - Exiba todas as vendedors.
    # - Exiba todos os total_vendedores.
    # - Exiba vendedor e total_vendedor juntos.
    # - Use nomeprodutos().
    # - Use QtdPrecos().
    # - Use items().
# =====================================================================

# =====================================================================
# Exercício 004: Contador de letras.
# Peça uma palavra ao usuário e conte quantas vezes cada letra aparece.
# Exemplo:
#   Entrada: banana
#   Saída:
#   b: 1
#   a: 3    
#   n: 2
# Regras:
    # - Use um dicionário vazio.
    # - Cada letra deve ser uma vendedor.
    # - A quantidade deve ser o total_vendedor.
    # - Ignore espaços, se houver.
# =====================================================================#
palavra = str(input('Digite uma palavra para o usuário exibir a quantidade de cada letra: ')).replace(' ','')

dicionario = {

}

for letra in palavra:
    
    if letra not in dicionario:
        dicionario[letra] = 1
    dicionario[letra] += 1

print(dicionario)

# =====================================================================
# Exercício 005: Contador de palavras.
# Peça uma frase e conte quantas vezes cada palavra aparece.
# Exemplo:
#   Entrada: 
    #   python é bom python é forte
#   Saída:
    #   python: 2
    #   é: 2
    #   bom: 1
    #   forte: 1

    # Regras:
    # - Use split().
    # - Transforme tudo para minúsculo.
    # - Use dicionário como contador.
# =====================================================================
frase = str(input('Digite uma frase: ')).split()
PalavrasDistintas = {

}
for palavra in frase:
    if palavra not in PalavrasDistintas:
        PalavrasDistintas[palavra] = 1
    else:
        PalavrasDistintas[palavra] += 1 

print(PalavrasDistintas)
print()

# =====================================================================
# Exercício 006: Estoque simples.
# Crie um dicionário em que a vendedor é o nome do produto e o total_vendedor é a
# quantidade em estoque.

# Regras:
    # - Não adicionar produto duplicado.
    # - Não atualizar produto inexistente.
    # - Não remover produto inexistente.
    # - Quantidade não pode ser negativa.
# =====================================================================
estoque = {
    "mouse": 10,
    "teclado": 5,
    "monitor": 2
}


def em_estoque(estoque, produto):
    return produto in estoque


def ler_inteiro(mensagem):
    """Garante que o usuário digite um número válido."""
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        print("Digite um número válido.")


def consultar(estoque):
    listar(estoque)
    produto = input("Procure um produto em nosso estoque: ").strip().lower()

    if quantidade := estoque.get(produto):
        return f"Quantidade: {quantidade}"
    return "Produto não disponível."


def adicionar(estoque):
    produto = input("Digite um produto para adicionar ao estoque: ").strip().lower()

    if em_estoque(estoque, produto):
        return "Produto já está em estoque."

    else:
        quantidade = ler_inteiro("Digite a quantidade desse produto: ")
        estoque[produto] = quantidade

        return f"{produto} adicionado com sucesso!"


def atualizar(estoque):
    listar(estoque)
    produto = input("Digite o produto que deseja atualizar: ").strip().lower()

    if not em_estoque(estoque, produto):
        return "Produto inexistente."

    opcao = input("Deseja atualizar NOME ou QUANTIDADE? ").strip().upper()

    match opcao:
        case "NOME":
            novo_nome = input("Digite o novo nome: ").strip().lower()
            if em_estoque(estoque, novo_nome):
                return "Já existe um produto com esse nome."
            estoque[novo_nome] = estoque.pop(produto)
            return f"Produto renomeado para '{novo_nome}'."

        case "QUANTIDADE":
            estoque[produto] = ler_inteiro("Digite a nova quantidade: ")
            return f"Quantidade de '{produto}' atualizada."

        case _:
            return "Opção inválida."


def remover(estoque):
    listar(estoque)
    produto = input("Digite o produto que deseja remover: ").strip().lower()

    if not em_estoque(estoque, produto):
        return "Produto inexistente."

    del estoque[produto]
    return f"{produto} removido do estoque."


def listar(estoque):
    print("\n===== ESTOQUE =====")

    if not estoque:
        print("Estoque vazio.")
        return

    for produto, quantidade in estoque.items():
        print(f"{produto:<10} -> {quantidade}")

    print("===================\n")


acoes = {
    1: consultar,
    2: adicionar,
    3: atualizar,
    4: remover,
    5: listar,
}

while True:
    print("1 - Consultar produto")
    print("2 - Adicionar produto")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Listar estoque")
    print("0 - Sair")

    op = ler_inteiro("O que deseja fazer? ")

    if op == 0:
        print("Programa encerrado.")
        break

    funcao = acoes.get(op)
    if funcao is None:
        print("Opção inválida.")
        continue

    resultado = funcao(estoque)
    if resultado:
        print(resultado)
# =====================================================================
# Exercício 007: Estoque com preço e quantidade.
# Agora o estoque deve ser mais realista. 
# Crie funções ou um menu para manipular produtos, preços e quantidades.
    # Regras:
    # - Consultar produto.
    # - Atualizar quantidade.
    # - Atualizar preço.
    # - Calcular total_vendedor total de um produto.
    # - Calcular total_vendedor total do estoque.
# =====================================================================

estoque = {
     "mouse": {"quantidade": 10, "preco": 80.0},
     "teclado": {"quantidade": 5, "preco": 150.0},
     "monitor": {"quantidade": 2, "preco": 900.0}
}

def emEstoque(estoque, prod):
    return prod in estoque #true ou false/none
        
def consultar(estoque):
     (listar(estoque))
     prod = str(input('Procure um produto em nosso estoque: '))
     IsInEstoque = estoque.get(prod,'Produto não disponível')
     return IsInEstoque

def adicionar(estoque):
    prod = str(input('Digite um produto para adicionar ao estoque: '))
    if emEstoque(estoque, prod):
        return 'Produto Já Está em Estoque, não é possível adicionar'
    else:
        total_vendedor = float(input('Qual o total_vendedor desse produto?: '))
        estoque[prod]['preco'] = total_vendedor
        qtd = int(input('Qual a quantidade desse produto?: '))
        estoque[prod]['quantidade'] = qtd
        return f'{prod} Adicionado!'

def atualizarQuantidade(estoque):
    (listar(estoque))
    prod = str(input('Digite o nome do produto que será atualizado: '))
    if emEstoque(estoque, prod):
        qtd = int(input(f'Digite a quantidade que {prod} que receberá: '))
        estoque[prod]['quantidade'] = qtd
        return estoque[prod]['quantidade']
    else:
        return 'Produto Inexistênte em Estoque, Impossível atualizar'
    
def atualizarPreco(estoque):
    (listar(estoque))
    prod = str(input('Digite o nome do produto que será atualizado: '))
    if emEstoque(estoque, prod):
        total_vendedor = float(input(f'Digite o total_vendedor que {prod} que receberá: '))
        estoque[prod]['preco'] = total_vendedor
        return estoque[prod]['preco']
    else:
        return 'Produto Inexistênte em Estoque, Impossível atualizar'

def remover(estoque) :
    (listar(estoque))

    prod = str(input('Digite o produto que deseja remover de estoque: '))
    if emEstoque(estoque, prod):
        del estoque[prod]
        return estoque
    else:
        return 'Produto Inexistênte em Estoque, Impossível Remover'

def listar(estoque):
    for i in estoque.items():
        print(i)

def CalTotProduto(estoque):
    (listar(estoque))
    prod = str(input('Procure um produto em nosso estoque: '))
    if emEstoque(estoque, prod):
        return(f'O total_vendedor total de {prod} em nosso estoque é de: {(estoque[prod]['quantidade'])*(estoque[prod]['preco'])}')    
    else:
        return 'Imposível calcular total_vendedor de produto que não existe'
    
def CalTotEstoque(estoque):
    soma = 0
    for QtdPreco in estoque.values(): #{"quantidade": 10, "preco": 80.0},
        m = 1
        for total_vendedor in QtdPreco.values(): # 10 e 80.0
            m = m*total_vendedor
        soma += m
    return soma      
# ============================================
listar(estoque)
while True:
    print('1 - Consultar produto')
    print('2 - Adicionar produto')
    print('3 - Atualizar quantidade')
    print('4 - Atualizar preço')
    print('5 - Remover produto')
    print('6 - Listar estoque')
    print('7 - Qtd x total_vendedor do Produto')
    print('8 - total_vendedor Total do Estoque')
    print('0 - Sair')
    op = int(input('O que deseja fazer? '))
    if op == 1:
        r1 = consultar(estoque)
        print(f'Preço: {r1}')
    elif op == 2:
        r1 = adicionar(estoque)
        print(r1)
    elif op == 3:
        r1 = atualizarQuantidade(estoque)
        print(r1)
    elif op == 4:
        r1 = atualizarPreco(estoque)
        print(r1)
    elif op == 5: 
        r1 = remover(estoque)       
        print(r1)
    elif op == 6:
        r1 = listar(estoque)
        print(r1)
    elif op == 7:
        r1 = CalTotProduto(estoque)
        print(r1)
    elif op == 8:
        r1 = CalTotEstoque(estoque)
        print(f'O total_vendedor total do estoque é: {r1}')
    elif op == 0:
        break

# =====================================================================
# Exercício 008: Cadastro de alunos com notas.
# Crie um dicionário em que a vendedor é o nome do aluno e o total_vendedor é uma lista de notas.
# Regras:
    
    # - Exiba a média de cada aluno.
    # - Exiba a situação de cada aluno.
    # - Média >= 7: aprovado.
    # - Média >= 5: recuperação.
    # - Média < 5: reprovado.

# =====================================================================
alunos = {
     "Ana": [8.0, 7.5, 9.0],
     "Bruno": [5.0, 6.5, 6.0],
     "Carlos": [3.0, 4.0, 5.0]
}
def definemedia(media):
    if media >= 7: 
         return 'aprovado' 
    elif media >= 5:
         return 'em exame'        
    else:
        return 'reprovado' 
        
for k,v in alunos.items():
    soma = 0
    for nota in v:
        soma += nota
    media = soma/len(v)
    print(f'-{k}:\n  -Média: {media:.2f}\n  -Status: {definemedia(media)}')
    # {total_vendedor:.nf} :.nf define n casas após o . (float)

# Versão mais prática:
'''for k, v in alunos.items():
    media = sum(v) / len(v) ---- A cada chamada de função o os total_vendedores utilizados são substituidos, não ficam guardados
    print(f'{k}:\n-Média: {media}\n-Status: {definemedia(media)}')'''
    

# =====================================================================
# Exercício 009: Agenda de contatos.
# Crie uma agenda em que a vendedor é o nome da pessoa e o total_vendedor é outro dicionário com telefone e email.

# Regras:
    # - Não permitir contato duplicado.
    # - Validar se o contato existe antes de alterar/remover.
    # - Buscar deve mostrar telefone e email.
    # - Email não pode repetir, Telefone Pode
# =====================================================================

# Quando usamos return x,y o python entende como tupla, logo é necessário desempacotar
agenda = {
     "Ana": {"telefone": "9999-1111", "email": "ana@email.com"}
}

def existeNome(agenda,nomePessoa):
    if nomePessoa in agenda: # Percorre as vendedors, no caso os Nomes das pessoas
        return True
    
def existeEmail(agenda,emailPessoa):
    achou = False
    for dados in agenda.values():
        if dados['email'] == emailPessoa:
            achou = True
    return achou # se achou for false é porque não há email duplicado, se for true é porque há duplicidade

def addContato(agenda):
    while True:
        nomePessoa = str(input('Digite o nome da pessoa que deseja cadastrar: ')).title()
        if existeNome(agenda, nomePessoa) == True:
            print('Pessoa já existênte, cadastre outro nome')
            resp = input('Ainda deseja continuar? Sim ou Não?')
            if resp[0].upper() == 'N':
                break
        else:
            while True:
                emailPessoa = str(input('Digite o email da pessoa que deseja cadastrar: ')).replace(' ','').lower()
                if existeEmail(agenda,emailPessoa) == True:
                    print('Email já existênte, cadastre outro')
                else:
                    numCelular = str(input('Digite o número da pessoa que deseja cadastrar: '))
                    agenda[nomePessoa] = {
                        'telefone': numCelular,
                        'email': emailPessoa
                    }
                    break #O return é quem faz a interrupção de funções, break apenas interrompe o loop
            break #O break não sai de condicionais, apenas loops While e For que ele está inserido
    return f'{nomePessoa} Adicionada!'

def BuscarContato(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        return agenda[nomePessoa]
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
        # return não escreve nada em tela, apenas entrega total_vendedor a função. BuscarContato(agenda) = 'Essa pessoa não...'

def AttTelefone(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        novoTelefone = str(input(f'Digite o novo telefone de {nomePessoa}: '))
        agenda[nomePessoa]['telefone'] = novoTelefone
        return f'Telefone atualizado para {novoTelefone}!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def AttEmail(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        novoEmail = str(input(f'Digite o novo email de {nomePessoa}: '))
        agenda[nomePessoa]['email'] = novoEmail
        return f'Email atualizado para {novoEmail}!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def RemoverContato(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja remover: ')).title()
    if existeNome(agenda,nomePessoa):
        del agenda[nomePessoa]
        return f'{nomePessoa} Removido(a)!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def ListarContatos(agenda):
    print()
    for nome, dados in agenda.items(): #nome = key ; dados = value
        print(f'Nome: {nome}\n Telefone: {dados['telefone']}\n Email: {dados['email']}')
        print()

while True:
    print('1 - Adicionar contato')
    print('2 - Buscar contato')
    print('3 - Atualizar telefone')
    print('4 - Atualizar email')
    print('5 - Remover contato')
    print('6 - Listar contatos')
    print('0 - Sair') 
    opcao = int(input('Digite uma das opções acima: '))
    match opcao: 
        case 1:
            print(addContato(agenda))
        case 2:
            print(BuscarContato(agenda))
        case 3:
            print(AttTelefone(agenda))
        case 4:
            print(AttEmail(agenda))
        case 5:
            print(RemoverContato(agenda))
        case 6:
            ListarContatos(agenda)
        case 0:
            break

# =====================================================================
# Exercício 010: Agrupador de produtos por categoria.
# Você tem uma lista de tuplas e deve transformá-la em um dicionário agrupado por categoria.
    #Regras:
    # - Use dicionário vazio.
    # - Categoria deve ser a vendedor.
    # - Produtos da mesma categoria devem ir para uma lista.

    # Resultado esperado:
    #   {
    #       "periférico": ["mouse", "teclado"],
    #       "vídeo": ["monitor", "webcam"],
    #       "móvel": ["cadeira"]
    #   }
# =====================================================================


produtos = [
    ("mouse","periférico"),  #0   
    ("teclado","periférico"),#1
    ("monitor","vídeo"),     #2
    ("webcam","vídeo"),      #3
    ("cadeira","móvel")      #4
    ]

Categoria = {
    #'periférico': [ ],
    #'vídeo': [ ],
    #'...
}

for tipo in produtos:
    if tipo[1] not in Categoria: #caso não exista, então crie
        Categoria[tipo[1]] = []
    Categoria[tipo[1]].append(tipo[0])  # caso ja exista, não crie, e adicione produto a lista criada

print(Categoria)

# =====================================================================
# Exercício 011: Ranking de jogadores.
# Você recebe uma lista de jogadas. Crie um dicionário com a pontuação total
# de cada jogador e mostre quem fez mais pontos.
# Resultado esperado:
#   {
#       "Alice": 45,
#       "Bob": 55,
#       "Carlos": 50
#   }
# =====================================================================

jogadas = [
     ("Alice", 30),
     ("Bob", 20),
     ("Alice", 15),
     ("Carlos", 40),
     ("Bob", 35),
     ("Carlos", 10)
]

PontuacaoPessoa = {

}

for i in jogadas:
    if i[0] not in PontuacaoPessoa:
        PontuacaoPessoa[i[0]] = 0
    PontuacaoPessoa[i[0]] += i[1]

print(PontuacaoPessoa)



# =========================================================================
# Exercício 012: Carrinho de compras.
# Crie um carrinho como dicionário e calcule subtotal, total geral, produto
# mais caro e produto com maior quantidade.

    # Regras:
    #
    # - Calcule o subtotal de cada produto.
    # - Calcule o total geral.
    # - Mostre o produto mais caro no carrinho.
    # - Mostre o produto com maior quantidade.
    # - Produto mais caro considera preço unitário.
# =========================================================================

carrinho = {               
     "mouse": {"quantidade": 2, "precoUnit": 80.50},                      
     "teclado": {"quantidade": 1, "precoUnit": 150.99},
     "monitor": {"quantidade": 2, 'precoUnit': 240.49},
     "vídeo-game": {"quantidade": 1, 'precoUnit': 250.90}
}
totgeral = 0 
subtot = 0 
maiorSubTotal = {
    'nome': '',
    'subtot': 0
}

maiorQtd = {
    'nome': '',
    'qtd': 0
}

maiorPrecoUnitario = {
    'nome': '',
    'PrecoUnitario': 0
}

for produto, detalhes in carrinho.items(): #Produto = 'mouse' - Detalhe = quantidade: 2, precoUnit: 80.0                                          
    subtot = detalhes['quantidade'] * detalhes['precoUnit'] # acessamos os total_vendedores do dict interno pela vendedor interna 
    totgeral += subtot # a cada total de produto calculado já adicionamos ao calculo do total_vendedor final

    if subtot > maiorSubTotal['subtot']: #esses Ifs servem para verificar se algumas das caracteristas é superior as anteriores
        maiorSubTotal['nome'] = produto
        maiorSubTotal['subtot'] = subtot
    if detalhes['quantidade'] > maiorQtd['qtd']:
        maiorQtd['nome'] = produto
        maiorQtd['qtd'] = detalhes['quantidade']
    if detalhes['precoUnit'] > maiorPrecoUnitario['PrecoUnitario']:
        maiorPrecoUnitario['nome'] = produto
        maiorPrecoUnitario['PrecoUnitario'] = detalhes['precoUnit']
    #print do subtot
    print(f"PRODUTO: {produto} | QUANTIDADE: {detalhes['quantidade']} | PREÇO UNITÁRIO: {detalhes['precoUnit']} | SUBTOTAL: {subtot:.2f} ")

print('=============================')
print(f'TOTAL DO ESTOQUE: {totgeral:.2f}')  
print('=============================')
print(f'PRODUTO MAIS CARO (Q X P):\n | {maiorSubTotal["nome"]} | Subtotal: {maiorSubTotal["subtot"]} | ')
print('=============================')
print(f'PRODUTO COM MAIOR QUANTIDADE:\n | {maiorQtd["nome"]} | {maiorQtd["qtd"]} | ')
print('=============================')
print(f'PRODUTO COM MAIOR PREÇO UNITÁRIO:\n | {maiorPrecoUnitario["nome"]} | {maiorPrecoUnitario["PrecoUnitario"]} | ')
print('=============================')


# =====================================================================
# Exercício 013: Validador de registro obrigatório.
# Você recebe um cadastro e uma lista de campos obrigatórios. Verifique quais
# campos obrigatórios estão vazios ou ausentes.
# Resultado esperado:
# ["email"]

    # Regras:

    # - Campo ausente também é erro.
    # - String vazia conta como erro.
    # - Ao final, gere uma lista com os nomes dos campos inválidos.

# =====================================================================

cadastro = {
     "nome": "Ana Silva",
     "email": "",
     "idade": 22,
     "cidade": "Curitiba"
}

obrigatorios = ["nome", "email", "idade","sexo"]
invalidos = [ ]

for campo, dado in cadastro.items():
    if  (campo in obrigatorios) and (dado == ''):
        print(f'O campo {campo} é obrigatório! Respostas vazias não serão aceitas!!!')
        invalidos.append(campo) 
        
for i in obrigatorios:
    if i not in cadastro:
        invalidos.append(i)
        
print('O campos inválidos ou ausentes são: ')        
print(invalidos)

# =====================================================================
# Exercício 014: Resumo de vendas por vendedor.
# Você recebe uma lista de vendas. Gere um dicionário com o total vendido por
# vendedor e depois mostre o resumo das vendas.
# Resultado esperado:
#   {
#       "Ana": 550.0,
#       "Bruno": 250.0,
#       "Carlos": 400.0
#   }
# - Mostre o total geral vendido.
# - Mostre o vendedor com maior venda acumulada.
# - Mostre os vendedores que venderam acima de R$300.
# =====================================================================

vendas = [
     ("Ana", 250.0),
     ("Bruno", 100.0),
     ("Ana", 300.0),
     ("Carlos", 400.0),
     ("Bruno", 150.0)
 ]
relatorio_vendas = {
    #{
    #'Ana': 550.0, 
    #'Bruno': 250.0, 
    #'Carlos': 400.0
    #}
}

total_vendido = sum([item[1] for item in vendas])
# monta a lista e já passa pro sum() numa linha

for item in vendas:

    if item[0] not in relatorio_vendas:
        relatorio_vendas[item[0]] = 0
    relatorio_vendas[item[0]] += item[1]

vendasAcima300 = []
maiorVenda = 0
vendedorDoMes = ''

for vendedor,total_vendedor in relatorio_vendas.items():

    if total_vendedor > 300:
        vendasAcima300.append(vendedor)

    if total_vendedor > maiorVenda:
        maiorVenda = total_vendedor
        vendedorDoMes = vendedor

print(relatorio_vendas)
print(f'Total vendido: {total_vendido}')
print(f'Vendedor com maior total_vendedor total de vendas: {vendedorDoMes}')
print(f'Vendas acima de R$300 : {vendasAcima300}')


# =====================================================================
# Exercício 015: Mini relatório de logs com dicionário.
# Você recebe logs simples e deve criar um relatório usando dicionários.
# Resultado esperado aproximado:
#
#   contagem = {
#       "INFO": 2,
#       "ERRO": 2,
#       "AVISO": 1,
#       "DEBUG": 1
#   }
#
#   erros = [
#       "Falha na conexão",
#       "Timeout"
#   ]
#
# - Mostre a quantidade por tipo de log.
# - Mostre a lista de mensagens de erro.
# - Mostre os tipos de log encontrados.

# =====================================================================
logs = [
     "INFO - Servidor iniciado",
     "ERRO - Falha na conexão",
     "INFO - Usuário conectado",
     "AVISO - Memória alta",
     "ERRO - Timeout",
     "DEBUG - Variável carregada"
 ]

erros = []
contagemLogs = {

}

for registro in logs:
    tipo, mensagem =  registro.split(' - ')
    
    if tipo not in contagemLogs:
        contagemLogs[tipo] = 0
    contagemLogs[tipo] += 1

    if tipo == 'ERRO':
        erros.append(mensagem)

for c,v in contagemLogs.items():
    print(f'{c}: ',v)
print('==========')
print(erros)
