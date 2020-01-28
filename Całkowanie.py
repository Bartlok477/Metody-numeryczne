# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:09:55 2020

@author: ZUISA
"""


import matplotlib.pyplot as plt 
import math
import numpy as np


def f(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2+1.2



def lewy_prostokat(a,b):
    return(b-a)*f(a)
    
def srodkowy_prostokat(a,b):
    x0=(a+b)/2
    return(b-a)*f(x0)
    
def prawy_prostokat(a,b):
    return(b-a)*f(b)
    
def trapez(a,b):
    return ((b-a)/2)*(f(a)+f(b))
    

a=0
b=10
x=np.arange(-100,100,0.1)



lew=lewy_prostokat(a,b)

srod=srodkowy_prostokat(a,b)

praw=prawy_prostokat(a,b)



print(abs(lew),abs(srod ),abs(praw))
plt.plot(x,f(x),"--",a,lew,"o",(a+b)/2,srod,"o",b,praw,"o")
plt.legend(["wykres","lewy","srod","prawy"])
plt.show()