import random
import time

global interacciones # Contador de interacciones
interacciones = 0

def busqueda_binaria(lista, comienzo, final, objetivo):
    #print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    global interacciones 
    interacciones += 1
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    tamano_de_lista = int(parameters["tamaño"])#input('De que tamano sera la lista? '))
    objetivo = int(parameters["objetivo"])#input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, parameters["tamaño"]) for i in range(tamano_de_lista)])
    inicio = time.time()
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    fin = time.time()

    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Tiempo de busqueda binaria: {fin - inicio} segundos')
    print(f'Interacciones: {interacciones}')