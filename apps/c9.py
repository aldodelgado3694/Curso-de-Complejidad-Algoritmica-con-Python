
import random


def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    tamano_de_lista = int(parameters["tamaño"])#input('De que tamano sera la lista? '))

    lista = [random.randint(0, parameters["tamaño"]) for i in range(tamano_de_lista)]
    print(lista)

    ordenamiento_por_insercion(lista)
    
    print(lista)