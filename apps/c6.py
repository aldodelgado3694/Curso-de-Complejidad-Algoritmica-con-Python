import random
import time

global interacciones # Contador de interacciones
interacciones = 0

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        global interacciones 
        interacciones += 1
        if elemento == objetivo:
            match = True
            break

    return match

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    tamano_de_lista = int(parameters["tamaño"])#input('De que tamano sera la lista? '))
    objetivo = int(parameters["objetivo"])#input('Que numero quieres encontrar? '))

    lista = [random.randint(0, parameters["tamaño"]) for i in range(tamano_de_lista)]

    inicio = time.time()
    encontrado = busqueda_lineal(lista, objetivo)
    fin = time.time()

    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Tiempo de busqueda lineal: {fin - inicio} segundos')
    print(f'Interacciones: {interacciones}')