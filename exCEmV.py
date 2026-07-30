# =====================================================================
# Exercício 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
# correto.
# =====================================================================
while True:
    sexo = input('Digite seu sexo [M] ou [F]: ')
    if sexo not in 'MmFf':
        print('Resposta Inválida, tente novamente')
    else:
        break
if sexo == 'M'or sexo == 'm':
    print('Você é homem')
else:
    print('Você é mulher')

# =====================================================================
# Exercício 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
# =====================================================================
# import random
# computador = random.randint(1,10)

# while True:
#     palpite = int(input('Qual número você acha que o computador pensou? R: '))
#     if palpite == computador:
#         print('Parabéns')
#         break
#     else:
#         print('Tente novamente')

# =====================================================================
# Exercício 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# =====================================================================
n = int(input('numero que será fatorado: '))
f = 1 
i = 2
while i <= n:
    f = f * i
    i += 1
print(f'O fatorial de {n} é {f}')


# =====================================================================
# Exercício 063: Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci.
# =====================================================================
tam = int(input('tamanho da seq de fibonaci '))
sequencia = [0,1]

while True:
    for e in range(2,tam):
        sequencia.append(sequencia[e-1] + sequencia[e-2]) 
    print(sequencia)
    op = input('Deseja continuar? S ou N ')
    if op in 'Nn':
        break
    elif op in 'Ss':
        tam = int(input('Novo tamanho para a seq de fibonaci '))
    else:
        print('Invalida, tente dnv') 

# =====================================================================
# Exercício 064: Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).
# =====================================================================

# =====================================================================
# Exercício 065: Crie um programa que leia vários números inteiros pelo teclado. No
# final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores.
# =====================================================================

# =====================================================================
# Exercício 066: Crie um programa que leia números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o
# flag).
# =====================================================================

# =====================================================================
# Exercício 067: Faça um programa que mostre a tabuada de vários números, um de cada
# vez, para cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.
# =====================================================================

# =====================================================================
# Exercício 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só
# será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
# =====================================================================

# =====================================================================
# Exercício 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:
# =====================================================================

# =====================================================================
# Exercício 070: Crie um programa que leia o nome e o preço de vários produtos. O
# programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# =====================================================================

# =====================================================================
# Exercício 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
# =====================================================================

# =====================================================================
# Exercício 072: Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por extenso.
# =====================================================================

# =====================================================================
# Exercício 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# =====================================================================

# =====================================================================
# Exercício 074: Crie um programa que vai gerar cinco números aleatórios e colocar em
# uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla.
# =====================================================================

# =====================================================================
# Exercício 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# =====================================================================

# =====================================================================
# Exercício 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.
# =====================================================================

# =====================================================================
# Exercício 077: Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas
# vogais.
# =====================================================================

# =====================================================================
# Exercício 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.
# =====================================================================

# =====================================================================
# Exercício 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.
# =====================================================================

# =====================================================================
# Exercício 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No
# final, mostre a lista ordenada na tela.
# =====================================================================

# =====================================================================
# Exercício 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# =====================================================================

# =====================================================================
# Exercício 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
# =====================================================================

# =====================================================================
# Exercício 083: Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.
# =====================================================================

# =====================================================================
# Exercício 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# 1- Quantas pessoas foram cadastradas
# 2- Lista de mais pesadas
# 3- Lista de mais leves
# =====================================================================

pessoas = []
pesadas = []
leves = []
cadastro = []

while True:
    pessoas.clear() # evita que o registro do loop anterior permaneca 
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cadastro.append(pessoas[:]) # copia dados para outra lista
    op = str(input('Deseja continuar? [S/N]?'))
    if op in 'Nn':
        break
        
for c in cadastro: # / = float ; // = int
    if c[1] >= 80.0:
        pesadas.append(c)
    elif c[1] <= 40.0:
        leves.append(c)

print(f'A quantidade de pessoas cadastradas foi: {len(cadastro)}\n Pessoas Leves {leves}; Pesadas: {pesadas}')

# =====================================================================
# Exercício 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No
# final, mostre os valores pares e ímpares em ordem crescente.
# =====================================================================

# =====================================================================
# Exercício 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação
# correta.
# =====================================================================
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
      elemento = int(input(f'valor na posição [{i+1},{j+1}] = '))
      linha.append(elemento)
    matriz.append(linha)
                                    # matriz = [1,2,3]
for i in range(3):                  #          [4,5,6]
    print(f'{matriz[i]}')           #          [7,8,9] 
        
# =====================================================================
# Exercício 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e
# 60 para cada jogo, cadastrando tudo em uma lista composta.
# =====================================================================
import random
qtd = int(input('Quantos jogos serão comprados? '))

jogosLista = []
for i in range(qtd):
    numSorteados = []
    for j in range(1):
        e = random.sample(range(1,100),6) # e recebe uma lista de 6 valores
        numSorteados.append(e) # = [[1,2,3,4,5,6]]
    jogosLista.append(numSorteados)

print(f'Você comprou {qtd} jogos!\nAqui estão seus números sorteados:')
for i in range(qtd):
    print(f'{i+1}º Jogo: {jogosLista[i]}')

# jogosLista = [[],[],[]]
# Cada [] interno é definido por qtd
# j = 1 permite que dentro de cada i seja armazado uma lista de 6 numeros

# =====================================================================
# Exercício 089: Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
# =====================================================================
boletim = []
nomeAluno = []
notasAluno = []
while True:
    nome = input('Digite o nome do aluno')
    nomeAluno.append([nome]) # Guarda o nome como uma lista dentro de nome aluno = nomeALUNO[['Ana'],['Júlio']]
    op = str(input('Continuar? S/N'))
    if op in 'Nn':
        break

print(nomeAluno) # [[a1,[notas]],[a2,[notas]],[a3,[notas]]]

for posi, aluno in enumerate(nomeAluno):
    notasAluno = [] # Reseta a lista de notas a cada novo aluno
    for notas in range(2):
        elemento = float(input(f'{notas+1} ª nota de {aluno} = '))
        notasAluno.append(elemento)
    nomeAluno[posi].append(notasAluno[:]) # Aluno recebe uma cópia : de suas notas, para quando resetar as Notas não alterar dentro de nome

boletim = nomeAluno

for aluno in boletim:
    print(aluno)

# =====================================================================
# Exercício 090: Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# =====================================================================

# =====================================================================
# Exercício 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# =====================================================================

# =====================================================================
# Exercício 092: Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# =====================================================================

# =====================================================================
# Exercício 093: Crie um programa que gerencie o aproveitamento de um jogador de
# futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.
# =====================================================================

# =====================================================================
# Exercício 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# =====================================================================

# =====================================================================
# Exercício 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# =====================================================================

# =====================================================================
# Exercício 096: Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# =====================================================================

# =====================================================================
# Exercício 097: Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# =====================================================================

# =====================================================================
# Exercício 098: Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
# através da função criada:
# =====================================================================

# =====================================================================
# Exercício 099: Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.
# =====================================================================

# =====================================================================
# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.
# =====================================================================

# =====================================================================
# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# =====================================================================

# =====================================================================
# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será
# um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.
# =====================================================================

# =====================================================================
# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa
# deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
# informado corretamente.
# =====================================================================

# =====================================================================
# Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de
# forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar
# apenas um valor numérico.
# =====================================================================

# =====================================================================
# Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# =====================================================================

# =====================================================================
# Exercício 106: Faça um mini-sistema que utilize o Interactive Help do Python. O
# usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
# palavra 'FIM', o programa se encerrará. Importante: use cores.
# =====================================================================

# =====================================================================
# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse
# módulo e use algumas dessas funções.
# =====================================================================

# =====================================================================
# Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada
# moeda() que consiga mostrar os números como um valor monetário formatado.
# =====================================================================

# =====================================================================
# Exercício 109: Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.
# =====================================================================

# =====================================================================
# Exercício 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já
# temos no módulo criado até aqui.
# =====================================================================

# =====================================================================
# Exercício 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
# chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e
# 109 para o primeiro pacote e mantenha tudo funcionando.
# =====================================================================

# =====================================================================
# Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
# módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que seja monetários.
# =====================================================================

# =====================================================================
# Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.
# =====================================================================

# =====================================================================
# Exercício 114: Crie um código em que teste se o site pudim está acessível pelo
# computador usado.
# =====================================================================
