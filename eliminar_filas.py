# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:05:09 2023

@author: ivan_
"""

import pandas as pd

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="airbnb_limpio.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)

# Contar las filas con 10 o más columnas nulas
num_nulls = df.isnull().sum(axis=1)
num_rows_to_drop = sum(num_nulls >= 10)
print(f"Filas con 10 o más columnas nulas: {num_rows_to_drop}")

# Eliminar las filas con 10 o más columnas nulas
df = df[num_nulls < 10]

# Imprimir el número de filas y columnas en el DataFrame resultante
print(f"Número de filas: {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}")