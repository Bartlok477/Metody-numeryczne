# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:15:12 2019

@author: ZUISA
"""
import matplotlib.pyplot as plt
import numpy as np
import math 


def f(x):
    return x**2

#def f(x):
#    return -x**3+5*x
    
#def f(x):
#    return -x**3+2*x**2-x+5


#def f(x):
#    return x**3-3*x+8
    

x = np.array( [ 1, 2, 3,4, 5, 6 ] )[None, :]
F = np.transpose( f(x) )
# funkcja interpolujaca (n = m = 3) P = a0 + a1*x + a2*x^2
# a = [a0 a1 a2]^T
# p = [1 x x^2]

B = np.zeros((x.shape[1], x.shape[1]))
B[0, :] = x**0
B[1, :] = x**1
B[2, :] = x**2
B[3, :] = x**3
B[4, :] = x**4
B[5, :] = x**5

# a = ((B*B')^(-1)) * B*F
# a = np.dot( np.linalg.inv( np.dot( B, np.transpose(B) ) ), np.dot(B, F))
# a = ((B')^(-1)) * F   # zapis uproszczony (mozliwy bo B jest macierza kwadratowa)
a = np.dot( np.linalg.inv( np.transpose(B) ), F )
# funkcja interpolujaca w postaci wielomianu
p = np.poly1d( np.squeeze( np.fliplr(np.transpose(a)) ) )


# wspolczynniki wielomianu interpolacyjnego
for idx, val in enumerate(a):
    print('a[%d] = %g' % (idx, val))
print(p)
plt.plot(p,"red")
