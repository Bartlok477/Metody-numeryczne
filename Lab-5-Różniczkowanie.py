# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:13:40 2019

@author: ZUISA
"""

import matplotlib.pyplot as plt

from pylab import *




def f(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2



def df(x):
    return -0.4*x**3-0.45*x**2-x-0.25

def ddf(x):
    return -1.2*x**2-0.9*x-1




x=arange(-10,10,0.1)
y1=f(x)
y2=df(x)
y3=ddf(x)
y4=df(0.5)
    
plt.plot(x,y1,"-",x,y2,"--",x,y3,":",0.5,y4,"o")
plt.legend(["f(x)","f'(x)","f''(x)","f'(0.5)"])
plt.show()







