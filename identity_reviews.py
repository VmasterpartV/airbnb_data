# -*- coding: utf-8 -*-
"""
Created on Wed May 31 01:06:40 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
# Ruta del archivo CSV de reseñas
filename_reviews = mainpath + "reviews.csv"
filename_listings = mainpath + "airbnb_completo.csv"

# Leer los archivos CSV de reseñas y listados
df_reviews = pd.read_csv(filename_reviews)
df_listings = pd.read_csv(filename_listings)

# Filtrar solo las columnas necesarias
df_reviews = df_reviews[['listing_id']]
df_listings = df_listings[['listing_id', 'host_identity_verified']]

# Combinar los DataFrames de reseñas y listados por el ID de la propiedad (listing_id)
df_merged = pd.merge(df_reviews, df_listings, left_on='listing_id', right_on='listing_id')

# Calcular el número de reseñas por propiedad
df_grouped = df_merged.groupby('listing_id').size().reset_index(name='review_count')

# Agregar la información de superhost a cada propiedad
df_merged = pd.merge(df_grouped, df_listings, left_on='listing_id', right_on='listing_id')

# Calcular el número promedio de reseñas por tipo de anfitrión
df_avg_reviews = df_merged.groupby('host_identity_verified')['review_count'].mean().reset_index(name='average_reviews')

# Graficar el número promedio de reseñas por tipo de anfitrión
fig, ax = plt.subplots(figsize=(8, 6))

# Crear un gráfico de barras
ax.bar(df_avg_reviews['host_identity_verified'], df_avg_reviews['average_reviews'])

# Personalizar el gráfico
ax.set_xlabel('Superhost')
ax.set_ylabel('Número Promedio de Reseñas')
ax.set_title('Impacto de la identidad verificada en las Reseñas')

# Mostrar el gráfico
plt.show()

print(df_avg_reviews)