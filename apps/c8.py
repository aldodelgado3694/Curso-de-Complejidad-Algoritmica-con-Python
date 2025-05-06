
import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    tamano_de_lista = int(parameters["tamaño"])#input('De que tamano sera la lista? '))

    lista = [random.randint(0, parameters["tamaño"]) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)