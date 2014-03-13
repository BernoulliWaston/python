#!/usr/bin/python
#-*- coding:utf-8 -*-

def partition1(X, a, b, p):
    i = a; j = b; c = a + 1; Y = []
    for k in X: Y.append(0)
    while (c <= b):
        if (X[c] < X[p]):
            Y[i] = X[c]
            i += 1
        else:
            Y[j] = X[c]
            j -= 1
        print Y
        c += 1
    Y[i] = X[p]
    print Y
    print "pos pivote: " + str(i)
    return i

def quickSort(X, a, b):
    v = 0
    p = partition1(X, a, b, v)
    quickSort(X, a, p-1)
    quickSort(X, p+1, b)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
if __name__ == "__main__":
    print factorial(4)
##    X = [4, 7, 1, 6, 8, 3, 5, 2]
##    print X
##    a = 0; b = len(X)-1; p = 0
##    #quickSort(X, a, b)
##    #print partition1(X, a, b, p)
