import numpy as np
from  pylab import *
from scipy import  *
import matplotlib.pyplot as plt
 

def f(x):                                          
    y=-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2
    return y

def df(x):                                          
    t=(f(x+dx1)-f(x))/dx1
    return t

def ddf(x):                                          
    return df(x+dx1)-df(x)/dx1

def wykresy(a,b,dx,title,x0):
     x0=x0   
     x=np.arange(a,b,dx1)
     print(title)
     prog(dx)
     reg(x0,dx)
     cent(x0,dx)
     plt.title(title)
     plt.plot(x,f(x),"-",x,df(x),"--",x,ddf(x),":")
     plt.show()

def prog(dx):                       
    print("Progresywny: ",(f(x0)+df(x0)*dx-f(x0))/dx  )          

def reg(dx0,dx):                        
    print("Regresywn: ",(f(x0)-(f(x0)-df(x0)*dx))/dx)

def cent(x0,dx):                         
    print("Centralny ",(f(x0)+df(x0)*dx-(f(x0)-df(x0)*dx))/(2*dx))


if(__name__=="__main__"):
    x0=0.5
    a=-10
    b=10
    dx1=0.5
    dx2=0.25
    dx3=0.3
    dx4=6
    title="Krok= 0.5"
    wykresy(a,b,dx1,title,x0)
    title="Krok= 0.25"
    wykresy(a,b,dx2,title,x0)
    title="Krok= 0.3"
    wykresy(a,b,dx3,title,x0)
    title="Krok= 6"
    wykresy(a,b,dx4,title,x0)

    
