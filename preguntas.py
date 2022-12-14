"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from audioop import maxpp
from operator import itemgetter


with open("data.csv", "r") as file:
    data = file.readlines()

newdata = data

newdata = [line.replace("\n", "") for line in newdata]

newdata = [line.split("\t") for line in newdata]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    a = 0
    for z in newdata[0:]:
        a += int(z[1])
    return a

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    a = [z[0] for z in newdata[0:]]
    b = sorted(list(set(a)))
    aa = []
    for i in b:
        aa.append(a.count(i))

    z = list(zip(b, aa))
    
    return z


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    a = [z[0] for z in newdata[0:]]
    a = sorted(list(set(a)))

    ac = []
    for i in a:
        w = [int(z[1]) for z in newdata[0:] if z[0] == i]
        ac.append(sum(w))

    ac = list(zip(a,ac))
    return ac

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    a = [z[2].split("-") for z in newdata[0:]]
    b = sorted(list(set([z[1] for z in a])))

    ac = []

    for i in b:
        w = ([z for z in a if z[1] == i])
        ac.append(len(w))

    ac = list(zip(b,ac))

    return ac

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    a = [z[0] for z in newdata[0:]]
    a = sorted(list(set(a)))

    maxi = []
    mini = []
    for i in a:
        w = [int(z[1]) for z in newdata[0:] if z[0] == i]
        maxi.append(max(w))
        mini.append(min(w))

    ac = list(zip(a,maxi,mini))
    return ac

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [data[4].split(",") for data in x]
    valores = []
    for diccionario in x:
        [valores.append(valor) for valor in diccionario]
    x = [(valor.split(":")[0],int(valor.split(":")[1])) for valor in valores]
    x = sorted(x)
    tuples = []
    previous_key = None
    acum = 0
    i = 0
    nums = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key,minimo,maximo))
            previous_key = key
            nums = []
            nums.append(value)
        else:
            nums.append(value)
        i += 1
        if i == len(x):
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key,minimo,maximo))
            break
    return tuples

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(int(data[1]),data[0]) for data in x]
    x = sorted(x, key=itemgetter(0))
    tuples = []
    previous_key = None
    acum = 0
    i = 0
    letras = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key,letras))
            previous_key = key
            letras = []
            letras.append(value)
        else:
            letras.append(value)
        i += 1
        if i == len(x):
            tuples.append((previous_key,letras))
            break
    return tuples

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(int(data[1]),data[0]) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    acum = 0
    i = 0
    letras = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key,sorted(set(letras))))
            previous_key = key
            letras = []
            letras.append(value)
        else:
            letras.append(value)
        i += 1
        if i == len(x):
            tuples.append((previous_key,sorted(set(letras))))
            break
    return tuples


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open('data.csv') as file:
        data = file.readlines()
        data = [x.strip().split('\t')[-1] for x in data]
        data = ','.join(data).split(',')
        data = [x.split(':')[0] for x in data]
        strings = sorted(list(set(data)))
        res = dict()
        
        for i in strings:
            res[i] = data.count(i)

    return res


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv') as file:
        data = file.readlines()
        data = [x.strip().split('\t') for x in data]
        
        for i in data:
            i.pop(1)
            i.pop(1)
            i[1] = len(i[1].split(','))
            i[2] = len(i[2].split(','))
            
        res = [tuple(x) for x in data]
    return res



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv') as file:
        
        data = file.readlines()
        aux = data.copy()
        data = [x.strip().split('\t')[3] for x in data]
        data = ','.join(data).split(',')
        l = sorted(list(set(data)))
        aux = [x.strip().split('\t') for x in aux]
        res = dict()
        
        for i in l:
            acum = 0
            for j in aux:
                if i in j[3]:
                    acum += int(j[1])
            res[i] = acum
            
    return res



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv') as file:
        
        data = file.readlines()
        data = [x.strip().split('\t') for x in data]
        listaux = list()
        
        for i in data:
            for j in range(3):
                i.pop(1)
            i[1] = i[1].split(',')
            
        valores = [x[1] for x in data]
        
        for j in valores:
            lista = sum([int(x.split(':').pop(1)) for x in j])
            listaux.append(lista)
            
        for k in range(len(data)):
            data[k].append(listaux[k])
            data[k].pop(1)
            
        l = [x[0] for x in data]
        l = sorted(list(set(l)))
        res = dict()
        
        for i in l:
            acum = 0
            for j in data:
                if j[0] == i:
                    acum += j[1]
            res[i] = acum
            
    return res

print(pregunta_12())