# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:38:18 2023

@author: ivan_
"""

import pandas as pd

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="airbnb_limpio.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)

# Variables boolenas

# Calculamos la moda de la columna host_has_profile_pic
moda = df["host_has_profile_pic"].mode()[0]

# Sustituimos los valores nulos por la moda
df["host_has_profile_pic"].fillna(moda, inplace=True)

# Calculamos la moda de la columna host_is_superhost
moda = df["host_is_superhost"].mode()[0]

# Sustituimos los valores nulos por la moda
df["host_is_superhost"].fillna(moda, inplace=True)

# Calculamos la moda de la columna host_identity_verified
moda = df["host_identity_verified"].mode()[0]

# Sustituimos los valores nulos por la moda
df["host_identity_verified"].fillna(moda, inplace=True)

# Variables numéricas

# Calcular la mediana de host_total_listings_count
mediana = df['host_total_listings_count'].median()

# Reemplazar los valores nulos por la mediana
df['host_total_listings_count'] = df['host_total_listings_count'].fillna(mediana)

# Calcular la mediana
mediana = df['bedrooms'].median()

# Reemplazar los valores nulos por la mediana
df['bedrooms'] = df['bedrooms'].fillna(mediana)

# Guardar el csv con los nuevos valores

df.to_csv('airbnb_completo.csv', index=False)
