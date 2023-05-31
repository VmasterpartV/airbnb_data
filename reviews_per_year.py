# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:05:42 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename_airbnb = "airbnb_completo.csv"
filename_reviews = "reviews.csv"

# Lee los archivos CSV
df_airbnb = pd.read_csv(mainpath + filename_airbnb)
df_reviews = pd.read_csv(mainpath + filename_reviews)

# Fusiona los DataFrames por el listing_id
df_merged = pd.merge(df_airbnb, df_reviews, on='listing_id')

# Convierte la columna "date" en formato de fecha
df_merged['date'] = pd.to_datetime(df_merged['date'])

# Obtén el rango de fechas
fecha_min = df_merged['date'].min().date()
fecha_max = df_merged['date'].max().date()

# Cuenta el número total de reviews
num_reviews_total = df_merged.shape[0]

# Cuenta el número de reviewer_id sin contar repetidos
num_reviewers = df_merged['reviewer_id'].nunique()

# Agrupa los datos por ciudad, año y cuenta la cantidad de reviews
df_grouped = df_merged.groupby(['city', df_merged['date'].dt.year]).size().reset_index(name='review_count')

# Grafica la actividad de las reviews por ciudad durante el tiempo
fig, ax = plt.subplots(figsize=(12, 6))

# Recorre las ciudades y grafica una línea para cada una
for city in df_grouped['city'].unique():
    df_city = df_grouped[df_grouped['city'] == city]
    ax.plot(df_city['date'], df_city['review_count'], label=city)

# Personaliza el gráfico
ax.set_xlabel('Año')
ax.set_ylabel('Cantidad de Reviews')
ax.set_title('Actividad de Reviews por Ciudad')
ax.legend()

# Imprime el rango de fechas, el número total de reviews y el número de reviewers
print("Rango de fechas:", fecha_min, "a", fecha_max)
print("Número total de reviews:", num_reviews_total)
print("Número de reviewers únicos:", num_reviewers)

# Muestra el gráfico
plt.show()

# Reorganiza los datos con pivot
df_pivot = df_grouped.pivot(index='city', columns='date', values='review_count')

# Restablece el índice del DataFrame df_pivot
df_pivot = df_pivot.reset_index()

# Guarda el DataFrame df_pivot en un nuevo archivo CSV
output_filename = "reviews_actividad_ciudades.csv"
df_pivot.to_csv(output_filename, index=False)