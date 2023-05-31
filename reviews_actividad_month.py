# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:31:22 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename_reviews = "reviews.csv"

# Lee el archivo CSV de reseñas
df_reviews = pd.read_csv(mainpath + filename_reviews)

# Convierte la columna "date" en formato de fecha
df_reviews['date'] = pd.to_datetime(df_reviews['date'])

# Agrupa los datos por mes y cuenta el número de reseñas
df_grouped = df_reviews.groupby(df_reviews['date'].dt.month).size().reset_index(name='review_count')

# Grafica la actividad de reseñas por mes de todos los años
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df_grouped['date'], df_grouped['review_count'])

# Personaliza el gráfico
ax.set_xlabel('Mes')
ax.set_ylabel('Número de Reseñas')
ax.set_title('Actividad de Reseñas por Mes (Todos los Años)')

# Muestra el gráfico
plt.show()

print(df_grouped)