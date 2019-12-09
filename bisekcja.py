# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import*
import numpy as np
from matplotlib.pyplot import*
def f(x):
    "Definicja funkcji"
    return x**2+x-1

#metoda bisekcji
iter=100
delta=0.00001
a=0.05
b=0.95
for k in range(1,iter):
    x=(a+b)/2
    if abs(f(x))<delta:
        break
    else:
        if f(x)*f(a)<0:
            b=x
        else:
            a=x
            
print(a)
print(b)
x=arange(0.05,0.95,0.00001)
plot(x,f(x))
grid(True)

