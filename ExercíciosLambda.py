# ===========================LIST COMPREHENSION=======================================
# Crie:
# uma lista apenas com IDs positivos
# uma lista com o dobro dos IDs positivos
# usando comprehension.
# =====================================================================

ids = [101, -5, 202, 0, 303, -10, 404]

ids_positivos = [ id for id in ids if id > 0] #criada uma lista com apenas > 0
print(ids_positivos)

ids_dobro = [ id * 2 for id in ids_positivos] # usa como base a lista criada anteriormente
print(ids_dobro)

# =====================================================================
# Crie uma nova lista contendo:
# nomes sem espaços
# todos em minúsculo
# =====================================================================

nomes = [" ana ", "Bruno", " CARLOS", "maria  "]

nomes_100_espacos = [ nome.lower().strip() for nome in nomes]
print(nomes_100_espacos)

# =====================================================================
# Crie:
# uma lista apenas com mensagens de erro
# outra lista contendo apenas o texto após "ERRO:"
# =====================================================================

logs = [
    "INFO: Servidor iniciado",
    "ERRO: Banco desconectado",
    "INFO: Usuário autenticado",
    "ERRO: Timeout"
]

erros = [linha for linha in logs if linha.split(':')[0] == 'ERRO']
mensagensErro = [msg.split(':')[1] for msg in erros]
print(erros)
print(mensagensErro)

# =====================================================================
# Crie um novo dicionário contendo apenas produtos com estoque maior que zero.
# =====================================================================

estoque = {
    "mouse": 10,
    "teclado": 0,
    "monitor": 3,
    "webcam": 0
}

estoque_non_zerado = {produto: qtd  for produto, qtd in estoque.items() if qtd > 0}
print(estoque_non_zerado)

# =====================================================================
# Crie um set contendo emails únicos em minúsculo.
# =====================================================================
emails = [
    "ANA@EMAIL.COM",
    "bruno@email.com",
    "ana@email.com",
    "CARLOS@email.com"
]

email_unique = {email.lower() for email in emails }
print(email_unique)
# =====================================================================
# Transforme em:
# [1, 2, 3, 4, 5, 6, 7, 8]
# =====================================================================
matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

matriz_em_linha = [num for linha in matriz for num in linha]
print(matriz_em_linha)

# ===================================LAMBDA============================
# Ordene os nomes pelo tamanho.
# =====================================================================
nomes = ["Ana", "Fernanda", "João", "Gabriel"]

nomes_crescentes = sorted(nomes, key=lambda n:len(n))

print(nomes_crescentes)

# =====================================================================
# Exercício 09 — Ordenar produtos por preço
# =====================================================================


produtos = [
    ("mouse", 80),
    ("monitor", 900),
    ("teclado", 150)
]

# key= use ESSE crtério para ordenar (no caso cada valor/indice dessa lista pela posição 1 da tupla)
cheaper = sorted(produtos,key=lambda valor: valor[1])
print(cheaper)

'''
pyhton pega o mouse/80 e aloca em cheaper -->
python pega monitor/900 e aloca depois de mouse, afinal o preço é maior -->
python pega teclado/150 e aloca entre ambos pq mouse < teclado < monitor
'''
# =====================================================================
# Exercício 10 — Ordenar usuários por idade
# =====================================================================

usuarios = [
    {"nome": "Ana", 
     "idade": 20},

    {"nome": "Carlos", 
     "idade": 17},

    {"nome": "Bruno", 
     "idade": 30}
]

# Ordene pela idade usando lambda.

idades = sorted(usuarios, key=lambda chave: chave['idade']) #para cada linha de usuários, analise e ordene a campo chave de idade
print(idades)

# =====================================================================
# Exercício 11 — Maior venda
# =====================================================================

vendas = [
    ("Ana", 300),
    ("Bruno", 1000),
    ("Carlos", 450)
]

# Use max() + lambda para encontrar a maior venda.

maior_venda = max(vendas,key=lambda linha: linha[1])
print(f' Para cada linha de vendas, faça: encontre o MAIOR valor de todos com base no dado na posição [1]: {maior_venda}')

# =====================================================================
# Exercício 12 — Menor estoque
# =====================================================================

estoque = {
    "mouse": 10,
    "teclado": 2,
    "monitor": 5
}

# Use min() + lambda para descobrir o produto com menor estoque.
menor_estoque = min(estoque, key= lambda linha: linha[1])
print(menor_estoque)

# =====================================================================
# Exercício 13 — Filtrar números pares
# =====================================================================

numeros = [1,2,3,4,5,6,7,8,9,10]

only_pares = list(filter(lambda num: num % 2 == 0,numeros)) # filter(função, iteravel) /// melhor usar list comprehension [ x for x in numeros if x % 2 == 0]
'''
--> a própria função já retorna True ou False, sendo ela lambda ou não, ai já serve como If Conditional do Filter
'''
print(only_pares)
# Use filter() + lambda para gerar apenas os pares.
# Converta o resultado para lista.


# =====================================================================
# Exercício 14 
# Use filter() para retornar apenas os produtos que estão em estoque (estoque > 0).
# Use map() para gerar uma nova lista contendo apenas os nomes dos produtos em estoque (pode usar o resultado da tarefa 1).
# Use sorted() para ordenar a lista original de produtos pelo preço, do menor para o maior.
# Use map() para gerar uma lista com os preços com 10% de desconto aplicado em todos os produtos.
# =====================================================================

produtos = [
    {"nome": "Notebook",   "preco": 3500, "estoque": 0},
    {"nome": "Mouse",      "preco": 150,  "estoque": 5},
    {"nome": "Teclado",    "preco": 280,  "estoque": 0},
    {"nome": "Monitor",    "preco": 1200, "estoque": 3},
    {"nome": "Headset",    "preco": 400,  "estoque": 8},
]

em_estoque = list(filter(lambda prod: prod['estoque'] > 0 ,produtos))
'''
-> usamos list() para converter a função filter, pois ela guarda os valores em um gerador, o qual faz lazy evaluation
-> Na lista produtos, prod indicará o indice atual da lista e,
verifique se no item atual, no campo estoque haja valores > 0'''
print(em_estoque)

nomes_em_estoque = list(map(lambda prod: prod['nome'] ,em_estoque))
print(nomes_em_estoque)

valores = sorted(produtos, key=lambda prod : prod['preco'])
print(valores)

desconto10 = list(map(lambda prod: f' produto: {prod['nome']}, preço: {prod['preco'] * 0.9}',produtos))
print(desconto10)

# =====================================================================
# Exercício 1 — Turma de alunos
# =====================================================================

alunos = [
    {"nome": "Ana",     "notas": [8.0, 7.5, 9.0], "serie": "A"},
    {"nome": "Bruno",   "notas": [4.0, 5.0, 3.5], "serie": "B"},
    {"nome": "Carol",   "notas": [6.0, 7.0, 8.5], "serie": "A"},
    {"nome": "Diego",   "notas": [9.5, 9.0, 10.0],"serie": "B"},
    {"nome": "Elena",   "notas": [4.5, 4.0, 5.5], "serie": "A"},
    {"nome": "Felipe",  "notas": [7.0, 8.0, 6.5], "serie": "B"},
]

media_aluno = [
    f'Nome: {dado['nome']}, Media: {sum(dado['notas'])/len(dado["notas"]):.2f}' 
    for dado in alunos]

print(media_aluno)



# =====================================================================
# BLOCO 3 — GENERATOR EXPRESSIONS

li = [1,2,4,3,5,6,8,0,7]

pares = filter(lambda n: n % 2 == 0, li)
while True:
    try:
        num = next(pares)
        print(num)
    except StopIteration:
        break
'''
Funções como filter funcionam semelhantes a um generator, eles fazem suas operações e guardam em obejto de tipo iteravel
Nesses casos, os valores não são armazenados na memória, de uma vez só, ao invés disso, eles são liberados via Lazy Evaluation.
Ou seja, só vão ser exibidos se usarmos next e percorremos um por um, por isso muitas vezes usamos list()
De forma a converter em uma estrutura mais manipulavel e iteravel.
'''
# =====================================================================
# Exercício 15 — Soma total
# =====================================================================
# Dataset:
vendas = [100, 200, 300, 400]
# Use generator expression dentro de sum() para calcular o total.
# SEM criar lista intermediária.

total_vendas = (sum(x for x in vendas))

# =====================================================================
# Exercício 16 — Quantidade de erros
# =====================================================================
# Dataset:
logs = [
     "INFO",
     "ERRO",
     "INFO",
     "ERRO",
     "ERRO"
]
# Use generator expression para contar quantos "ERRO" existem.

contador_erros = ()
# Exercício 17 — Existe produto caro?

# Dataset:

# precos = [100, 200, 1500, 300]

# Use any() + generator expression para verificar se existe produto acima de 1000.

# Exercício 18 — Todos usuários são maiores?

# Dataset:

# idades = [20, 18, 30, 15]

# Use all() + generator expression para verificar se todos são maiores de idade.

# Exercício 19 — Total do carrinho

# Dataset:

# carrinho = [
#     {"produto": "mouse", "quantidade": 2, "preco": 80},
#     {"produto": "monitor", "quantidade": 1, "preco": 900},
#     {"produto": "teclado", "quantidade": 3, "preco": 150}
# ]

# Calcule o valor total usando generator expression.

# Exercício 20 — Palavras longas

# Dataset:

# palavras = ["python", "sql", "dados", "etl", "engenharia"]

# Use generator expression + list() para gerar apenas palavras com mais de 5 letras.

# Exercício 21 — Pipeline realista (mais difícil)

# Dataset:

# usuarios = [
#     {"nome": "Ana", "ativo": True, "idade": 20},
#     {"nome": "Bruno", "ativo": False, "idade": 30},
#     {"nome": "Carlos", "ativo": True, "idade": 17},
#     {"nome": "Fernanda", "ativo": True, "idade": 40}
# ]

# Faça:

# Gere uma lista apenas com usuários ativos.
# Gere uma lista apenas com nomes dos ativos.
# Gere um generator expression para contar quantos ativos são maiores de idade.
# Descubra o usuário mais velho usando max() + lambda.
# Gere um set com nomes em minúsculo.