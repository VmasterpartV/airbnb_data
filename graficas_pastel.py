# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:01:33 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename
df = pd.read_csv(archivo)

# Crea una función para generar las gráficas de torta o dona
def generar_grafica_torta(datos, titulo):
    plt.figure(figsize=(8, 6))
    plt.pie(datos.values, labels=datos.index, autopct='%1.1f%%', startangle=90)
    circle = plt.Circle((0, 0), 0.6, color='white')
    plt.gca().add_artist(circle)
    plt.title(titulo)
    plt.axis('equal')
    plt.show()

# Genera las gráficas de torta o dona para las variables requeridas
variables = ["host_is_superhost", "host_identity_verified", "host_has_profile_pic", "instant_bookable"]
titulos = ["Proporción de Propiedades por Superhost",
           "Proporción de Propiedades por Verificación de Identidad",
           "Proporción de Propiedades por Perfil de Anfitrión con Foto",
           "Proporción de Propiedades por Reserva Instantánea"]

for variable, titulo in zip(variables, titulos):
    datos = df[variable].value_counts()
    generar_grafica_torta(datos, titulo)