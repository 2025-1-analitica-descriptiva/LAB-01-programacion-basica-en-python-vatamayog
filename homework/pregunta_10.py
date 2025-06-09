"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from pregunta_01 import read_dataset

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    
    data = read_dataset("files/input/data.csv")
    result = []

    for row in data:
        letra = row[0]
        col4_count = len(row[3].split(','))
        col5_count = len(row[4].split(','))
        result.append((letra, col4_count, col5_count))

    return result

