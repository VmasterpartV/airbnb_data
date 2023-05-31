# -*- coding: utf-8 -*-
"""
Created on Wed May 31 02:08:34 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Filtra los datos para hosts que son superhost y tienen identidad verificada
superhost_verificado = df[(df['host_is_superhost'] == 't') & (df['host_identity_verified'] == 't')]

# Calcula el recuento de hosts con superhost e identidad verificada
recuento_superhost_verificado = superhost_verificado.shape[0]

# Calcula el recuento de hosts sin superhost o sin identidad verificada
recuento_no_superhost_verificado = df.shape[0] - recuento_superhost_verificado

# Genera la gráfica de pastel
datos = pd.Series([recuento_superhost_verificado, recuento_no_superhost_verificado], index=['Superhost e Identidad Verificada', 'No Cumplen Ambas Condiciones'])
plt.figure(figsize=(8, 6))
plt.pie(datos.values, labels=datos.index, autopct='%1.1f%%', startangle=90)
plt.title("Proporción de Hosts con Superhost e Identidad Verificada")
plt.axis('equal')
plt.show()