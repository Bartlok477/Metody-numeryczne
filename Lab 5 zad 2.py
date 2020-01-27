
import numpy as np
from scipy import  *
import matplotlib.pyplot as plt
from pylab import *

def f(x):                                           
    tmp=-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2
    return tmp

def c(x):
     tmp=(f(x+dx)-f(x))/dx
     return tmp



def prog(f,a,x0,dx):                       
    return (f(x0)+c(x0)*dx-f(x0))/dx            

def reg(f,a,x0,dx):                        
    return (f(x0)-(f(x0)-c(x0)*dx))/dx

def cent(f,a,x0,dx):                         
    return (f(x0)+c(x0)*dx-(f(x0)-c(x0)*dx))/(2*dx)


if(__name__=="__main__"):
     a=-10.0                                               
     b=10.0
     dx=0.5                                              
     x0=0.5                                             

     x=np.arange(a,b,dx)                                 
     f1=f(x)
     f2=c(x)

     tmp=-0.4*x**3-0.45*x**2-x-0.25  
     
     pro=prog(f,a,x0,dx)
     re=reg(f,a,x0,dx)
     ce=cent(f,a,x0,dx)
                                           
     plt.plot(x,f1,"-",x,f2,"--",x,tmp,pro,"o",re,"x",ce,"w")
     plt.legend(["funkcja","obliczona","recznie liczone","ilorazy "])
     plt.show()
