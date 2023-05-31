# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:36:43 2023

@author: ivan_
"""

import pandas as pd
from ast import literal_eval
from multiprocessing import Pool
import logging

mainpath = "C:/Users/ivan_/Documents/Escuela/8vo/Ciencia de datos/"
filename = "airbnb_completo.csv"
archivo = mainpath + filename

chunk_size = 10000

# Configurar el registro de mensajes
logging.basicConfig(level=logging.INFO)

# Función para procesar cada chunk en paralelo
def process_chunk(chunk):
    logging.info('Procesando un chunk')
    chunk['amenities'] = chunk['amenities'].apply(literal_eval)
    dummy_vars = pd.get_dummies(chunk['amenities'].apply(pd.Series).stack(), sparse=True).sum(level=0)
    return dummy_vars

print('Dividir el DataFrame en chunks')
# Dividir el DataFrame en chunks
chunks = pd.read_csv(archivo, chunksize=chunk_size)

print('Crear un pool de procesos')
# Crear un pool de procesos
pool = Pool()

print('Procesar los chunks en paralelo utilizando el pool de procesos')
# Procesar los chunks en paralelo utilizando el pool de procesos
dummy_vars_list = pool.map(process_chunk, chunks)

print('Cerrar el pool de procesos')
# Cerrar el pool de procesos
pool.close()
pool.join()

print('Concatenar las variables dummy de todos los chunks')
# Concatenar las variables dummy de todos los chunks
dummy_vars = pd.concat(dummy_vars_list, axis=0)

print('Leer el archivo original una vez más')
# Leer el archivo original una vez más
df = pd.read_csv(archivo)

print('Concatenar las variables dummy al DataFrame original')
# Concatenar las variables dummy al DataFrame original
df = pd.concat([df, dummy_vars], axis=1)

print('Guardar el DataFrame actualizado en un nuevo archivo CSV')
# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('dummies_nvo_multi.csv', index=False)

print('Generado')