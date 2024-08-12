#import matplotlib.pyplot as plt
#import requests
#import json
#import openpyxl
import mod_data
import mod_estadistica


# Función para el menú
def menu():
    print("Menú:")
    print("1. Obtener datos de la API y guardarlos en un archivo JSON")
    print("2. Cargar datos desde un archivo JSON")
    print("3. Generar gráfico de datos")
    print("4. Guardar datos en un archivo Excel")
    print("5. Calcular estadísticas")
    print("6. Salir")

def main():
    data = None
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            data = mod_data.obtener_datos()
            if data:
                mod_data.guardar_datos_en_json(data, "covid_data.json")  # Se puede cambiar el nombre de archivo
        elif opcion == "2":
            data = mod_data.cargar_datos_desde_json("covid_data.json")  # Se puede cambiar el nombre de archivo
        elif opcion == "3":
          print("¿Que tipo de grafica quiere generar?\n")
          print("1. Lineal")
          print("2. Barras Vertical")
          print("3. Barras Horizontal")
          tipoG = int(input())
          if tipoG == 1:
            mod_estadistica.generar_grafico_lineal(data)
          elif tipoG == 2:
            mod_estadistica.generar_grafica_barras(data)
          elif tipoG == 3:
            mod_estadistica.generar_grafica_barras_horizontal(data)
          else:
            print("Opcion no valida")
        elif opcion == "4":
            mod_data.guardar_datos_en_excel(data, "covid_data.xlsx")  # Se puede cambiar el nombre de archivo
        elif opcion == "5":
            estadisticas = mod_estadistica.calcular_estadisticas(data)
            if estadisticas:
                for key, value in estadisticas.items():
                    print(f"{key}: {value}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()