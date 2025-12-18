
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos
    df = pd.read_csv("epa-sea-level.csv")

    # Crear gráfico de dispersión
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color='blue')

    # Primera línea de regresión: todos los años
    slope, intercept, *_ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(int(df["Year"].min()), 2051))
    line_all = slope * years_all + intercept
    plt.plot(years_all, line_all, 'r', label='Fit: All years')

    # Segunda línea de regresión: desde 2000
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_recent, 'green', label='Fit: From 2000')

    # Etiquetas, título y leyenda
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Guardar imagen
    plt.savefig("sea_level_plot.png")
    return plt.gca()  # Devuelve el gráfico para pruebas unitarias

# Para poder ejecutar directamente
if __name__ == "__main__":
    draw_plot()
    plt.show()
