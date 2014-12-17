# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 12:49:52 2014

@author: Johan
"""
import numpy 
import quicksort as quick
import random as alea

#a = [10, 2, 13, 24, 5]
a = [0]*10 # lista de 10 elementos inicialmente todos en cero
for i in range(10):
    a[i] = alea.randrange(100) # generando una lista con elementos aleatorios
    
b = quick.quicksort(a) # método Quicksort
print 'Lista inicial\t', a # muestra en pantalla de la lista inicial
print '\nLista final\t', b # muestra en pantalla de la lista después del método

