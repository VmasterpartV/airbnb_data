# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:28:48 2023

@author: ivan_
"""

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

mainpath="C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename="Listings_1.csv"
archivo=mainpath+filename

df = pd.read_csv(archivo)


sns.lmplot( x="review_scores_rating", y="price", data=df, fit_reg=False, hue='city', legend=False)
 
# Move the legend to an empty part of the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()