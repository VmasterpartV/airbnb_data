# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:21:24 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

df = pd.read_csv(archivo)

# Calcular el precio promedio por ciudad
precio_promedio_ciudad = df.groupby('city')['price_USD'].mean()

# Ordenar de mayor a menor
precio_promedio_ciudad = precio_promedio_ciudad.sort_values(ascending=False)

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(precio_promedio_ciudad.index, precio_promedio_ciudad.values)
plt.xlabel('Ciudad')
plt.ylabel('Precio Promedio (USD)')
plt.title('Precio Promedio de Alojamientos por Ciudad')

# Rotar las etiquetas del eje x para una mejor legibilidad si es necesario
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()

# Imprimir los resultados en consola
print(precio_promedio_ciudad)