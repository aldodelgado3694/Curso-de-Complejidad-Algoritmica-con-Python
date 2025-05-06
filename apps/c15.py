#Morral.py

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        
        return 0

    if pesos[n - 1] > tamano_morral:
        
        return morral(tamano_morral, pesos, valores, n - 1)

    case1 =  valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    case2 = morral(tamano_morral, pesos, valores, n - 1)
    
    return max(case1,
                case2)

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main.py
def run(parameters):
    valores = parameters["valores"]
    pesos = parameters["pesos"]
    tamano_morral = parameters["tamaño"]
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)