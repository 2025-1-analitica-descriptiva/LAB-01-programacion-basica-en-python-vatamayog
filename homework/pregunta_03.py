"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from pregunta_01 import read_dataset

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    data = read_dataset("files/input/data.csv")
    letter_sum = {}

    for row in data:
        letter = row[0]
        value = int(row[1])
        letter_sum[letter] = letter_sum.get(letter, 0) + value

    result = sorted(letter_sum.items())
    return result

