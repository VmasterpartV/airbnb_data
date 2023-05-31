# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:25:59 2023

@author: ivan_
"""

import pandas as pd
import statistics as st

# Cargar el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "Listings_1.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Analisis de columnas del dataset
print(df.head(10))
print("\n")
print(df)
print("\n")
print(df.columns.values)
print("\n")
print(df.isnull().sum())
print("\n")

# Reemplazar valores nulos
print(df['city'].unique())

# Calcular medidas de tendencia central
# media=st.mean(df['price'])
# mediana=st.median(df['price'])
# moda=st.mode(df['price'])
# minimo=min(df['price'])
# maximo=max(df['price'])
# print('Media=',media)
# print('Mediana=',mediana)
# print('Moda=',moda)
# print('Minimo=',minimo)
# print('Maximo=',maximo)