#!/usr/bin/python
#-*- coding:utf-8 -*-
from math import *

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
        if (i == 0):
            c2.append(0)
        else:
            c2.append(i*c[i])
    return c2
        
#Punto 4: Bisección
class bis:
    def __init__(self,f,a,b,e,maxiter):
       self.f = f.replace("x", "{}")
       self.a = a
       self.b = b
       self.e = float(e)
       self.maxiter = maxiter

    def eq(self, x):
        return eval(self.f.format(str(x),str(x)))
         
    def get_root(self):
        i = 1;
        while (i <= self.maxiter):
            p = (self.a + self.b) / 2.0
            if (abs(p) > self.e):
                fa = self.eq(self.a)
                fp = self.eq(p)
                if (fa * fp < 0):
                    self.b = p
                else:
                    self.a = p
            else:
                break
            return "x = " + str(p)
            """
            fa = self.eq(self.a)
            fp = self.eq(p)
            if (fa * fp < self.maxiter):
                return "x = " + str(p)
                break
            """
            i += 1

if __name__ == "__main__":
    c = [2, 1, 3] # 2 + x + 3x**2
    x = 2

    ##print PolyEval(c,x)
    ##print HornerIt(c, x)
    print PolyDeriv(c)
    ##print "Metodo de Biseccion.\n"
    ##print bis("x*sin(x)-1",0,2,0.5,10).get_root()
