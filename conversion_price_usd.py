# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:36:19 2023

@author: ivan_
"""

import pandas as pd

# Lee el archivo csv y crea un DataFrame
# Cargar el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "Listings_1.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 1.11

# Selecciona los registros que corresponden a Paris
paris = df[df['city'] == 'Paris']
rome = df[df['city'] == 'Rome']
paris_rome = pd.concat([paris, rome])

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
paris_rome['price_USD'] = paris_rome['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.052

# Selecciona los registros que corresponden a Paris
istambul = df[df['city'] == 'Istanbul']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
istambul['price_USD'] = istambul['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.67

# Selecciona los registros que corresponden a Paris
sydney = df[df['city'] == 'Sydney']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
sydney['price_USD'] = sydney['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.20

# Selecciona los registros que corresponden a Paris
rio = df[df['city'] == 'Rio de Janeiro']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
rio['price_USD'] = rio['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.029

# Selecciona los registros que corresponden a Paris
Bangkok = df[df['city'] == 'Bangkok']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
Bangkok['price_USD'] = Bangkok['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 1

# Selecciona los registros que corresponden a Paris
new_york = df[df['city'] == 'New York']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
new_york['price_USD'] = new_york['price'] * tipo_cambio



# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.13

# Selecciona los registros que corresponden a Paris
hong = df[df['city'] == 'Hong Kong']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
hong['price_USD'] = hong['price'] * tipo_cambio


# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.056

# Selecciona los registros que corresponden a Paris
mex = df[df['city'] == 'Mexico City']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
mex['price_USD'] = mex['price'] * tipo_cambio



# Define el tipo de cambio de dólar correspondiente a Paris
tipo_cambio = 0.055

# Selecciona los registros que corresponden a Paris
cape = df[df['city'] == 'Cape Town']

# Multiplica la columna 'price' por el tipo de cambio y crea una nueva columna 'price_USD'
cape['price_USD'] = cape['price'] * tipo_cambio


new_df = pd.concat([paris_rome, istambul, sydney, rio, Bangkok, new_york, hong, mex, cape])


# Guardar el archivo CSV con la nueva columna
new_df.to_csv('airbnb_usd.csv', index=False)