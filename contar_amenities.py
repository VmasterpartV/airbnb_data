# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:10:31 2023

@author: ivan_
"""

import pandas as pd

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

df = pd.read_csv(archivo)

# Convierte la columna 'amenities' a minúsculas
df['amenities'] = df['amenities'].str.lower()

def calculate_percentage(df, word):
    total_options = len(df)
    word_options = df['amenities'].str.contains(word).sum()
    return round(word_options / total_options * 100, 2)

# Palabras a buscar y su descripción
words = {
    'wifi': 'Wifi',
    'tv': 'TV',
    'heating': 'Calefacción',
    'air conditioning': 'Aire acondicionado',
    'gym': 'Gimnasio',
    'kitchen': 'Cocina',
    'washer': 'Lavadora',
    'iron': 'Plancha',
    'refrigerator': 'Refrigerador',
    'hangers': 'Ganchos para ropa',
    'workspace': 'Espacio de trabajo',
    'hair dryer': 'Secadora de pelo',
    'hot water': 'Calentador de agua'
}

# Calcular el porcentaje para cada palabra
percentages = {description: calculate_percentage(df, word) for word, description in words.items()}

# Ordenar el diccionario por valores en orden descendente
sorted_percentages = sorted(percentages.items(), key=lambda x: x[1], reverse=True)

# Mostrar el resultado ordenado
for description, percentage in sorted_percentages:
    print(f'{percentage}% tienen {description}')