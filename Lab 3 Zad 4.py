# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:01:02 2019

@author: ZUISA
"""

def f(x):
    return x**5-x+1



def pochodna(x):
    y=(f(x+(1/2)*iter)-f(x-(1/2)*iter))/iter
    return y


if(__name__=="__main__"):
    iter =0.0000001
    delta= 100
    x=0
    a=0.05
    b=0.95
    for k in range(1,delta):
        styczna=x-(f(x)/pochodna(x))
        print("x=",styczna)
        if(abs(styczna)<iter):
            
            break
    
            
    
