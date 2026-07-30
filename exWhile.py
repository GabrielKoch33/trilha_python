# =====================================================================
# Exemplo While True para Loops Infinitos
# =====================================================================

while True: #Enquanto True for verdadeiro faça: (True sempre será verdadeiro, logo executa o código até ler um BREAK)
    
    resposta = input("Digite sair para encerrar: ")

    if resposta == "sair": #Se essa condição for atendida 
        break   # Então o programa é encerrado

    print("Você digitou:", resposta) # Se não for atendida, printa essa mensagem e volta ao início

    
print("Programa encerrado.") # Caso o IF for atendido, o programa sai do Loop While e exibe essa mensagem

# While funciona de forma que: enquanto a condição for verdadeira o laço se repete
# While True cria um loop infinito porque True é sempre verdade
# While False cria um loop que nunca vai ser executado, pois, False nunca será verdadeiro, logo o bloco do while false é ignorado


# =====================================================================
# Exercício 001: Crie um programa que leia vários números inteiros usando while.
# O programa deve parar apenas quando o usuário digitar 0. No final, mostre quantos
# números foram digitados, a soma total e a média entre eles, desconsiderando o 0.
# =====================================================================
contador = 0
media = 0
soma = 0
while True:
    num = int(input('DIGITE UM NUM, SE FOR 0 VC SAI: '))
    if num == 0:
        break
    else:
        contador += 1   
        soma += num
print(f'A quatidade de números inseridos: {contador}\nA soma total: {soma}\n A média {soma/contador}')

# =====================================================================
# Exercício 003: Crie um programa que leia nomes de produtos e seus preços usando
# while True. O cadastro deve parar quando o usuário responder "N" para continuar. No
# final, mostre o total gasto e quantos produtos custaram mais de R$1000.00.
# =====================================================================
cadastroProdutos = {

}
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input(f'Digite o preço do {produto}'))
    cadastroProdutos[produto] = preco
    sair = str(input('Deseja sair? [Y/N]')).upper()
    if sair == 'Y':
        break

print(cadastroProdutos)

# =====================================================================
# Exercício 010: Faça um programa que leia uma frase e conte, usando while, quantas
# vogais existem nela. Ignore diferenças entre letras maiúsculas e minúsculas.
# =====================================================================

frase = input('Digite a frase: ').replace(' ','').lower()
letra = 0
while letra < len(frase):
    if frase[letra] in 'aeiou':
        countVogais += 1

    letra += 1


# =====================================================================
# Exercício 014: Faça um programa que leia vários nomes e pesos, guardando os dados em
# uma lista composta. O cadastro deve continuar enquanto o usuário quiser. No final,
# mostre quantas pessoas foram cadastradas, a pessoa mais pesada e a pessoa mais leve.
# =====================================================================

pessoas = []
contpessoas = 0

    # if peso > maisPesada:
    #     maisPesada = peso
    #     nomeMaisPesada = nome
    
while True:
    nome = input('nome: ')
    peso = float(input('peso: '))
    contpessoas += 1
    pessoas.append([nome,peso])# ja guarda nome e peso como lista dentro de outra lista
    
    sair = str(input('Deseja sair? [Y/N]')).upper()
    if sair == 'Y':
        break

maisPesada = pessoas[0]                                                                #   0       1      2
maisLeve = pessoas [0] # Fora de um loop uma unica chave [] significa a posição inteira[[a0 b1],[c1 d2],[e0 f1]]

for item in pessoas[1:]: # começa no indice 1 até o fim
    if item[1] > maisPesada: #Se usasse um else ele iria considerar <=
        maisPesada = item #maispesada guarda [nome][peso]
    elif item[1] < maisLeve:
        maisLeve = item

print(f'mais pesada: {maisPesada[0]} ({maisPesada[1]}kg)')
print(f'mais leve:   {maisLeve[0]} ({maisLeve[1]}kg)')
print(pessoas)

# =====================================================================
# Exercício 015: Crie um programa que controle uma lista de tarefas. O usuário pode
# adicionar tarefa, marcar tarefa como concluída, listar tarefas pendentes, listar
# tarefas concluídas ou sair. Use while para manter o menu funcionando.
# =====================================================================

def adicionartarefa(toDoList):
    tarefa = input('Digite o nome da tarefa').title()
    tarefa = formatatexto(tarefa)

    if jaexiste(toDoList,tarefa):
        return('Tarefa Já Existênte')
    else:
        toDoList[tarefa] = 'PENDENTE'
        return f'{tarefa} Foi marcada como Pendente!'

def tarefaconcluida(toDoList):
    tarefa = tarefa = input('Digite o nome da tarefa').title()
    tarefa = formatatexto(tarefa)
    if jaexiste(toDoList,tarefa) == False:
        return('Tarefa Não Existe')
    else:
        toDoList[tarefa] = 'CONCLUÍDO'
        return f'{tarefa} Foi marcada como Concluída!'
    
def listarpendentes(toDoList): 

    for task, status in toDoList.items():
        if status == 'PENDENTE':
            print(f'{task}: {status}')

    
def listarconcluidas(toDoList): 
    
    for task, status in toDoList.items():
        if status == 'CONCLUÍDO':
            print(f'{task}: {status}')

def jaexiste(toDoList,tarefa):
    if tarefa in toDoList:
        return True
    else:
        return False

def formatatexto(tarefa):
    trata_texto = tarefa.split()
    for palavra in trata_texto:
        if len(palavra) <= 2:
            palavra = palavra.lower()
    
    tarefa = ' '.join(trata_texto)
    return tarefa

toDoList = {

}

op = ''
while op != '0':
    print('1 - Adicionar tarefa')
    print('2 - Marcar tarefa como concluída')
    print('3 - Listar tarefas pendentes')
    print('4 - Listar tarefas concluídas')
    print('0 - Sair')
    op = input('Escolha uma opção: ')
    if op == '1':
        r1 = adicionartarefa(toDoList)
        print(r1)
    elif op == '2': 
        r1 = tarefaconcluida(toDoList)
        print(r1)
    elif op == '3':
        listarpendentes(toDoList)
    elif op == '4':
        listarconcluidas(toDoList)
    elif op == '0':
       break 
        


# =====================================================================
# Exercício 016: Validador de senha com tentativas limitadas
# Crie um programa que peça uma senha até ela ser considerada válida ou até
# o usuário errar 5 vezes.
#
# Critérios da senha:
# - mínimo 8 caracteres
# - pelo menos 1 número
# - pelo menos 1 letra maiúscula
# - pelo menos 1 caractere especial entre @, #, $, %, &, !
#
# Ao final, informe se o cadastro foi aceito ou bloqueado por excesso de
# tentativas.
#
# Obrigatório:
# [ ] usar while
# [ ] contar tentativas
# [ ] não aceitar senha inválida
# [ ] mostrar o motivo da invalidação
# =====================================================================

print(' BEM VINDO AO SISTEMA! INSIRA SUA SENHA PARA LOGAR: ')
numTentativas = 0
contadorRequisitos = 0

while numTentativas < 5:

    contadorRequisitos = 0  # A cada break do while interno, o contador reinicia para evitar guardar a pontuação no loop anterior
    senha = str(input('Digite sua senha: ')).strip()
    numTentativas += 1      # A cada break do while interno, o numtentativas aumenta
    
         
    while True:
        
        if len(senha) >= 8:
            contadorRequisitos += 1
        else:
            print('erro tam')
            break
        
        temNumero = False
        for c in senha:
            if c in '0123456789':
                temNumero = True
                break
            
        if temNumero:
            contadorRequisitos += 1
        else:
            print('erro num')
            break
        
        contaMaiuscula = 0 
        for letra in senha:
            if letra.isupper():
                contaMaiuscula = 1
                break

        if contaMaiuscula == 1:
            contadorRequisitos += 1
        else:
            print('erro maius')
            break

        temEspecial = False
        for c in senha:
            if c in '@#$%&!':         
                temEspecial = True
                break
            
        if temEspecial:
            contadorRequisitos += 1
        else:
            print('erro espec')
            break

        break # Esse break, que sai do while True, só é executado quando o contadorRequisitos == 4

    if contadorRequisitos == 4: # Logo, se o break de cima ocorreu, então esse print aparece.
        print('Senha válida — login bem sucedido!')
        break # Esse break sai do loop externos (das tentativas)

if contadorRequisitos < 4 and numTentativas == 5: # Quando o numTentativas == 5 então o while externo quebra e roda esse bloco
    print('Número máximo de tentativas atingido.')
   # só executa esse bloco se as duas forem true, como o contador de requisitos vai ser == 4 então ele não roda esse bloco


# =====================================================================
# Exercício 017: Caixa eletrônico com saque controlado
# O usuário começa com saldo de R$ 1000. O programa deve exibir um menu
# enquanto ele não escolher sair:
#
# 1 - Ver saldo
# 2 - Sacar
# 3 - Depositar
# 0 - Sair
#
# Regras:
# - não permitir saque maior que o saldo
# - não permitir valores negativos ou zero
# - contar quantas operações foram feitas
# - mostrar saldo final ao sair

# =====================================================================
operacoes = {

}

def versaldo(saldo):
    if 'Ver Saldo' not in operacoes:
        operacoes['Ver Saldo'] = 0
    operacoes['Ver Saldo'] += 1
    print(f'R${saldo}') 
     

def sacar(saldo):
    print(f'Seu saldo atual R${saldo}')
    if 'Saque' not in operacoes:
        operacoes['Saque'] = {'Total': 0, 'Saque Inválido': 0, 'Saque Válido': 0}

    valorSaque = float(input('Quanto que você deseja sacar?'))

    if valorSaque > saldo:
        operacoes['Saque']['Total'] += 1
        operacoes['Saque']['Saque Inválido'] += 1
        print('impossível sacar valor maior que o saldo')
        return saldo
    
    else:
        operacoes['Saque']['Total'] += 1
        operacoes['Saque']['Saque Válido'] += 1
        return saldo - valorSaque
    
def depositar(saldo):
    print(f'Seu saldo atual R${saldo}')
    if 'Depositar' not in operacoes:
        operacoes['Despositar'] = 0
    operacoes['Despositar'] += 1
    valorDeposito = float(input('Digite o valor que deseja depositar: '))
    
    return saldo + valorDeposito


saldo = 1000
op = ''

while op != '0':  
    print('1 - Ver saldo')
    print('2 - Sacar')
    print('3 - Depositar')
    print('4 - Relatório')
    print('0 - Sair')
    op = input('Qual operação deseja fazer? ')
    if op == '1':
        versaldo(saldo)
    if op == '2':
       saldo = sacar(saldo)
    if op == '3':
       saldo = depositar(saldo)
    if op == '4':
        for atividade,quantidade in operacoes.items():
            print(f'{atividade}: {quantidade}')
    if op == '0':
        print('Saindo...')
        break

# =====================================================================
# Exercício 019: Jogo de adivinhação com dificuldade
# Crie um jogo em que o programa sorteia um número secreto.
#
# O usuário escolhe a dificuldade:
# 1 - Fácil: 10 tentativas, número de 1 a 50
# 2 - Médio: 7 tentativas, número de 1 a 100
# 3 - Difícil: 5 tentativas, número de 1 a 200
#
# A cada tentativa, informe se o chute foi maior ou menor que o número secreto.
#
# Obrigatório:
# [ ] usar random.randint()
# [ ] controlar tentativas com while
# [ ] validar chute fora do intervalo
# [ ] encerrar ao acertar ou ao acabar tentativas
# =====================================================================


import random

numMin = 1
opcao = ''

while opcao != '0':
    print('1 - Fácil: 10 tentativas, número de 1 a 50')
    print('2 - Médio: 7 tentativas, número de 1 a 100')
    print('3 - Difícil: 5 tentativas, número de 1 a 200')
    print('4 - Sair')

    opcao = input('>Digite a opção referente a dificuldade escolhida: ')
    if opcao == '1':
        tentativas = 10
        numMax = 50
        numAletorio = random.randint(1,numMax)
    elif opcao == '2':
        tentativas = 7
        numMax = 100 
        numAletorio = random.randint(1,numMax)
    elif opcao == '3': 
        tentativas = 5
        numMax = 200
        numAletorio = random.randint(1,numMax)
    elif opcao == '4':
        print('Saindo...')
        break 

    i = 1
    while i <= tentativas:
        print(f'{i}ª Tentativa!')
    
        while True:
            chute = int(input('>Qual é o seu chute?: '))
            if chute > numMax:
                print('Valor alto demais, tente denovo!')
            else:
                break

        if chute > numAletorio:
            print(f'Chute alto, o número é MENOR que {chute}')
            i += 1

        elif chute < numAletorio:
            print(f'Chute baixo, o número é MAIOR que {chute}')
            i += 1

        else:
            print(f'Acertou!!! O nº era {numAletorio} e você chutou {chute}!')
            break

    resposta = input('Deseja jogar denovo?: [y][n]')
    if resposta[0].upper( ) == 'N':
        break 

# =====================================================================
# Exercício 022: Simulador de login
# Você tem usuários válidos em duas listas paralelas:

# Peça usuário e senha até o login ser válido ou até atingir 3 tentativas.
#
# Regras:
# - se usuário não existir, informar usuário inválido
# - se usuário existir mas senha estiver errada, informar senha inválida
# - se acertar, mostrar mensagem de boas-vindas
#
# Obrigatório:
# [ ] while com limite de tentativas
# [ ] busca manual na lista
# [ ] não usar dict
# =====================================================================

usuarios = ["ana", "joao", "maria"]
senhas = ["1234", "abcd", "senha10"]

def userExiste (user, usuarios):
    return user in usuarios


tentativas = 0 
loginSuccess = False

print('> LOGIN NO SISTEMA: ')

while tentativas < 3 and not loginSuccess:
    user = input('> Informe o Usuário: ')
    if not userExiste(user,usuarios):
        print('>Usuário não existe :( ')
        tentativas += 1
        continue # ignora tudo abaixo e volta ao inicio do while += i
        
    print('>Usuário Válido :) ') # user existir vai pra cá e ignora o if
    suasenha = input(f'>Digite a senha do usuário {user}: ')

    if senhas[usuarios.index(user)] == suasenha: # se a senha digitada for igual a senha na posicão que esta o user na lista:
        print('> Login bem sucedido. Bem vindo!')
        loginSuccess = True
    else:
        print(f'Senha para o usuário {user} inválida, tente novamente')
        tentativas += 1

if not loginSuccess: #se as 3 tentativas foram feitas e o login continuou false:
    print('Acesso bloqueado — tentativas esgotadas.')


# =====================================================================
# Exercício 024: Verificador de CPF simplificado
# Peça um CPF no formato livre, podendo ter pontos e traço:
#
# Extraia apenas os números e valide:
# - deve ter exatamente 11 dígitos
# - não pode conter todos os números iguais, como 11111111111

# Obrigatório:
# [ ] usar while para percorrer caracteres
# [ ] montar nova string só com dígitos
# [ ] validar tamanho
# [ ] validar repetição
# =====================================================================

cpf = '451.244.841-50'
novo_cpf = []

for c in cpf:
    if c.isnumeric():
        novo_cpf.append(c)

for i in novo_cpf:
    if novo_cpf.count(i) == 11:
        print(f'CPF inválido! O nº {i} repetiu 11 vezes')
        break

cpf = ''.join(novo_cpf)
print(f'>{cpf}')


# =====================================================================
# Exercício 026: Sequência de Fibonacci até limite
# Peça um número limite e gere a sequência de Fibonacci até que o próximo
# valor ultrapasse o limite.
#
# Exemplo:
# Limite: 30
# Saída: 0, 1, 1, 2, 3, 5, 8, 13, 21
#
# Obrigatório:
# [ ] usar while
# [ ] não usar lista pronta
# [ ] controlar os dois valores anteriores
# [ ] validar limite maior ou igual a 0
# =====================================================================

numLimite = int(input('Digite um valor que será o limite da sequência de Fibo: '))
a, b = 0, 1
while a < numLimite:
        print(a, end=' ') # 0 1
        a, b = b, a + b # b = 
