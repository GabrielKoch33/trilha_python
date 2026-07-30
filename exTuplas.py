# ==========================================================================================================
# Crie um sistema de placar que recebe jogadas como tuplas (jogador, pontos), 
# acumula os pontos por jogador numa lista e exibe o ranking final do mais pontuado ao menos pontuado
# ==========================================================================================================

jogadas = [
    ("Alice", 30), ("Bob", 20), ("Alice", 15),
    ("Carlos", 40), ("Bob", 35), ("Carlos", 10) 
                ]

placar = {} # Criado Dicionário Placar; Nome: Pontos

# Percorre cada tupla desempacotando jogador e pontos
for jogador, pontos in jogadas:
    if jogador not in placar: # Se Alice não estiver no placar, então:
        placar[jogador] = 0 #"Alice" é adicionada com 0 pontos

    placar[jogador] += pontos # Se o jogador já estiver no placar, então seus pontos são somados cada vez que ele aparece

# Ordena do maior para o menor pela pontuação
ranking = sorted(placar.items(), key=lambda item: item[1], reverse=True)

for posicao, (jogador, pontos) in enumerate(ranking, start=1):
    print(f"{posicao}º {jogador}: {pontos} pts")

print()
# saída esperada:
# 1º Bob: 55 pts
# 2º Carlos: 50 pts
# 3º Alice: 45 pts

# ==============================================================================
# Você recebe uma lista de transações como tuplas (tipo, valor). 
# Calcule o saldo final, o total de entradas, o total de saídas e alerte se o saldo ficar negativo em algum momento.
# ==============================================================================
transacoes = [
    ("entrada", 1000.0), #0
    ("saída", 250.0),    #1
    ("entrada", 500.0),  #2
    ("saída", 1400.0),   #3 NEGATIVO AQUI
    ("entrada", 300.0)   #4
]
totentrada = 0 #valor TOTAL da entrada | 1000;
totsaida = 0    
caixa = 0 
saldoneg = -1
for i in range(len(transacoes)):
    if transacoes[i][0] == 'entrada':
        totentrada += transacoes[i][1]
        caixa += transacoes[i][1]
    else:                               # Se for saída
        totsaida += transacoes[i][1]
        caixa -= transacoes[i][1]
        if caixa < 0:
            saldoneg = i+1 # i+1 para facilitar a leitura humana à lista

if saldoneg == -1:
    saldoneg = 'Não houve prejuízo'
print(f'Valor Total de Entradas: R${totentrada}\n Valor Total de Saídas: R${totsaida}\n Saldo Final em Caixa: R${caixa}\n Caixa Negativo na Transação nº{saldoneg}')
print()

# ==============================================================================
# Você tem uma lista de tuplas com dados de funcionários (nome, cargo, salário). 
# Exiba apenas os que ganham mais de R$3000.
# ==============================================================================

funcionarios = [
    ("Carlos", "Dev", 4500.0),
    ("Maria", "Designer", 2800.0),
    ("João", "Analista", 3200.0),
    ("Ana", "Estagiária", 1500.0)
]

for f in range(len(funcionarios)):
    if funcionarios[f][2] > 3000:
        print(f'Nome: {funcionarios[f][0]} | Cargo: {funcionarios[f][1]}')
print()

# ========================================================================================================
# Crie uma função que recebe uma lista de números e retorna o maior, o menor e a média — tudo de uma vez. 
# Desempacote o resultado ao chamar.
# ========================================================================================================
import statistics as st

def estatistica(numeros):
    a = max(numeros)
    b = min(numeros)
    c = st.mean(numeros) #ou = sum(numeros)/len(numeros)
    return a,b,c 

numeros = [4, 8, 2, 10, 5]
maior, menor, media = estatistica(numeros)
print(f'Maior: {maior}; Menor: {menor}; Média: {media}')
print()

# ==========================================================================================================
# Dada a lista de produtos, ordene-a pelo preço (do mais barato ao mais caro) e exiba o resultado formatado.
# ==========================================================================================================
              
produtos = [
    ("Monitor", 900.0),
    ("Mouse", 80.0),
    ("Teclado", 150.0),
    ("Webcam", 130.0)
]

for i in range(len(produtos) - 1):
    for j in range(len(produtos) - i - 1):
        if produtos[j][1] > produtos[j + 1][1]:
            aux = produtos[j]
            produtos[j] = produtos[j + 1]
            produtos[j + 1] = aux

print(produtos)

# ======================================================================
# Desempacote e exiba: Produto: Teclado | Preço: R$150.00 | Estoque: 10"
# ======================================================================
produto = ("Teclado", 150.0, 10)

a,b,c = produto
print(f' | Produto: {a}\n | Preço: {b}\n | Estoque: {c}')

# =====================================================================
# Crie uma tupla de cores. Tente modificar um elemento e observe o erro. 
# Depois converta para lista, altere, e converta de volta para tupla.
# =====================================================================

cores = ("vermelho", "verde", "azul")
print(cores)
# 1. tente cores[0] = "amarelo" e veja o erro
# 2. converta para lista, mude o primeiro para "amarelo"
# 3. converta de volta para tupla e exiba
lista = list(cores)
lista[0] = 'Amarelo'
cores = tuple(lista)
print(cores)

# =====================================================================
# Quantas vezes aparece 7.0?
# Em qual índice está o primeiro 9.0?
# =====================================================================
notas = (6.0, 7.0, 9.0, 7.0, 8.5, 9.0, 7.0)

print(f'O 7 aparece {notas.count(7.0)} vezes')
print(f'O primeiro 9 aparece no indice {notas.index(9.0)+1}')