import numpy as np
import math

a=np.array([[0,2,2],
    [3,3,0],
    [1,0,1]])
#^macierz x
b=np.array([1,3,2])
#^macierz wyników



def sprawdzenie(a):
     if(np.linalg.det(a)==0):
          return False
     else:
          return True
#^sprawdzenie czy macierz jest osobliwa
def zamiana_tablic(a,b):
     n=len(a)
     z=([[0 for col in range(n+1)] for row in range(n)])
     #^generowanie tablicy z samymi zerami
     #Przeniesienie tablicy a do z
     for i in range(n):
          for k in range(n):
               z[k][i]=a[k][i]

     
     n=len(z)
     
     
     for j in range(n):
          z[j][n]=b[j]
    
     
     return z
     

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
     x =( [0 for i in range(n)])
     #xn,xn-1,
     for i in range(n-1,-1,-1):
          x[i]=c[i][n]/c[i][i]
          for k in range(i-1, -1, -1):
            c[k][n] -= c[k][i] * x[i]
     return x


if(__name__=="__main__"):
     if(sprawdzenie(a)==True):
          print("Macierz jest nieosobliwa ,trwa obliczanie")
          z=zamiana_tablic(a,b)
          
          zerowanie(z)
          print("Wynik=", gauss(z))

          
     elif(sprawdzenie(a)==False):
          print("Macierz jest osobliwa")
