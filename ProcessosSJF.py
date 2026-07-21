# fazer uma lista onde cada processo vai ter uma numeração e um valor, o codigo vai analisar o com menos valor e dar remove()
import time
lista_de_processos = [('P1',5),('P2',1),('P3',7),('P4',3),('P5',4),('P6',10),('P7',2)]

while lista_de_processos:
    posicao_menor = 0  

    for indice in range(len(lista_de_processos)):
        if lista_de_processos[indice][1] < lista_de_processos[posicao_menor][1]:
            posicao_menor = indice  # atualiza se encontrar um menor

    print(f'Processo [{lista_de_processos[posicao_menor][0]}] é o com menor tempo de conclusão ({lista_de_processos[posicao_menor][1]})segundos. Removido!', flush=True)
    time.sleep(1)
    lista_de_processos.pop(posicao_menor)

print('Todos processos foram finalizados do menor tempo para o maior')
print(lista_de_processos)
