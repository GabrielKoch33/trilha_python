import sys
"""
=====================================================
EXERCÍCIOS - LIST COMPREHENSION E GENERATOR EXPRESSIONS
=====================================================

Regras:
- Não utilize respostas prontas.
- Prefira List Comprehension sempre que o exercício pedir.
- Nos exercícios sobre Generator Expression, evite converter para lista,
  exceto quando solicitado.
"""
lista = [1,25,4,30,5,68,7,87,9,11,22,23,45]

#List Comprehension usa: [ expressão for valor in lista ]
dobro = [x*2 for x in lista]
pares = [x for x in lista if x % 2 == 0] # filtra quais vão entrar
pares_impares = ["par" if x % 2 == 0 else "ímpar" for x in lista] #  classifica os valores de acordo com filtro
pares2impares3 = [ x*2 if x % 2 == 0 else x*3 for x in lista if x >= 30]
    # para cada elemento da lista, se x for maior ou igual a 30, veja se ele é par, se sim, dobre-o, senão, triplique-o

#Generator Expression usa: ( expressão for valor in lista) 
dobro = (x * 2 for x in lista)
maiores10 = (x for x in lista if x > 10)
pares_impares = ("Par" if x % 2 == 0 else "Ímpar" for x in lista)
    # semelhante a LC, porém, os resultados não vão direto para a memória, eles ficam armazenados em geradores que trabalham
    # com Lazy Evaluation, ou seja, só trazem os valores quando solicitados com next()

#Lambda usa: var = lambda arg : expressão
pares_impares = lambda x: "Par" if x % 2 == 0 else "Ímpar" 
grades = lambda x: ("A" if x >= 90 else "B" if x >= 70 else "C")

filtermaiores10 = filter(lambda x: x > 10, lista) #nesse caso filter (e map etc) armazem em um objeto gerador, semelhante a GENERATOR EXP.
print(pares_impares(10))
print(grades(10))

while True:
    continuar = input('continuar S/N: ')
    if continuar == 'S':
        print(next(filtermaiores10))
    else: 
       break

# =====================================================
# NÍVEL 1 - ENTENDENDO A SINTAXE
# =====================================================

# Exercício 1
# Dada a lista abaixo, gere outra lista contendo o dobro
# de todos os números.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobro = [n*2 for n in numeros]
       # ^       ^-- para cada valor na lista de numeros     
       # |-- retorne o valor * 2
print(dobro)
# Resultado esperado:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# -----------------------------------------------------
# Exercício 2
# Gere uma lista contendo apenas os números pares.

somente_pares = [num for num in numeros if num % 2 == 0]
print(somente_pares)

# Resultado esperado:
# [2, 4, 6, 8, 10]

# -----------------------------------------------------
# Exercício 3
# Gere uma lista contendo o quadrado apenas dos números ímpares.

quadrado_dos_impares = [ num*num for num in numeros if num % 2 == 1]
print(quadrado_dos_impares)
# Resultado esperado:
# [1, 9, 25, 49, 81]


# -----------------------------------------------------
# Exercício 4
# Transforme todos os nomes para letras maiúsculas.

nomes = ["Ana", "Carlos", "Maria", "Pedro"]
nomes_maiuscula = [nome.upper() for nome in nomes]
print(nomes_maiuscula)
# Resultado esperado:
# ["ANA", "CARLOS", "MARIA", "PEDRO"]

# =====================================================
# NÍVEL 2 - CONDIÇÕES
# =====================================================
# Exercício 5
# Transforme a lista abaixo
numeros = [4, -2, 8, -7, 0, 3]
# em:
["positivo", "negativo", "positivo","negativo", "zero", "positivo"]

lista_valores = ["positivo" if num > 0 else "negativo" if num < 0 else "zero" for num in numeros]
print(lista_valores)

# -----------------------------------------------------
# Exercício 6
# Retorne apenas as palavras com mais de quatro letras.

palavras = ["python", "java", "c", "javascript", "go"]
mais_de_4_letras = [p for p in palavras if len(p) > 4]
print(mais_de_4_letras)

# -----------------------------------------------------
# Exercício 7
# Transforme todas as palavras em letras minúsculas.

linguagens = ["Python", "JAVA", "Sql", "Docker"]
tudo_maiuscula = [p.upper() for p in linguagens]
print(tudo_maiuscula)

# Resultado esperado:
# ["python", "java", "sql", "docker"]

# =====================================================
# NÍVEL 3 - DICIONÁRIOS
# =====================================================
# Exercício 8
# Gere uma lista contendo apenas os nomes dos produtos
# cujo preço seja maior que R$300.
produtos = {
    "mouse": 150,
    "teclado": 250,
    "monitor": 1200,
    "webcam": 400
}
somente_nomes = [ produto for produto, preco in produtos.items() if preco > 300 ]
print(somente_nomes)

# -----------------------------------------------------
# Exercício 9
# Gere uma lista contendo apenas os preços.

somente_precos = [ preco for preco in produtos.values()]
print(somente_precos)

# Resultado esperado:
# [150, 250, 1200, 400]
# -----------------------------------------------------
# Exercício 10
# Gere uma lista contendo strings no formato:
#
# "mouse - R$150"
# "teclado - R$250"
# ...
produtos_formatados = [f'"{prod} - {preco}"' for prod, preco in produtos.items()]
print(produtos_formatados)

# =====================================================
# NÍVEL 4 - COMPREENSÕES ANINHADAS
# =====================================================
# Exercício 11
# Gere todos os pares possíveis entre letras e números.

letras = ["A", "B", "C"]
numeros = [1, 2, 3]

combinacoes = [(letra,num) for letra in letras for num in numeros]
print(combinacoes)
# Resultado esperado:
#
# ('A',1)
# ('A',2)
# ('A',3)
# ('B',1)
# ...
# -----------------------------------------------------
# Exercício 12
# Crie uma matriz 5x5 preenchida com zeros.

matriz_zero = [[0 for c in range(5)] for l in range(5)]
for linha in matriz_zero:
    print(linha)

# -----------------------------------------------------

# Exercício 13
# Crie uma matriz 4x4 onde cada posição seja:
# linha + coluna

# Resultado esperado:
# [
# [0,1,2,3],
# [1,2,3,4],
# [2,3,4,5],
# [3,4,5,6]
# ]
matriz4x4 = [[i+j for j in range(4)] for i in range(4)]
for linha in matriz4x4:
    print(linha)
'''
Mostrando a diferença entre usar LIST COMPREHENSION x FOR LOOPs normais.
A única desvantagem da LC é a legibilidade.
'''
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i+j)
    matriz.append(linha)
print(matriz)
# =====================================================
# NÍVEL 5 - GENERATOR EXPRESSIONS
# =====================================================
# Exercício 14
# Crie um generator que produza os quadrados dos números
# de 1 até 100.
#
# Não transforme em lista.
quadrados100 = ( i*i for i in range(1,101))
while quadrados100:
    try:
        print(next(quadrados100))
    except Exception as erro:
        print(f'GERADOR VAZIO {erro}')
        print('SAINDO DO GERADOR')
        break

# -----------------------------------------------------
# Exercício 15
# Consuma o generator anterior utilizando um for.
quadrados100 = ( i*i for i in range(1,101))
for i in range(1,101):
    print(next(quadrados100))


# -----------------------------------------------------
# Exercício 16
# Utilize um generator para calcular a soma dos quadrados
# de 1 até 100.
#
quadrados100 = ( i*i for i in range(1,101))

somaquad = (sum(x for x in quadrados100))
print(somaquad)

# -----------------------------------------------------
# Exercício 17
# Crie um generator contendo apenas os números pares
# de 1 até 1000.
# Imprima apenas os 10 primeiros usando next().

onlypares = (i for i in range(1,1001) if i % 2 == 0)
for i in range(10):
    print(next(onlypares))

# =====================================================
# NÍVEL 6 - COMPARAÇÕES
# =====================================================
# Exercício 18
# Faça duas implementações:
#
# 1) List Comprehension
# 2) Generator Expression
#
# Para gerar os quadrados dos números de 1 até 1.000.000.
# Depois compare:
# - type()
# - sys.getsizeof()
# - tempo de criação (opcional)

list_c = [i for i in range(1,1000000)]
gen_ex = (i for i in range(1,1000000))
print(type(list_c)) # class list 
print(type(gen_ex)) # class generator
print(sys.getsizeof(list_c)) # 8448728
print(sys.getsizeof(gen_ex)) # 200

# -----------------------------------------------------
# Exercício 19
# Considere:

clientes = [
    {"nome": "Ana", "idade": 20},
    {"nome": "Carlos", "idade": 15},
    {"nome": "Maria", "idade": 42},
    {"nome": "João", "idade": 18},
]
# Faça:
# a) Uma List Comprehension contendo apenas os nomes
#    dos maiores de idade.
# b) Um Generator Expression produzindo exatamente
#    o mesmo resultado.
lc_nomes_menores = [cliente['nome'] for cliente in clientes if cliente['idade'] >= 18 ]
genex_menor_nome = (cliente['nome'] for cliente in clientes if cliente['idade'] >= 18)
print(lc_nomes_menores)
while True:
    try:
        print(next(genex_menor_nome))
    except:
        break
# =====================================================
# CONSIDERAÇÕES FINAIS
# geradores:
# -> Permitem guardar valores infinitos sem necessidade de mandar para memória
# -> Consultamos apenas aquilo que queremos
# -> Bom para enorme quantidades de dados
# =====================================================

def gerador():
    for e in range(5):
        yield e
# yield nos permite transformar funções em genexp
# nesse caso o yield seria como um 'return'
# yield guarda os valores de 'e' em gerador() e mesmo se for interrompido, quando chamado dnv ele saberá de onde parou
for item in gerador():
    print(item) # 0,1,2,3,4


def fib_gen(n):
    a = b = 1
    for e in range(n):
        a, b = b, a + b
        yield a

for x in fib_gen(7):
    print(x) #1,2,3,5,8,13,21
