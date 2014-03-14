#!/usr/bin/python
#-*- coding:utf-8 -*-
import random

def partition1(X, a, b):
    i = a; j = b; c = a + 1; Y = []
    p = random.randint(0, n-1)
    pivote = X[p]
    print "Pivote Seleccionado: " + str(pivote) + "\n"
    if (X[0] != pivote):
        i0 = X[0]
        X[0] = pivote
        X[p] = i0
    print "Arreglo con pivote en posicion 0: " + str(X)
    for k in X: Y.append(0)
    while (c <= b):
        if (X[c] < pivote):
            Y[i] = X[c]
            i += 1
        else:
            Y[j] = X[c]
            j -= 1
        print Y
        c += 1
    Y[i] = pivote
    print Y
    return [Y, i]

def quickSort(X, a, b):
    v = 0
    if (b > 1):
        p = partition1(X, a, b, v)
        quickSort(X, a, p-1)
        quickSort(X, p+1, b)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
if __name__ == "__main__":
##    print factorial(4)
    X = [4, 7, 2, 6, 8, 3, 5, 1]
    print "Arreglo Principal:" + str(X) + "\n"
    a = 0; b0 = len(X)-1
    #quickSort(X, a, b)
    #print partition1(X, a, b, p)
    print "Posicionando Pivote"
    vect = partition1(X, a, b0)
    Y = vect[0]
    b = vect[1]
    suba1 = Y[0:b];  suba2 = Y[b+1:]
    print "\nPosicionando pivote subarreglo 1:" + str(suba1)
    vect1 = partition1(suba1, a, len(suba1)-1)
    print "\nPosicionando pivote subarreglo 2:" + str(suba2)
    vect2 = partition1(suba2, a, len(suba2)-1)
