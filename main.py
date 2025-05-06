import argparse
from apps import modulos


if __name__ == "__main__":
    #modulos["c2"].run({"n":2000})
    #modulos["c6"].run({"tamaño": 10000, "objetivo": 50})
    #modulos["c7"].run({"tamaño": 10000, "objetivo": 50})
    #modulos["c8"].run({"tamaño": 1000000})
    #modulos["c9"].run({"tamaño": 20})
    #modulos["c10"].run({"tamaño": 5})
    #modulos["c13exercice"].run({"fechaIni": "2018-01-01", "fechaFin": "2025-05-06"})
    #modulos["c15"].run({"valores": [60, 100, 120], "pesos": [10, 20, 30], "tamaño": 50})
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--modulo", help="Nombre de modulo a ejecutar validos (c2, c6, c7, c8, c9, c10, c13exercice, c15)", type=str)
    parser.add_argument("-t", "--tamaño", help="Tamaño de la lista a ordenar valido en (c6, c7, c8, c9, c10, c15)", type=int)
    parser.add_argument("-o", "--objetivo", help="Objetivo de la lista a ordenar valido en (c6 y c7)", type=int)
    parser.add_argument("-i", "--fechaI", help="Fecha de inicio en formato YYYY-MM-DD valido en c13exercice", type=str)
    parser.add_argument("-f", "--fechaF", help="Fecha de fin en formato YYYY-MM-DD valido en c13exercice", type=str)
    parser.add_argument("-v", "--valores", help="Valores del morral valido en c15", type=list)
    parser.add_argument("-p", "--pesos", help="Pesos del morral valido en c15", type=list)
    parser.add_argument("-n", "--n", help="Numero de elementos a calcular en c2", type=int)
    args = parser.parse_args()
    modulo = ""
    parametros = {}
    if args.modulo:
        modulo = args.modulo
    else:
        print("No se ha indicado un modulo a ejecutar")
        exit(1)
    if args.tamaño:
        parametros["tamaño"] = args.tamaño
    if args.objetivo:
        parametros["objetivo"] = args.objetivo
    if args.fechaI:
        parametros["fechaIni"] = args.fechaI
    if args.fechaF:
        parametros["fechaFin"] = args.fechaF
    if args.valores:
        parametros["valores"] = args.valores
    if args.pesos:
        parametros["pesos"] = args.pesos
    if args.n:
        parametros["n"] = args.n
    

    modulos[modulo].run(parametros)

