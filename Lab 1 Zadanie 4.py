# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:14:49 2019

@author: ZUISA
"""

from matplotlib import *
import numpy as np 


x=np.array([[ 2, 3],[1,1]])
wyznacznik1=np.linalg.det(x)

print("Wyznacznik nr 1 : \n",wyznacznik1)


y=np.array([[ 2, 3,2],[1,4,3],[1,2,6]])

wyznacznik2=np.linalg.det(y)

print("Wyznacznik nr 1 : \n",wyznacznik2)
