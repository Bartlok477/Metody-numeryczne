# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:12:39 2020

@author: ZUISA
"""

import numpy as np 
import scipy.integrate as integ
a,b=integ.quad(lambda x: -0.1*x**4-0.15*x**3-0.5*x**2+1.2,0,10)
print("pole= ",abs(a))
print("błąd= ",b)