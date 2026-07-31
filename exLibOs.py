import os

def line(num):
    print("="*30)
    print(num)
    print("="*30)

if not os.path.exists("dataset"):
    os.mkdir("dataset")

os.chdir("dataset")
# os já é automaticamente movido para o local indicado
# ele não precisa que seja guardado em uma variavel.
# Caso diretorio não exista da erro.

estrutura = {
    "fotos": ["praia.png","cachorro.jpeg"],
    "documentos": ["contrato.txt","contatos.docx"]
}

# Dentro da pasta Dataset
for pasta, arquivos in estrutura.items():
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    # Caso não exista, criamos a pasta da estrutura
    for arquivo in arquivos:
        # path.join vai guardar a string do caminho do arquivo
        # ele ainda não existe, apenas 'visualizamos' seu destino
        caminho_ = os.path.join(pasta, arquivo)
        with open(caminho_,'w') as f:
            f.write('')
        # o arquivo, caso não exista é criado
        # caso já exista: é sobrescrito

with open('planilha.xlsx','w') as p:
    p.write('Oii')

print(os.getcwd())

# =============================================================

line(1)
print(f'Diretório Atual:\n{os.getcwd()}')

print(f'Itens encontrados: \n  ')

# listdir() é usado para percorrer SUPERFICIALMENTE as pastas/arquivos
for conteudo in os.listdir():
    if os.path.isfile(conteudo):
        print(f'[ARQ] {conteudo}')
    else:
        print(f'[DIR] {conteudo}')

line(2)
# os.walk(.) também serve para referenciar o diretorio atual
p = 0
a = 0
for raiz, subpastas, arquivos in os.walk(os.getcwd()):

    for subpasta in subpastas:
        p += 1
    for arquivo in arquivos:
        a += 1

print(f'Total de pastas: {p}')
print(f"Total de arquivos: {a}")

line(3)
dataset = [
    'foto.jpg',
    'foto2.jpg',
    'texto.pdf',
    'planilha.xlsx',
    'imagem.png',
    'musica.mp3',
]

for arquivo in dataset:
    with open(arquivo, 'w') as f:
        f.write(' ')

extensoes = {'JPG': 0,"PDF":0,"XLSX":0,"PNG":0,"MP3":0}
for arquivo in os.listdir():
    if arquivo.endswith('.jpg'):
        extensoes["JPG"] += 1
    elif arquivo.endswith('.pdf'):
        extensoes["PDF"] += 1
    elif arquivo.endswith('.xlsx'):
        extensoes["XLSX"] += 1
    elif arquivo.endswith('.png'):
        extensoes["PNG"] += 1
    elif arquivo.endswith('.mp3'):
        extensoes["MP3"] += 1

for tipo,qtd in extensoes.items():
    print(f"{tipo} => {qtd}")

line(4)

for item in os.listdir():
    arquivo = False
    print(f"Arquivo:\n {item}")
    if os.path.isfile(item):
        nome, ext = os.path.splitext(item)
        print(f"Nome:\n {nome}")
        print(f"Extensão:\n {ext}")
        arquivo = True
    print(f"Absoluto:\n {os.getcwd()}")
    print(f"É arquivo?\n {arquivo}")

line(5)

# dataset = [
#     "IMG001.jpg",
#     "IMG002.jpg",
#     "IMG003.jpg",
#     "IMG004.jpg",
# ]

# for item in dataset:
#     with open(item,'w') as f:
#         f.write(' ')

os.chdir("IMG")
i = 1
for arquivo in os.listdir():
    os.rename(arquivo,'Foto_00' + str(i))
    i += 1

line(6)

docs = {
    "contratos": ['janeiro.pdf','fevereiro.pdf'],
    "notas": ['aula1.pdf','aula2.pdf','aula3.pdf'],
}
os.chdir("..")
if not os.path.exists("ex06"):
    os.mkdir("ex06")
os.chdir("ex06")

for pasta, documentos in docs.items():
    if not os.path.exists(pasta):
        os.mkdir(pasta)

    for doc in documentos:
        caminho_ = os.path.join(pasta,doc)
        with open(caminho_,'w') as f:
            f.write(' ')

for root,subpastas,arquivos in os.walk('.'):

    for arquivo in arquivos:
        if arquivo.endswith('.pdf'):
            print('PDF encontrado')
            print(os.path.join(os.getcwd(),arquivo))


if __name__ == '__main__':
    line()