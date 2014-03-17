#!/usr/bin/python
# -*- coding: cp1252 -*-

#-*- coding:utf-8 -*-

# Emerson Potes Rua, cc 98764868


#Punto 1
def PolyEval(c, x):
    n = len(c); p = 0
    for i in range(n):
        p += c[i]*(x**i)
    return p

#Punto 2:

# 2.1 Metodo de Horn - Iterativo
def HornerIt(c, x):
    n = len(c); b = c[n-1]
    for i in range(n-1, 0, -1):
        b = c[i-1] + x*b
    return b

# 2.2 Metodo de Horn - Recursivo
def HornerRec(c, x):
    n = len(c); 
    if (n > 1):
        b = c[0] + x*HornerRec(c[1:], x)
    elif (n == 1):
        b = c[0]
    return b

#Punto 3
def PolyDeriv(c):
    n = len(c); c2 = [];
    for i in range(n):
        if (i > 0): c2.append(i*c[i])    
    return c2

#Punto 4: Bisección
def Biseccion(c, a, b, e):
    fa = HornerIt(c, a) # f(a)
    fb = HornerIt(c, b) # f(b)
    if (fa * fb < 0):
        p = (a + b) / 2.0
        fp = HornerIt(c, p) # f(p)
        while (b - a > e or abs(fp) > e):
            fa = HornerIt(c, a)
            p = (a + b) / 2.0
            fp = HornerIt(c, p)
            if (fa * fp <= 0):
                b = p
            else:
                a = p
        return p
    elif (len(c) == 3 and c[1]**2-4*c[2]*c[0] == 0):
        return "El polinomio no se puede resolver por biseccion"
    elif (len(c) == 3 and c[1]**2-4*c[2]*c[0] < 0):
        return "El polinomio no tiene solucion en los reales"
    else:
        return "El intervalo [{},{}] NO contiene un cero real de f(x) o no se puede resolver".format(a, b)
    
def PolyCeros(c, e):
    n = len(c); x = [] # Arreglo de ceros reales de f(x)
    if (n > 2):
        k = 0
        for i in c[:len(c)-1]:
            k += abs(i)
        M = max(2.0 * float(k)/abs(c[len(c)-1]), 1)
        c2 = PolyDeriv(c)
        y = PolyCeros(c2, e)
        if (len(y) >= 1):
            aux = y
            aux.insert(0, -M)
            aux.insert(len(aux), M)
            for i in range(len(aux)-1):
                x.append(Biseccion(c, aux[i], aux[i+1], e))
    elif (n == 2):
        x.append(-float(c[0])/c[1])
    return x

#Punto 5: Newton-Raphson
def Newton(c, x0, e, N0):
    if (len(c) == 3 and c[1]**2-4*c[2]*c[0] == 0):
        xk_1 = "El polinomio no se puede resolver por Newton"
    elif (len(c) == 3 and c[1]**2-4*c[2]*c[0] < 0):
        xk_1 = "El polinomio no tiene solucion en los reales"
    else:
        k = 0; xk = x0; xk_1 = 0; roots = []
        #print xk
        dif, fxk = e, e # con estos valores garantizo la primera iteración
        while (dif >= e or abs(fxk) >= e):
            if (k <= N0):
                fxk = HornerIt(c, xk) # f(xk)
                c2 = PolyDeriv(c); c3 = PolyDeriv(c2)
                fc2 = HornerIt(c2, xk) # f'(xk)
                fc3 = HornerIt(c3, xk) # f''(xk)
                if (fc2 != 0):
                    if (fxk == 0):
                        break
                    else:
                        #xk_1 = xk - (float(fxk)/fc2) # xk+1 -> k+1 subindice; Metodo Normal
                        xk_1 = xk - ((float(fxk)*fc2)/(fc2**2-fxk*fc3)) # xk+1 -> k+1 subindice; Metodo Modificado
                        dif = abs(xk_1 - xk)
                        xk = xk_1
                else:
                    xk_1 = "Error: division por cero"
                    break
            else:
                break
            #print xk_1
            k += 1
    return xk_1

def PolyCerosN(c, e):
    n = len(c); x = [] # Arreglo de ceros reales de f(x)
    if (n > 2):
        k = 0
        for i in c[:len(c)-1]:
            k += abs(i)
        M = max(2.0 * float(k)/abs(c[len(c)-1]), 1)
        x.append(Newton(c, -M, e, 100))
        x.append(Newton(c, M, e, 100))
    elif (n == 2):
        x.append(-float(c[0])/c[1])
    return x

if __name__ == "__main__":
    c = [-12, 1, 1] # El orden de c es desde a0 hasta an siendo 'a' los coeficientes del polinomio
    
    #x = 197
    #print PolyEval(c,x)
    #print HornerIt(c, x)
    #print HornerRec(c, x)
    #print PolyDeriv(c)
    #print Biseccion(c, 0, 3, 0.01)
    #print PolyCeros(c, 0.01)
    #print Newton(c, 13, 0.01, 10)
    print PolyCerosN(c, 0.01) # Para polinomios de 2do. grado

