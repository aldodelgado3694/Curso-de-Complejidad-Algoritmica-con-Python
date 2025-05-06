# Que es esto?

Proyecto donde se recompilan los ejercicios para el Curso de Complejidad Algorítmica con Python, el proyecto se aborda desde un unico proyecto con los archivos separados por curso "Cx.py". 

## Caracteristicas

- Se creo en _ _init__.py con el codigo necesario para poder correr todos los modulos desde main.
- Se hace uso de diccionario de parametros para pasar parametro y no modificar el modulo ya hecho.
- En main encontrara comentado cada uno de los cofigos de ejmemplo y solo necesitaras ejecutra main.

## Empezar

1. Crear ambiente virtual

```sh
python -m venv venv # Crear ambiente
```

2. Instala requirements.txt 

```sh
source venv/bin/activate  #Activa ambiente
# En Windows: venv\Scripts\activate
```

3. Activa ambiante virtual 

```sh
pip install -r requirements.txt
```

4. Ejecuta el comando -h y disfruta

```sh
python main.py -h
```


- Debera regresar

```sh
usage: main.py [-h] [-m MODULO] [-t TAMAÑO] [-o OBJETIVO] [-i FECHAI] [-f FECHAF] [-v VALORES] [-p PESOS] [-n N]

options:
  -h, --help            show this help message and exit
  -m MODULO, --modulo MODULO
                        Nombre de modulo a ejecutar validos (c2, c6, c7, c8, c9, c10, c13exercice, c15)
  -t TAMAÑO, --tamaño TAMAÑO
                        Tamaño de la lista a ordenar valido en (c6, c7, c8, c9, c10, c15)
  -o OBJETIVO, --objetivo OBJETIVO
                        Objetivo de la lista a ordenar valido en (c6 y c7)
  -i FECHAI, --fechaI FECHAI
                        Fecha de inicio en formato YYYY-MM-DD valido en c13exercice
  -f FECHAF, --fechaF FECHAF
                        Fecha de fin en formato YYYY-MM-DD valido en c13exercice
  -v VALORES, --valores VALORES
                        Valores del morral valido en c15
  -p PESOS, --pesos PESOS
                        Pesos del morral valido en c15
  -n N, --n N           Numero de elementos a calcular en c2
```

## Ejemplos de uso

```python
modulos["c2"].run({"n":2000})
modulos["c6"].run({"tamaño": 10000, "objetivo": 50})
modulos["c7"].run({"tamaño": 10000, "objetivo": 50})
modulos["c8"].run({"tamaño": 1000000})
modulos["c9"].run({"tamaño": 20})
modulos["c10"].run({"tamaño": 5})
modulos["c13exercice"].run({"fechaIni": "2018-01-01", "fechaFin": "2025-05-06"})
modulos["c15"].run({"valores": [60, 100, 120], "pesos": [10, 20, 30], "tamaño": 50})
```