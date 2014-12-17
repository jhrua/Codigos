# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 10:13:08 2014

@author: Johan
"""

## Aún es una versión preliminar del mètodo de indexación.
## Estoy deciciendo la estrategia para evitar al máximo el uso de ciclos


# Listas que al momento he usado.
Lista = []
cont = []

# Lista de prueba. Cada elemento a[i] es una lista.
a = [[1, 2, 3, 3], [2, 3, 3, 3, 4], [1, 2, 7, 7], [2, 3, 5, 5, 5, 7],
      [1, 5, 6, 7, 8, 10]] 

## Asignación de índices a la primera lista.
L = len(a)
Pl = a[0] # primera lista
for i in range(len(Pl)):
    Lista.append([Pl[i], i])
indice_max = i
print Lista
##

Nl = a[1] # segunda lista
lst = list(set(Nl)) # lista Nl sin elementos repetidos.
for i in range(len(lst)):
    cont.append(Nl.count(lst[i])) # repeticiones de cada elemento en la lista.
    if lst[i] in Pl:
        cont[i] 
    else:
        lista.append([lst[i],indice_max])
            
print lst
print cont

#print lpl 
