# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:08:13 2019

@author: ZUISA
"""
from pylab import*
import numpy as np
from matplotlib.pyplot import*
def f(x):
    "Definicja funkcji"
    return -x**2+x-0.2

#metoda bisekcji
iter=100
delta=0.00001
a=0.6
b=0.9
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
x=arange(0.6,0.9,0.00001)
plot(x,f(x),color='orange')
grid(True)
