# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:16:16 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

df = pd.read_csv(archivo)

# Obtener el conteo de alojamientos por ciudad
conteo_por_ciudad = df['city'].value_counts()

# Crear la gráfica de embudo
plt.figure(figsize=(8, 6))
plt.barh(conteo_por_ciudad.index, conteo_por_ciudad.values)
plt.xlabel('Cantidad de Alojamientos')
plt.ylabel('Ciudad')
plt.title('Conteo de Alojamientos por Ciudad')

# Mostrar el gráfico
plt.show()

print(conteo_por_ciudad)