import matplotlib.pyplot as plt
#modulos para generar archivos

#agregar solo statics para sacar media de que numero de casos se repitio mas


# Función para generar el gráfico
def generar_grafico(data):
    if data:
        dates = list(data['cases'].keys())
        cases = list(data['cases'].values())
        deaths = list(data['deaths'].values())
        recovered = list(data['recovered'].values())

        plt.figure(figsize=(12, 6))
        plt.plot(dates, cases, label='Casos', marker='o')
        plt.plot(dates, deaths, label='Muertes', marker='x')
        plt.plot(dates, recovered, label='Recuperados', marker='s')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad')
        plt.title('Evolución de casos, muertes y recuperados')
        plt.xticks(range(0, len(dates), 30), rotation=45)  # Mostrar una etiqueta por mes
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

# Función para realizar cálculos estadísticos
def calcular_estadisticas(data):
    if data:
        cases = list(data['cases'].values())
        deaths = list(data['deaths'].values())
        recovered = list(data['recovered'].values())
        total_cases = sum(cases)
        total_deaths = sum(deaths)
        total_recovered = sum(recovered)
        max_cases = max(cases)
        max_deaths = max(deaths)
        max_recovered = max(recovered)
        min_cases = min(cases)
        min_deaths = min(deaths)
        min_recovered = min(recovered)
        promedio_cases = total_cases / len(cases)
        promedio_deaths = total_deaths / len(deaths)
        promedio_recovered = total_recovered / len(recovered)
        
        return {
            "Total de casos": total_cases,
            "Total de muertes": total_deaths,
            "Total de recuperados": total_recovered,
            "Máximo de casos en un día": max_cases,
            "Máximo de muertes en un día": max_deaths,
            "Máximo de recuperados en un día": max_recovered,
            "Mínimo de casos en un día": min_cases,
            "Mínimo de muertes en un día": min_deaths,
            "Mínimo de recuperados en un día": min_recovered,
            "Promedio de casos por día": promedio_cases,
            "Promedio de muertes por día": promedio_deaths,
            "Promedio de recuperados por día": promedio_recovered
        }
    else:
        return None
