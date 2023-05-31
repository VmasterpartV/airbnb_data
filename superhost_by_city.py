# -*- coding: utf-8 -*-
"""
Created on Wed May 31 02:30:09 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Elimina las filas duplicadas basadas en el host_id
df_unique = df.drop_duplicates(subset='host_id')

# Filtra los datos para obtener solo las columnas necesarias
df_filtered = df_unique[['host_is_superhost', 'city']]

# Agrupa los datos por ciudad y tipo de superhost
df_grouped = df_filtered.groupby(['city', 'host_is_superhost']).size().unstack().fillna(0)

# Guarda los datos en un nuevo archivo CSV
csv_filename = "resultados.csv"
df_grouped.to_csv(csv_filename)

# Genera la gráfica de barras agrupadas
ciudades = df_grouped.index
num_categorias = len(df_grouped.columns)
ancho_barras = 0.35
posicion_barras = range(len(ciudades))

fig, ax = plt.subplots(figsize=(12, 6))
for i, col in enumerate(df_grouped.columns):
    ax.bar(posicion_barras, df_grouped[col], width=ancho_barras, label=col)
    posicion_barras = [x + ancho_barras for x in posicion_barras]

ax.set_xticks(range(len(ciudades)))
ax.set_xticklabels(ciudades)
ax.set_title('Número de Superhost y No Superhost por Ciudad')
ax.set_xlabel('Ciudad')
ax.set_ylabel('Cantidad')
ax.legend(['No Superhost', 'Superhost'])

plt.show()
