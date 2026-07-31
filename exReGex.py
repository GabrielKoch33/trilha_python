import re

# -- 1 --

texto = "Meu telefone é 47999887766. Tenho 23 anos. Nasci em 2002."

numeros = re.findall(r"\d+",texto)
print(numeros)
# \d = apenas digitos,
# + =  caso exista numeros sozinhos ou uma sequencia


# -- 2 --

texto = "Rua A 89160-000 Rua B 89010-120 Rua C ABCDE"

cep_validos = re.findall(r"\d{5}-\d{3}",texto)
print(cep_validos)

# -- 3 --

texto = """
        João
        joao@gmail.com
        Maria
        maria@hotmail.com
        Pedro
        teste@@gmail
        empresa.com
        """
emails = re.findall(r"\w+@\w+.com",texto)
# [.com] = qualquer um desses elementos de forma individual
# .com = sequencia exata de '.com'
print(emails)

# -- 4 --

texto = """ (47)99999-1111
            (48)98888-2222
            9999-999
            abc
        """

tel = re.findall(r"\(\d{2}\)\d{5}-\d{4}",texto)
# [(] anula o poder do (, porém [] é ideal para grandes opções de busca
# \( tbm anula o poder do (, e nesse caso somente dele (1 caractere)
print(tel)


