# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:16:16 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

df = pd.read_csv(archivo)

# Obtener el recuento de alojamientos por cada tipo de "room_type" por ciudad
alojamientos_por_tipo_ciudad = df.groupby('city')['room_type'].value_counts().unstack().fillna(0)

print(alojamientos_por_tipo_ciudad)

# Crear el gráfico de barras apiladas para cada ciudad
fig, ax = plt.subplots()

alojamientos_por_tipo_ciudad.plot(kind='bar', stacked=True, ax=ax)

# Configurar los ejes y el título del gráfico
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Alojamientos')
plt.title('Número de alojamientos por ciudad')
plt.legend()

# Mostrar el gráfico
plt.show()

# Crear el gráfico de barras agrupadas para cada ciudad
fig, ax = plt.subplots()

alojamientos_por_tipo_ciudad.plot(kind='bar', ax=ax)

# Configurar los ejes y el título del gráfico
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Alojamientos')
plt.title('Número de alojamientos por ciudad')
plt.legend()

# Mostrar el gráfico
plt.show()