# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np



#x = np.array( [ 3.5, 7.0, 1.5, 4.0 ] )[None, :] 
#F = np.array( [ 4.3, 1.9, 15.3, 20.0 ] )[:, None] 


x = np.array( [ 2.55, 8.3, 1.5, 5.2 ] )[None, :] 
F = np.array( [ 3.32, 8.97, 15.3, 11.6 ] )[:, None] 

B = np.zeros((2, x.shape[1]))
B[0, :] = x**0

B[1, :] = x**1
B=np.transpose(B)
##
##
##a = np.dot(np.linalg.inv(np.dot(B,np.transpose(B))),np.dot(B,F))
##P = a[0] + a[1]*x 
##E = np.sum( (F - np.transpose(P))**2 ) 
##print("P:",P)
##print("E:",E)
##print("B:",B)


print(B)
