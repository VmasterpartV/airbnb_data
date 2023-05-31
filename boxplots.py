# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:18:34 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="airbnb_limpio.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)

# # Graficar countplot de seaborn
# sns.boxplot(x='room_type', y='accommodates', data=df, showfliers = False)
# plt.show()

# Graficar countplot de seaborn
sns.boxplot(x='host_identity_verified', y='price_USD', data=df)
plt.show()

# # Graficar countplot de seaborn
# sns.boxplot(x='accommodates', y='bedrooms', data=df, showfliers = False)
# plt.show()

# # Graficar countplot de seaborn
# sns.boxplot(x='accommodates', y='bedrooms', data=df)
# plt.xticks(rotation=90)
# plt.show()

# # Crear el boxplot usando seaborn
# sns.boxplot(x="city", y="price_USD", data=df, showfliers = False)
# plt.xticks(rotation=90)
# plt.show()

# # Crear el boxplot usando seaborn
# sns.boxplot(x="room_type", y="price_USD", data=df)
# plt.xticks(rotation=90)
# plt.show()
