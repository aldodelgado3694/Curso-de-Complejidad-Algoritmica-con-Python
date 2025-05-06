import os

modulos = {}

for archivo in os.listdir(os.path.dirname(__file__)):
    if archivo.endswith(".py") and archivo != "__init__.py":
        nombre_modulo = archivo[:-3]
        try:
            # Importa directamente al espacio de nombres del paquete
            exec(f"from . import {nombre_modulo}")
            modulos[nombre_modulo] = eval(nombre_modulo)
        except Exception as e:
            print(f"Error al importar {nombre_modulo}: {e}")
