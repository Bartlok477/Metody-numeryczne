import numpy as np
import math


#c=np.array([[10,40,70],
 #          [20,50,80],
  #         [30,60,80]])

#b=np.array([300,360,390])


c=np.array([[10,40,70,300],
          [20,50,80,360],
           [30,60,80,390]])

def zerowanie(c):
     n=len(c)
     for i in range(0, n):
          maxEl = abs(c[i][i])
          
          
          maxRow = i
          for k in range(i+1, n):
               if abs(c[k][i]) > maxEl:
                     maxEl = abs(c[k][i])
                     maxRow = k

             
          for k in range(i, n+1):
                 tmp = c[maxRow][k]
                 c[maxRow][k] = c[i][k]
                 c[i][k] = tmp

             
          for k in range(i+1, n):
               d = -c[k][i]/c[i][i]
               for j in range(i, n+1):
                    if i == j:
                         c[k][j] = 0
                    else:
                         c[k][j] += d * c[i][j]

def gauss(c):
     n=len(c)
     #tworzenie wyjsciowej tablicy 
     x = np.zeros((3,1))
     #xn,xn-1,
     for i in range(n-1,-1,-1):
          x[i]=c[i][n]/c[i][i]
          for k in range(i-1, -1, -1):
            c[k][n] -= c[k][i] * x[i]
     return x
     
if(__name__=="__main__"):
     print("Macierz startowa= \n",c)
     zerowanie(c)
     print("Macierz po zerowaniu= \n",c)
     print("Wynik=  \n",gauss(c))
     
     
               

