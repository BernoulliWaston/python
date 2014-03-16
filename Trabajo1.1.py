#!/usr/bin/python
#-*- coding:utf-8 -*-

# Emerson Potes Rua, cc 98764868

#Punto 1
def PolyEval(c, x):
    n = len(c); p = 0
    for i in range(n):
        p += c[i]*(x**i)
    return p


#Punto 2: Metodo de Horn - Iterativo
def HornerIt(c, x):
    n = len(c); b = c[n-1]
    for i in range(n-1, 0, -1):
        b = c[i-1] + x*b
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
    else:
        return "El intervalo [{},{}] NO contiene un cero real de f(x)".format(a, b)
    
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
    

if __name__ == "__main__":
    c = [-6, 14, -7, 1] # El orden de c es desde a0 hasta an siendo 'a' los coeficientes del polinomio
    
    #x = 2
    ##print PolyEval(c,x)
    #print HornerIt(c, x)
    #print PolyDeriv(c)
    
##    print "Metodo de Biseccion para c = %s \n"%str(c)
##    x = Biseccion(c, -3, 0, 0.01)
##    print "x = " + str(x)
##    if not isinstance(x, str): print "Prueba: " + str(HornerIt(c, x))

    print PolyCeros(c, 0.01)
    #print Biseccion(c, -10, 10, 0.01)
