# =====================================================================
# Exercício 001: Simulador de fila de atendimento com prioridades.
# Crie um sistema que simula uma fila de atendimento em uma clínica.
# Cada paciente deve ser armazenado como uma tupla: (nome, idade, prioridade).
# A prioridade pode ser:
#   "NORMAL"
#   "PREFERENCIAL"
#   "URGENTE"

# Regras:
# - Pacientes URGENTE devem ser chamados antes de todos.
# - Pacientes PREFERENCIAL devem ser chamados antes dos NORMAIS.
# - Dentro da mesma prioridade, respeite a ordem de chegada.
# - Ao chamar paciente, remova-o da fila.
# - Se a fila estiver vazia, informe corretamente.
# =====================================================================

fila = [
    ("Carlos", 45,"NORMAL"),
    ("Maria",72,"PREFERENCIAL"),
    ("João", 30,"NORMAL"),
    ("Ana",68,"PREFERENCIAL"),
    ("Pedro",25,"URGENTE"),
    ("Lucia",55,"NORMAL"),
    ("Roberto",80,"PREFERENCIAL"),
    ("Fernanda",15,"NORMAL"),
    ("Marcos",40,"URGENTE"),
    ("Beatriz",60,"NORMAL")
]
def remove_paciente(paciente, fila, chegada):
    fila.pop(chegada)
    return f'Paciente {paciente} Removido'

def chamar_proximo(fila):
    '''
    Usar varios if dentro de um loop vai ocasionar de: a cada nova incrementação o programa chamará o paciente,
    independente da PRIORIDADE, sendo que nosso objetivo é primeiro checar se há URGENTES, depois PREF. e dps NORMAL
    '''
    if len(fila) == 0:
        return 'Fila Vazia'

    for chegada, paciente in enumerate(fila):
        if paciente[2] == 'URGENTE':
            print(f'Chamando Paciente {paciente[0]}, {paciente[1]} Anos. Ordem de Chegada {chegada}. Estado {paciente[2]}')
            return remove_paciente(paciente,fila, chegada)
        

    for chegada, paciente in enumerate(fila):
        if paciente[2] == 'PREFERENCIAL':
            print(f'Chamando Paciente {paciente[0]}, {paciente[1]} Anos. Ordem de Chegada {chegada}. Estado {paciente[2]}')
            return remove_paciente(paciente,fila, chegada)
        
    for chegada, paciente in enumerate(fila):
        if paciente[2] == 'NORMAL':
            print(f'Chamando Paciente {paciente[0]}, {paciente[1]} Anos. Ordem de Chegada {chegada}. Estado {paciente[2]}')
            return remove_paciente(paciente,fila, chegada)
        
        
def listar(fila):
    if len(fila) == 0:
        print('Fila vazia.')
        return

    print(f'\n{"#":<4} {"Nome":<18} {"Idade":<7} {"Prioridade"}') # :<18 texto é escrito a esquerda e 18 espaços em brancos são postos a direita
    print('-' * 42)                                               # :>18 texto é escrito a direta e antes dele são inseridos 18 espaços em branco
    for i, paciente in enumerate(fila):                           # :^10 centraliza o texto
        print(f'{i+1:<4} {paciente[0]:<18} {paciente[1]:<7} {paciente[2]}')

def buscar(fila):
    nomePaciente = input('Digite o nome: ').title().strip()
    for paciente in fila:
        if paciente[0] == nomePaciente:
            return f'Paciente: {nomePaciente} | Estado: {paciente[2]}'
    return f'Paciente {nomePaciente} não encontrado.'
    

def cancelar(fila):
    nomePaciente = input('Digite o nome: ').title().strip()
    for chegada, paciente in enumerate(fila):
        if paciente[0] == nomePaciente:
            return remove_paciente(nomePaciente, fila, chegada)
    return f'Paciente {nomePaciente} não encontrado.'

while True:
    print('=================================')
    print('   SISTEMA DE FILA - CLÍNICA     ')
    print('=================================')
    print(' 1 - Chamar próximo paciente     ')
    print(' 2 - Listar fila                 ')
    print(' 3 - Buscar paciente pelo nome   ')
    print(' 4 - Cancelar atendimento        ')
    print(' 0 - Sair                        ')
    print('=================================')
    op = input('Opção: ').strip()
    if op == '1':
        print(chamar_proximo(fila))
    elif op == '2':
        listar(fila)
    elif op == '3':
        print(buscar(fila))
    elif op == '4':
        print(cancelar(fila))
    elif op == '0':
        print('> Saindo...')
        break
    else:
        print('> Opção inválida.')


# =====================================================================
# Exercício 002: Compactador e descompactador de texto simples.
# Crie um programa que compacte e descompacte textos simples.
# A compactação deve transformar repetições consecutivas em letra + quantidade.
# Exemplo:
#   Entrada: aaabbccccd
#   Saída: a3b2c4d1
# A descompactação deve fazer o inverso.
# Exemplo:
#   Entrada: a3b2c4d1
#   Saída: aaabbccccd
# =====================================================================
#
# Menu:
#
# 1 - Compactar texto
# 2 - Descompactar texto
# 0 - Sair
#
# Regras:
#
# - Use while para percorrer a string.
# - Não use bibliotecas.
# - Considere apenas letras seguidas de números de 1 dígito, por enquanto.
# - Valide texto vazio.
# - Na compactação, cuidado com o último bloco de caracteres.

# =====================================================================
# Exercício 003: Sistema de estoque com listas paralelas.
# Crie um sistema de estoque usando três listas paralelas.
# =====================================================================
#
# Estrutura obrigatória:
#
# produtos = []
# quantidades = []
# precos = []
#
# Menu:
#
# 1 - Cadastrar produto
# 2 - Entrada de estoque
# 3 - Saída de estoque
# 4 - Alterar preço
# 5 - Consultar produto
# 6 - Listar estoque completo
# 7 - Mostrar valor total em estoque
# 0 - Sair
#
# Regras:
#
# - Não permitir produto duplicado.
# - Não permitir quantidade negativa.
# - Não permitir preço menor ou igual a zero.
# - Saída de estoque não pode ultrapassar a quantidade disponível.
# - Consulta deve mostrar nome, quantidade, preço unitário e valor total daquele produto.
# - Valor total em estoque = soma de quantidade * preço de todos os produtos.


# =====================================================================
# Exercício 004: Analisador de transações financeiras sem dicionário.
# Crie funções para analisar transações financeiras.
# =====================================================================

transacoes = [
     ("entrada", 1500.00),
     ("saida", 300.00),
     ("saida", 200.00),
     ("entrada", 700.00),
     ("saida", 2500.00)
]

relatorio_transacoes = []

def contEntradaSaida (transacoes, relatorio_transacoes):
    entradas = 0
    saidas = 0
    for log in transacoes:
        if log[0] == 'entrada':
            entradas += 1
        else:
            saidas += 1
    relatorio_transacoes.append(("Entradas:", entradas))
    relatorio_transacoes.append(("Saídas: ", saidas))
    
def Saldo(transacoes, relatorio_transacoes):
    saldo = 0
    trans_negativo = 0
    for id,log in enumerate(transacoes):

        if log [0] == 'entrada':
            saldo += log[1]
        else:
            saldo -= log[1]
            if saldo < 0:
                trans_negativo = id

    relatorio_transacoes.append(("Saldo Final: ",saldo))
    relatorio_transacoes.append(("ID - Transação Saldo Negativo: ", trans_negativo+1))

def MaiorEntrada (transacoes, relatorio_transacoes):
    maior = 0
    for log in transacoes:
        if log[0] == "entrada" and log[1] > maior:
            maior = log[1]

    relatorio_transacoes.append(("Maior Entrada: ", maior))

def MaiorSaida (transacoes, relatorio_transacoes):
    maior = 0
    for log in transacoes:
        if log[0] == "saida" and log[1] > maior:
            maior = log[1]

    relatorio_transacoes.append(("Maior Saída: ", maior))

def TransSuspeitas (transacoes, relatorio_transacoes):
    for id, log in enumerate(transacoes):
        if (log[0] == 'entrada' and log[1] > 5000) or (log[0] == 'saída' and log[1] > 1000):
            relatorio_transacoes.append(('Transação Suspeita: ',id))

contEntradaSaida(transacoes, relatorio_transacoes)
Saldo(transacoes, relatorio_transacoes)
MaiorEntrada(transacoes, relatorio_transacoes)
MaiorSaida(transacoes, relatorio_transacoes)
TransSuspeitas(transacoes, relatorio_transacoes)

for i in relatorio_transacoes:
    print(i)
    
# - Uma transação é suspeita quando a saída for maior que 1000.
# - Uma transação é suspeita quando a entrada for maior que 5000.

# =====================================================================
# Exercício 005: Validador de comandos de terminal simplificado.
# Crie um programa que simula comandos básicos digitados pelo usuário.
# Esse exercício já começa a parecer ferramenta real de automação.
# =====================================================================
# Exemplo de uso:
#
# > add dados.csv
# Arquivo adicionado.
#
# > add logs.txt
# Arquivo adicionado.
#
# > list
# 1 - dados.csv
# 2 - logs.txt
#
# > remove dados.csv
# Arquivo removido.
#
# > exit
# Encerrando.
#
# Regras:
#
# - Armazene os arquivos em uma lista.
# - Não permita arquivo duplicado.
# - Não permita remover arquivo inexistente.
# - O comando list mostra todos os arquivos.
# - O comando clear limpa a lista.
# - O comando exit encerra o programa.
# - Qualquer comando fora do padrão deve ser rejeitado.
#=====================================================================

def addDict (logs_comandos):

    for acao in logs_comandos:
        if acao not in relatorio_acessos:
            relatorio_acessos[acao] = 0
        relatorio_acessos[acao] += 1


def exist (arq_name, lista_arquivos):
    return arq_name in lista_arquivos # retorna true se existir, false se não existir

def add(arq_name,lista_arquivos):
    logs_comandos.append('> add')
    addDict (logs_comandos)

    if exist(arq_name, lista_arquivos):
        return 'Arquivo já existênte'
    else:
        lista_arquivos.append(arq_name)

def remove(arq_name,lista_arquivos):
    logs_comandos.append('> remove')
    addDict(logs_comandos)

    if not exist(arq_name, lista_arquivos):
        return 'Arquivo inexistênte\n nada a remover'
    else:
        lista_arquivos.remove(arq_name)

def ls(lista_arquivos):
    logs_comandos.append('> list')
    addDict(logs_comandos)

    for i in lista_arquivos:
        print(i)

def clear(lista_arquivos):
    logs_comandos.append('> clear')
    addDict(logs_comandos)
    lista_arquivos.clear()

lista_arquivos = []
logs_comandos = []
relatorio_acessos = {}

while True:
    print('-'*30)
    print('''
    1 - add 
    2 - remove
    3 - list
    4 - clear
    5 - exit
    ''')
    print('-'*30)
    op = int(input('> type command do start working...'))
    if op == 1:
        arq_name = input('Nome do Arquivo: ')
        add(arq_name,lista_arquivos)
    elif op == 2:
        arq_name = input('Nome do Arquivo: ')
        remove(arq_name,lista_arquivos)
    elif op == 3:
        ls(lista_arquivos)
    elif op == 4:
        clear(lista_arquivos)
    elif op == 5:
        break


# =====================================================================
# Exercício 006: Detector de duplicidade e conflito em cadastros.
# Crie um sistema de cadastro simples.
# Variação mais difícil: detectar CPFs com todos os dígitos iguais, como 11111111111.
# =====================================================================
#
# Estrutura obrigatória:
#
# emails = []
# cpfs = []
#
# Menu:
#
# 1 - Cadastrar pessoa
# 2 - Verificar e-mails duplicados
# 3 - Verificar CPFs duplicados
# 4 - Listar cadastros
# 0 - Sair
#
# Regras:
#
# - O CPF deve ter 11 dígitos após remover pontos e traço.
# - O e-mail deve conter @ e ponto após o @.
# - Não bloqueie duplicados no cadastro.
# - As opções 2 e 3 devem detectar duplicidades depois.
# - Mostre quais e-mails ou CPFs aparecem repetidos.
# - Faça a detecção sem usar dicionários.


# =====================================================================
# Exercício 007: Interpretador de expressões matemáticas simples.
# Crie um programa que recebe expressões no formato: numero operador numero.
# Este é muito bom para sair de exercício acadêmico comum.
# =====================================================================
#
# Estrutura obrigatória:
#
# Exemplos:
# 10 + 5
# 20 - 3
# 4 * 8
# 9 / 3
# 10 // 3
# 10 % 3
# 2 ** 5
#
# Menu:
#
# 1 - Calcular expressão
# 2 - Ver histórico
# 3 - Limpar histórico
# 0 - Sair
#
# Regras:
#
# - Use split() para separar a expressão.
# - Valide se existem exatamente 3 partes.
# - Valide se os números são válidos.
# - Não permita divisão por zero.
# - Salve no histórico uma tupla: (expressao, resultado).
# - Não use eval().


# =====================================================================
# Exercício 008: Gerenciador de tarefas com estados.
# Crie um sistema de tarefas usando lista de tuplas: (titulo, status).
# Status possíveis:
#   "PENDENTE"
#   "EM_ANDAMENTO"
#   "CONCLUIDA"
# Esse exercício conversa bem com sistemas reais.
# =====================================================================
#
# Menu:
#
# 1 - Criar tarefa
# 2 - Alterar status
# 3 - Listar todas
# 4 - Listar por status
# 5 - Remover tarefa
# 6 - Mostrar resumo
# 0 - Sair
#
# Regras:
#
# - Não permitir título vazio.
# - Não permitir tarefa duplicada.
# - Para alterar status, buscar pelo título.
# - Como tupla é imutável, você precisará substituir a tupla inteira na lista.
# - O resumo deve mostrar quantidade de tarefas por status.


# =====================================================================
# Exercício 009: Simulador de processamento em lote.
# Crie um sistema que simula o processamento de arquivos pendentes.
# Esse exercício é diretamente alinhado com Engenharia de Dados.
# =====================================================================
#
# Estrutura obrigatória:
#
# arquivos = [
#     "clientes.csv",
#     "vendas.csv",
#     "produtos.txt",
#     "logs.csv",
#     "backup.zip",
#     "eventos.csv"
# ]
#
# Relatório esperado:
#
# Arquivos processados:
# - clientes.csv
# - vendas.csv
# - logs.csv
# - eventos.csv
#
# Arquivos rejeitados:
# - produtos.txt
# - backup.zip
#
# Total processados: 4
# Total rejeitados: 2
#
# Regras:
#
# - Só arquivos .csv devem ser processados.
# - Arquivos com outra extensão devem ser rejeitados.
# - Cada arquivo processado deve ir para uma lista de processados.
# - Cada arquivo rejeitado deve ir para uma lista de rejeitados.
# - O processamento deve ocorrer um arquivo por vez, usando while.
# - Ao final, mostre relatório.
# - O relatório deve mostrar os arquivos processados.
# - O relatório deve mostrar os arquivos rejeitados.
# - O relatório deve mostrar o total de processados.
# - O relatório deve mostrar o total de rejeitados.


# =====================================================================
# Exercício 010: Mini validador de dataset tabular.
# Crie um programa que analisa uma tabela e gera um relatório de qualidade.
# =====================================================================

dados = [
     ["id", "nome", "idade", "cidade"],
     ["1", "Ana", "23", "Curitiba"],
     ["2", "", "", "São Paulo"],
     ["3", "", "45", "Rio de Janeiro"],
     ["4", "Carlos", "abc", "Belo Horizonte"],
     ["5", "Daniela", "29", ""]
]


lista_erros = []
colunas = [] #id, nome, idade, cidade
linhas_invalidas = linhas_validas = 0

for item in dados[0]:
    colunas.append(item)

for linha in dados[1:]: # ignora a primeira linha de colunas e começa ja nos registros
    linha_tem_erro = False
    for i,item in enumerate(linha):

        if item ==  '':
            lista_erros.append((linha[0],colunas[i],'campo vazio'))
            linha_tem_erro = True

        elif i == 2 and not item.isnumeric(): 
            lista_erros.append((linha[0], colunas[i],'valor não numérico'))
            linha_tem_erro = True

    if linha_tem_erro:
        linhas_invalidas += 1

linhas_validas = (len(dados)-1) - (linhas_invalidas) 

for j in lista_erros:
    print(j)

print(linhas_invalidas)
print(linhas_validas)
 
 

# Formato dos erros:
# (numero_linha, nome_coluna, descricao_erro)
# (2, "idade", "campo vazio")
# (3, "nome", "campo vazio")
# (4, "idade", "valor não numérico")
# Regras:

# - A primeira linha é o cabeçalho.
# - As demais linhas são registros.
# - Verifique campos vazios.
# - Verifique se idade é numérica.
# - Conte quantas linhas válidas existem.
# - Conte quantas linhas inválidas existem.
# - Guarde os erros em uma lista de tuplas.
# - O formato dos erros deve ser: (numero_linha, nome_coluna, descricao_erro).

# =====================================================================
# Exercício 011: Você recebeu um arquivo CSV exportado de um sistema legado.
# Os dados estão sujos: espaços sobrando, campos em maiúsculo, separador inconsistente.
# Escreva uma função que:
# recebe uma lista de linhas brutas e retorna uma lista de dicionários limpos.

#saída esperada:
# [
#   {"id": "1", "nome": "Ana Silva",    "salario": 4500.0},
#   {"id": "2", "nome": "Carlos Souza", "salario": 3200.0},
#   {"id": "3", "nome": "Maria Lima",   "salario": 5100.5}
# ]
# =====================================================================
csv = [
    "ID ; NOME ; SALÁRIO ", 
    "1;  Ana Silva ;4500.0",
    "2; CARLOS SOUZA;  3200",
    "3; maria lima ;5100.50"
]

csv_limpo = [] #lista final

linhas = [] 
for item in csv: # para cada string de csv
    linhas.append(item.strip().split(';')) #vai ser adicionado em 'linhas' a string convertida em lista com o split:
    #[[ ID, NOME, SALÁRIO ], ["1", Ana Silva, ...][...]] 
    

colunas = linhas[0]   # Colunas do CSV vai receber o primeiro elemento de linhas =  [ ID, NOME, SALÁRIO ]
for linha in linhas[1:]:                    # pula o cabeçalho, apenas os dados
    novo = {}                               # dict vazio para cada registro de pessoa
    for i in range(len(colunas)):
        chave = colunas[i].strip().lower()# id, nome, salário
        valor = linha[i].strip()            # 1, Ana Silva, 4500
        novo[chave] = valor                 # preenche o dict
    csv_limpo.append(novo)                  # guarda na lista

for i in csv_limpo:   
    print(i)

# =====================================================================
# Exercício 012: Você está construindo um mecanismo de busca simples.
# Dado um conjunto de documentos, construa um índice invertido:
# para cada palavra, quais documentos a contêm.

# Saída esperada:
    # {
    #   "python": ["doc1", "doc3"],
    #   "é":      ["doc1", "doc2"],
    #   "rápido": ["doc1"],
    #   ...
    # }
# =====================================================================

docs = {
    "doc1": "python é rápido e simples",
    "doc2": "java é verboso mas robusto",
    "doc3": "python tem muitas bibliotecas"
}

palavras_doc = {

}

for doc, text in docs.items():
    for palavra in text.split():
        if palavra not in palavras_doc:
            palavras_doc[palavra] = []
        if doc in palavras_doc[palavra]:
            continue
        palavras_doc[palavra].append(doc)

for i,j in palavras_doc.items():
    print(i,j)
            

# =====================================================================
# Exercício 013: Antes de inserir registros num banco, 
# você precisa validar se cada campo tem o tipo correto
# e se os campos obrigatórios estão presentes. 
# Escreva uma função que recebe um registro 
# e um esquema e retorna uma lista de erros encontrados.
    # saída esperada:
    # [
    # "Campo 'idade': esperado int, recebido str",
    # "Campo 'ativo': ausente"
    # ]
# =====================================================================

esquema = {
    "nome": str,
    "idade": int,
    "salario": float,
    "ativo": bool
}
registro = {"nome": "Ana",
             "idade": "vinte", 
             "salario": 3000.0}

erros = [ ]

def validador(registro, esquema):
    for campo, tipo in esquema.items():
        if campo not in registro.keys():
            erros.append(f"Campo '{campo}': Ausente")
        else:
            if tipo != type(registro[campo]):
                erros.append(f"Campo '{campo}': esperado tipo {tipo}, recebido {type(registro[campo])}")
            else:
                print(f'Campo: {campo} Foi Preenchido corretamente, obrigado!')
        
    return erros

print(validador(registro,esquema))
