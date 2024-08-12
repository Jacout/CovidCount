import requests
import json
import openpyxl
#modulo para guardar datos

# Función para obtener datos de la API
def obtener_datos():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("La solicitud no fue exitosa; Estado:", response.status_code)
        return None


# Función para guardar datos en un archivo Excel
def guardar_datos_en_excel(data, archivo):
    if data:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Fecha", "Casos", "Muertes", "Recuperados"])
        dates = list(data['cases'].keys())
        cases = list(data['cases'].values())
        deaths = list(data['deaths'].values())
        recovered = list(data['recovered'].values())
        for i in range(len(dates)):
            ws.append([dates[i], cases[i], deaths[i], recovered[i]])
        wb.save(archivo)
    
# Función para guardar datos en un archivo JSON
def guardar_datos_en_json(data, archivo):
    with open(archivo, "w") as file:
        json.dump(data, file)

# Función para cargar datos desde un archivo JSON
def cargar_datos_desde_json(archivo):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo no existe.")
        return None