# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:12:24 2019

@author: ZUISA
"""
def f1(x):
    return x**2+x-1
def f2(x):
    return -x**2+x-1/5


iter=200
delta=0.0000001
a=0.1
b=0.4


for k in range(1, iter):
    
    x=(a+b)/2
    if (abs(f2(x))<delta): 
        break
    else:
        if (f2(x)*f2(a)<0):
            b=x
           
        else:
            a=x
print(k)
print("a=",round(a,4))
print("b=",round(b,4))
print("x=",round(x,4))




