#Complejidad algoritmica.py

import sys
import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 0:
        return 1

    return n * factorial_r(n - 1)


#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    n = parameters["n"]

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)
    
    print("Recursion limit: ", sys.getrecursionlimit())
    if sys.getrecursionlimit() < n:
        sys.setrecursionlimit(parameters["n"]+100)
    print("New Recursion limit: ", sys.getrecursionlimit())
  
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)