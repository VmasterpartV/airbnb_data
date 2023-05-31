# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:28:39 2023

@author: ivan_
"""

import pandas as pd
from ast import literal_eval

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="airbnb_completo.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)

chunk_size = 10000
dummy_vars_list = []

count = 0

for chunk in pd.read_csv(archivo, chunksize=chunk_size):
    count = count + 1
    print('chunk ' + str(count))
    chunk['amenities'] = chunk['amenities'].apply(literal_eval)
    dummy_vars = pd.get_dummies(chunk['amenities'].apply(pd.Series).stack(), sparse=True).sum(level=0)
    dummy_vars_list.append(dummy_vars)

dummy_vars = pd.concat(dummy_vars_list, axis=0)
df = pd.read_csv(archivo)
df = pd.concat([df, dummy_vars], axis=1)

df.to_csv('dummies_nvo.csv', index=False)

print('generado')



