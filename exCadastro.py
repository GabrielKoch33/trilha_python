# ==========================================================================================================================================
# 📋 Você trabalha num sistema de cadastro de usuários. Antes de salvar, o sistema precisa validar se os dados estão corretos.
# ==========================================================================================================================================

nome = "Ana S7474ilva"
email = "ana@email.com"
idade = 16
senha = "afg"


if not isinstance(nome, str):
    erroNome = 1
else:   
    erroNome = 0                             
    # gabriel koch da silva
    nome = nome.strip().split()
    for p in nome:
        if (len(p) == 1) or (not p.isalpha()) : 
            erroNome += 1 
            # REPLACE APENAS FUNCIONA EM STRING, NESSE CASO EU TORNEI NOVO NOME UMA LISTA COM STRINGS (1º e 2º nome)

email = email.strip()
if '@' not in email or '.com' not in email: # @ e .com existem?
    email_valido = False
else:
    email_valido = True

    for c in email:
        if c.isalpha() and c.isupper():
            email_valido = False
            break
        
if idade < 18:
    idade_valida = False
else:
    idade_valida = True

if len(senha) < 6:
    senha_valida = False
else: 
    senha_valida = True
                    
     
acesso = 0 # >= 1 acesso negado
if erroNome == 0:
    print('Nome Válido')
else:
    print('Nome Inválido (NOME INVÁLIDO AOS PADRÕES DO SITE)')
    acesso += 1
if email_valido == True:
    print('Email Válido')
else:
    print('Email Inválido (EMAIL INEXISTÊNTE)')
    acesso += 1
if idade_valida == True:
    print('Idade Válida')
else:
    print('Idade Inválida (MENOR DE IDADE)')
    acesso += 1
if senha_valida == True:
    print('Senha Válida')
else:
    print('Senha Inválida (SENHA FRACA)')
    acesso += 1
if acesso >= 1:
    print('Cadastro REJEITADO')

