
# =====================================================================
# Contar vogais
# =====================================================================

def vogais(frasevogais):
    contadorvogal = 0
    for i in range(len(frasevogais)):
        if frasevogais[i].lower() in 'aeiou':
            contadorvogal += 1
    return contadorvogal

frasevogais = input('Escreva frase: ')
resultado = vogais(frasevogais)
print(resultado)


# =====================================================================
# Palí­ndromo
# =====================================================================
def palindromo(frase):
    frase = frase.lower().replace(' ', '')
    frase_invertida = frase[::-1]
    return frase == frase_invertida

frase = input('Digite uma frase e veremos se Ã© palÃ­ndromo: ')
print(palindromo(frase))


# =====================================================================
# Substituição sem replace
# =====================================================================
def substituicao(frasevelha, oldpalavra, newpalavra):
    s = frasevelha.split()

    for i in range(len(s)):
        if s[i] == oldpalavra:
            s[i] = newpalavra

    frasenova = " ".join(s)
    return frasenova

frasevelha = input('Frase: ')
oldpalavra = input('Qual palavra da frase vai ser mudada?: ')
newpalavra = input('Qual vai ser a nova palavra?: ')
resultado1 = substituicao(frasevelha, oldpalavra, newpalavra)
print(resultado1)


# =====================================================================
# Ler email
# =====================================================================
def ler_email(e):
    achou = -1
    for i in range(len(e)):
        if e[i] == '@':
            achou = i
            break

    if achou == -1:
        print('Email invÃ¡lido')
    else:
        print(f'UsuÃ¡rio: {e[:achou]}')
        print(f'DomÃ­nio: {e[achou+1:]}')

e = input('Qual Ã© seu email?: ')
ler_email(e)


# =====================================================================
# Maior palavra
# =====================================================================
def qtd(frase):
    dividida = frase.split()

    if len(dividida) == 0:
        return ''

    maior = dividida[0]

    for i in range(1,len(dividida)):
        if len(dividida[i]) > len(maior):
            maior = dividida[i]

    return maior

frase = input('Digite uma frase: ')
resultado = qtd(frase)
print(resultado)


# =====================================================================
# Inverter ordem das palavras
# =====================================================================
def inverso(frase):
    d = frase.split()

    i = 0
    while i < len(d) // 2:
        aux = d[i]
        d[i] = d[len(d)-1-i]
        d[len(d)-1-i] = aux
        i += 1

    return " ".join(d)

frase = input('Digite a frase: ')
resultado = inverso(frase)
print(resultado)


# =====================================================================
# Formatação tí­tulo manual
# =====================================================================
def cap_nome(nome):
    newname = nome.split()
    resultadol = []

    for i in newname:
        novapalavra = i[0].upper() + i[1:].lower()
        resultadol.append(novapalavra)

    return " ".join(resultadol)

nome = input('Digite seu nome: ')
print(cap_nome(nome))


# =====================================================================
# Validar senha
# =====================================================================
def validaSenha(senha):
    tem_numero = False
    tem_maiuscula = False
    tem_especial = False
    especiais = '@#$%&Â©Â®â‚¬Â°!*-_'

    if len(senha) < 8:
        print('A senha deve conter no mÃ­nimo 8 caracteres')
        return

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True
        if caractere in especiais:
            tem_especial = True

    if not tem_numero:
        print('A senha deve conter pelo menos 1 nÃºmero')
    elif not tem_maiuscula:
        print('A senha deve conter pelo menos 1 letra maiÃºscula')
    elif not tem_especial:
        print('A senha deve conter pelo menos 1 caractere especial')
    else:
        print('Senha forte')

senha = input('Digite sua senha: ')
validaSenha(senha)


# =====================================================================
# Extraindo apenas os números do CPF s/ replace()
# =====================================================================
def formata(cpf):
    novocpf = ''
    for caractere in cpf:
        if caractere.isdigit():
            novocpf += caractere
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12): ')
cpfnumerico = formata(cpf)
print(cpfnumerico)


# =====================================================================
# Extraindo apenas os números do CPF c/ replace()
# =====================================================================
def formatacao(cpf):
    novocpf = cpf.replace('.', '').replace('-', '')
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12): ')
cpfnumerico = formatacao(cpf)
print(cpfnumerico)


# =====================================================================
# Faça uma função que receba uma frase e substitua todas as ocorrências
# de uma palavra por outra, sem usar replace().
# =====================================================================
def substituicao(frasevelha,oldpalavra, newpalavra):
    s = frasevelha.split() 
    for i in s: 
        if i == oldpalavra:
            i = newpalavra
                            
    frasenova = " ".join(s) 
    return frasenova
# Para o python uma lista ['a','b'] as ASPAS e VIRGULAS são meramente para visuais
# Logo, usar o " ".join(lista) ligará os elementos com um espaço ' '

frasevelha = input(print('frase: ')) 
oldpalavra = input(print('qual palavra da frase vai ser mudada?: '))
newpalavra = input(print('qual vai ser a nova palavra?: '))
resultado1 = substituicao(frasevelha,oldpalavra, newpalavra)
print(resultado1)


def ler_email(e):
    for i in range(len(e)):
        if e[i] == '@':
            achou = i
    print(f'UsuÃ¡rio: {e[:achou-1]}')    
    print(f'DomÃ­nio: {e[achou:]}')

e = print(input('Qual Ã© seu email?: '))
ler_email(e)


# =====================================================================
# Dada a string 'Maria:25:São Paulo', separe os dados usando ':'
# como separador e exiba nome, idade e cidade em linhas separadas.
# =====================================================================
def formulada (dados):
    print(f'Nome: {dados[0]}')
    print(f'Idade: {dados[1]}')
    print(f'Cidade: {dados[2]}')
    
dados = "Maria:25:São Paulo"
formulada(dados.split)

