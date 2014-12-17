# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 12:44:21 2014

@author: Johan
"""
import random as alea

def quicksort(S): # donde S es una lista
    ma = []    
    me = []
    ig = []
    L = len(S)
    if L <= 1:
        return S
    else:
        a = alea.randrange(L)
        ele = S[a] # elemento aleatorio en la lista
        for i in range(L):
            if S[i] > ele:
                ma.append([S[i]])
            elif S[i] < ele:
                me.append([S[i]])
            else:
                ig.append([S[i]])
        return quicksort(me), ig, quicksort(ma)
        