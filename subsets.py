# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:54:42 2023

@author: ivan_
"""

import pandas as pd

# Lee el archivo csv y crea un DataFrame
# Cargar el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_limpio.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# subset = df[(df['city'] == 'Paris') & (df['neighbourhood'] == 'Buttes-Montmartre')]
# subset = df[df['price_USD'] < 25]
# subset = df[(df['price_USD'] < 25) & (df['accommodates'] >= 4)]
subset = df[df['host_id'] == 370550979]

subset.to_csv('soloHost_370550979.csv', index=False)