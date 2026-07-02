#Principais comandos (modos) de execução:
#'r' = Read/leitura, o arquivo deve existir previamente
#'w' = Write/Escrita, se o arquivo não existir, ele é criado, caso ja exista, o conteúdo é sobreescrito
#'a' = Add/Anexar, adiciona informações ao final do arquivo
#'x' = Xclusive/Exclusivo, cria um novo arquivo somente se ele não existir 
#'b' = Binary, usado para arquivos binários, como imagens ou vídeos. ex: 'rb' (lê arquivos binários)
#'t' = Text, usado para arquivos de texto
#'+' = Att/Atualização, permite Leitura e Escrita juntas. ex: 'r+' ou 'w+'

#============================================================
# ESCRITA
#============================================================
arquivo = open('ola_mundo.txt','w')
arquivo.write('Olá, Mundo!')
arquivo.close()# <- sempre muito importante fecharmos o arquivo após o uso para que o SO libere memória e o acesso ao documento para 3ºs

#============================================================
# LEITURA
#============================================================
arquivo = open('ola_mundo.txt','r')
conteudo = arquivo.read()# <- variavel conteudo recebe todo o conteúdo do arquivo 
print(conteudo)# <- nesse caso estamos exibindo todo o texto interno

arquivo = open('ola_mundo.txt','w')
arquivo.write(
    'Lorem ipsum dolor sit amet,'
    'consectetur adipiscing elit.'
    'Vivamus sodales turpis quis tortor malesuada interdum.'
    'Praesent in elit bibendum felis rutrum ultricies.' 
    'Aenean in venenatis est, vestibulum dapibus enim.' 
    'Praesent aliquet cursus neque, in imperdiet nisi rutrum id.'
    'Donec lectus orci, malesuada eu volutpat at, pellentesque a tellus.'
    'Suspendisse ullamcorper ut neque iaculis ultrices.' 
    'Etiam vel tortor et ex cursus tincidunt ut quis nulla.' 
    'Sed quis fermentum ipsum, non blandit odio.'
    )

arquivo.close()


with open('ola_mundo.txt', 'r') as file:
    linha_conteudo = file.readline()

print(linha_conteudo)# <- caso desejassemos visualizar apenas a primeira linha de um texto, usamos .readline()

#============================================================
# DELETAR
#============================================================
# para deletarmos um arquivo precisamos importar o módulo .os
import os

os.remove('ola_mundo.txt')


#============================================================
# MANIPULANDO ARQUIVOS COM O STATEMENT 'with'
#============================================================
'''
With é usado para nos ajudar a abrir arquivos, trabalharmos neles, e que seja fechado corretamente
mesmo em casos de erro
'''
# aqui vai dar erro pq excluímos o arquivo acima, a agora tentamos ler 
with open('ola_mundo.txt','r') as file:# <- abre arquivo, e 'file' recebe seu conteudo
    conteudo = file.read()             # <- lemos o 'file' e passamos seu conteudo, caso o arquivo não exista, fecha
    print(conteudo)                    # <- print
                                       # <- arquivo fechado naturalmente
'''                                    
Durante o bloco With, as operações são realizadas, e em casos de Exceções, ele é fechado automaticamente.
Garantindo devido encerramento do processo.
'''