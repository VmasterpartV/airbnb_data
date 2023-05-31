# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:37:10 2023

@author: ivan_
"""

import pandas as pd
from collections import Counter
import re

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

df = pd.read_csv(archivo)

# Convierte la columna 'amenities' a minúsculas
df['amenities'] = df['amenities'].str.lower()

# Remueve los caracteres "?" de la columna 'amenities'
df['amenities'] = df['amenities'].apply(lambda x: re.sub(r'\?', '', x))

# Crea una lista con todas las palabras en la columna 'amenities'
all_amenities = [amenities.split(", ") for amenities in df['amenities']]
flat_amenities = [amenity for sublist in all_amenities for amenity in sublist]

# Calcula la frecuencia de cada amenidad
amenity_counts = Counter(flat_amenities)

# Imprime las 10 amenidades más comunes y su frecuencia
top_10_amenities = amenity_counts.most_common(10)
for amenity, count in top_10_amenities:
    print(f'{amenity}: {count}')