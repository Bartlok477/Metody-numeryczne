
"""
Created on Wed Nov 20 12:30:54 2019

@author: ZUISA
"""

import math 


def f(x):
    y=(pow(math.e,-5*x)-1/4)
    return y



##def f(x):
##    y=(-pow(math.e,-5*x)+1/4)
##    return y
##
##def f(x):
##    y=((pow(math.e,5*x)/100)+1/2)
##    return y


a=0.05
b=0.95
iter=1000
delta=0.001

for k in range(1,iter):
    #print (k)
    x=a-(f(a)/(f(b)-f(a))*(b-a))
    if(abs(f(x))<delta):
        break
    else:
        if(f(a)*f(x)>0):
            a=x
        else:
            b=x
print ("a= ",a," b=",b)










##
##




