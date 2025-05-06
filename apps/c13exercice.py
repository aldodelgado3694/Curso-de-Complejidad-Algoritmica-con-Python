#EJercicio.py

from bokeh.plotting import figure, output_file, show
from datetime import datetime
import requests
from requests.structures import CaseInsensitiveDict


#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main.py
def run(parameters):
    #parameters = {"fechaIni": "2018-01-01", "fechaFin": "2025-05-06"} # Parámetros de entrada si se usa __name__ == '__main__'
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/{parameters["fechaIni"]}/{parameters["fechaFin"]}' # "URL de la API"

    headers = CaseInsensitiveDict() # Estructura de datos para headers
    headers["Bmx-Token"] = "66439a32e1f8b6306c6167ef5bf96dfd2bb39abd15a015a15b89bd372976be34" # Token de acceso a la API 
    #Si quieres obtener tu propio token, ve a https://www.banxico.org.mx/SieAPIRest/service/v1/token
    
    resp = requests.get(url, headers=headers) # Realiza la solicitud GET a la API
    titulo = "" # Inicializa la variable titulo

    #inicializa Arrays para almacenar los datos
    xArray = []
    yArray = []
    if resp.status_code == 200: # Si la solicitud fue exitosa
        titulo = resp.json()["bmx"]["series"][0]["titulo"] # Extrae el título de la serie
        data = resp.json()["bmx"]["series"][0] # Convierte la respuesta a formato JSON retirando la parte innecesaria
        
        for item in data["datos"]:
            xArray.append(datetime.strptime(item["fecha"], '%d/%m/%Y')) # Extrae las fechas y se parsea a datetime para graficar datos serial
            yArray.append(item["dato"]) # Extrae el dato
    else:
        print(f"Error {resp.status_code} en la solicitud: {resp.reason}") # Imprime un mensaje de error si la solicitud falla

    output_file(f'dollar{parameters["fechaIni"]}{parameters["fechaFin"]}.html') # Crea un archivo HTML de salida
    
    fig = figure(x_axis_type='datetime', title=titulo) # Crea una figura con el tipo de eje x como fecha y el título de la serie
    fig.line(xArray, yArray, line_width=2)
    show(fig)