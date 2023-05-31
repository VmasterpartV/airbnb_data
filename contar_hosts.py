# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:38:45 2023

@author: ivan_
"""

import pandas as pd

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Cuenta el número de hosts únicos
cantidad_hosts = df['host_id'].nunique()

print("Cantidad de hosts:", cantidad_hosts)

# Obtiene el número de filas o registros
cantidad_registros = len(df)

print("Cantidad de alojamientos:", cantidad_registros)
