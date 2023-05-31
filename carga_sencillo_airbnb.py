# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:50:51 2023

@author: ivan_
"""

import pandas as pd

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="Listings_1.csv"
archivo=mainpath+filename
datatit = pd.read_csv(archivo)

print(datatit.head())
print("\n")
print(datatit)
print("\n")
print(datatit.columns.values)
print("\n")
print(datatit.isnull().sum())