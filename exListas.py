# O range(len()) é inclusivo no inicío e exclusiva no final, ou seja:
# for i in range(len(frutas)): sendo frutas len()=3; o range vai de 0 a 2

# =====================================================================
# Dada uma lista de números: Retorne quantos são maiores que a média
# =====================================================================
lista = []
tam = int(input('Digite o Tamanho da lista: '))
for i in range(tam):
    lista.append(int(input(f'digite o {i}º valor: ')))

sum = 0
for i in range(len(lista)):
    sum += lista[i]
media = sum / tam

print(f'A soma de todos os valores são {sum} e a média {media}')
cont = 0

for i in range(tam):
    if lista[i] > media:
        print(f'Valor acima da média: {lista[i]}')
        cont += 1
print(f'Existem {cont} Valores acima da média')

# =====================================================================
# Leia 10 números em uma lista e mostre: Vetor original & Vetor invertido (Sem Métodos)
# =====================================================================

num = []
for i in range(4):# = 0,1,2,3 = 4 espaços
    valor = int(input(f'Digite o {i+1}º Números: '))
    num.append(valor)

num_inv =[]
for i in range(3,-1,-1): # num = [{0}{1}{2}{3]}; -1 porque se fosse 0 ele iria apenas até o 1 (inicio,fim-1)
    num_inv.append(num[i])

print(num)
print(num_inv)


# =====================================================================
# Dada a lista: lista2 = [1,2,3,4,5]: Peça um valor e remova todas as ocorrências dele manualmente (sem usar remove())
# =====================================================================

lista2 = [1,2,3,4,5]

escolhido = int(input('Escolha um numero a ser removido: '))
for i in range(len(lista2)):
    if escolhido == lista2[i]:
        for j in range(i,len(lista2)- 1):
            lista2[j] = lista2[j+1]
        lista2.pop()#remove o último valor da lista, evitando que haja valor duplicado
        break

print(f'{escolhido}REMOVIDO!')
print(lista2)

# =====================================================================
# Peça um número ao usuário e: Retorne a posição dele ou '-1' se não existir
# =====================================================================

lista1 = [5,8,2,9,1]
achou = 0
posicao = 0

numero = int(input('digite um numero, vamos ver se ele está na lista!: '))

for i in range(len(lista1)):
    if numero == lista1[i]:
        posicao = i
        print(f'O valor está na posição {posicao}')

if numero not in lista1:
    achou -= 1
    print(achou)

# =====================================================================
# Leia uma lista de números inteiros informada pelo usuário. 
# Em seguida, crie uma segunda lista contendo apenas os valores únicos da lista original, sem repetição.
# Ao final, ordene essa nova lista em ordem crescente e exiba o resultado.
# =====================================================================

lista = []
nova = []
tam = int(input('Digite o tamanho da lista: '))

for i in range(tam):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

def nova_lista(lista, novo):
    for i in lista:
        if i not in novo:
            novo.append(i)

    for k in range(len(novo)):  # bubble sort
        for l in range(len(novo)- k - 1):
            if novo[l] > novo[l + 1]:
                novo[l], novo[l+1] = novo[l+1], novo[l] 
    return novo

nova_lista(lista, nova)
print(nova)

#=====================================================================
# 01) Dada uma lista de números, crie uma lista com o dobro de cada número usando list comprehension.
#=====================================================================

numeros = [2, 4, 6, 8]
numeros_dobro = [n*2 for n in numeros]
print(numeros_dobro)

#=====================================================================
# 02) Dada uma lista de nomes, crie uma lista apenas com nomes que tenham mais de 5 letras.
#=====================================================================

nomes = ["Ana", "Gabriel", "João", "Fernanda"]

nomes_com_5letras = [nome for nome in nomes if len(nome) > 5]

print(nomes_com_5letras)

#=====================================================================
# 03) Dado um dicionário de preços, crie outro dicionário com 10% de desconto.
#=====================================================================

precos = {
    "mouse": 80.0,
    "teclado": 150.0,
    "monitor": 900.0
}

precos_desconto10 = { item: preco-preco*0.1 for item, preco in precos.items()}

print(precos_desconto10)

#=====================================================================
# 04) Dada uma lista de emails com repetição, gere um set com emails em minúsculo.
#=====================================================================

emails = ["ANA@EMAIL.COM", "ana@email.com", "BRUNO@EMAIL.COM"]

unique_emails = {email.lower() for email in emails}
print(unique_emails)
