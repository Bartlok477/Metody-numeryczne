# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:01:02 2019

@author: ZUISA
"""

def f(x):
    return x**2+x-1



def pochodna(x):
    y=(f(x+(1/2)*iter)-f(x-(1/2)*iter))/iter
    return y

    iter =0.0000001
    delta= 100
    x=0.67
    a=0.05
    b=0.95
    for k in range(1,delta):
        styczna=x-(f(x)/pochodna(x))
        if(abs(styczna)<iter):
            print("x=",styczna)
            break
    
        

