import os

def line(num=1):
    print(f'"="*30\n{num}"="*30')

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

#listdir() é usado para percorrer SUPERFICIALMENTE as pastas/arquivos
for conteudo in os.listdir():
    if os.path.isfile(conteudo):
        print(f'[ARQ] {conteudo}')
    else:
        print(f'[DIR] {conteudo}')

line(2)
# os.walk(.) também serve para referenciar o diretorio atual
for raiz, subpastas, arquivos in os.walk(os.getcwd()):
    pass