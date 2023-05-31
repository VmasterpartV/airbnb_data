# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:57:46 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import statistics as st


mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="Listings_1.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)

#medidas de tendencia central
media=st.mean(df['price'])
mediana=st.median(df['price'])
moda=st.mode(df['price'])
minimo=min(df['price'])
maximo=max(df['price'])
print('Media=',media)
print('Mediana=',mediana)
print('Moda=',moda)
print('Minimo=',minimo)
print('Maximo=',maximo)

#medidas de dospersión

varianza=st.pvariance(df['price'], mu=None)
print('varianza=',varianza)


#Retorna la desviación típica poblacional 

# desvstr=st.pstdev(df['price'], mu=None)
# print('desvstdr=',desvstr)



# plt.figure(figsize = (15,8))
# ax=sns.catplot(x="city", y="review_scores_rating", 
#             kind="box", sharey=False, data=df)
# plt.xticks(rotation = 90)
# plt.grid()
# plt.savefig('miboxplot.png')
# plt.show()

# Identificar los barrios más populares
# plt.figure(figsize=(10,6))
# sns.countplot(y='neighbourhood', data=df, order=df['neighbourhood'].value_counts().iloc[:10].index)
# plt.title('Los 10 barrios más populares')
# plt.xlabel('Número de listados')
# plt.ylabel('Barrio')
# plt.show()

# Identificar las ciudades más populares
plt.figure(figsize=(10,6))
sns.countplot(y='city', data=df, order=df['city'].value_counts().iloc[:10].index)
plt.title('Las 10 ciudades con más propiedades en renta')
plt.xlabel('Número de listados')
plt.ylabel('Ciudad')

# Añadir el número de listados en cada barra
for i, v in enumerate(df['city'].value_counts().iloc[:10]):
    plt.text(v, i, str(v), color='black')

plt.show()