"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from pregunta_01 import read_dataset

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data = read_dataset("files/input/data.csv")
    sums = {}

    for row in data:
        value = int(row[1])
        letras = row[3].split(',')
        for letra in letras:
            sums[letra] = sums.get(letra, 0) + value

    return dict(sorted(sums.items()))

print(pregunta_11())
