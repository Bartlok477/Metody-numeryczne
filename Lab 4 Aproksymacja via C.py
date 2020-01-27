import matplotlib.pyplot as plt
import numpy as np

x = np.array( [ 2, 3, 4, 5 ] )[None, :] 
F = np.array( [ 3.32, 8.97, 15.3, 11.6 ] )[:, None] 

long=x.shape[1]

B=np.array([[0 for a in range(0,long)]for b in range(2,long)],dtype=float)

for a in range(0,long):
     B[0][a]=x[0][a]**0
     B[1][a]=x[0][a]**1
print(B)

def dot(Z,B):
     D=np.array([[0 for a in range(0,4)]for b in range(0,2)],dtype=float)
     
     for a in range(0,2):
          for b in range(0,4):
               for c in range(0,2):
                    D[a][b]+=Z[b][c]*B[c][a]
     print(D)
     print("A ",np.dot(Z,B))
def transpose(B):
     
     
     X=np.array([[0 for a in range(0,B.shape[0])]for b in range(0,B.shape[1])],dtype=float)
     for a in range(0,B.shape[1]):
          for b in range(0,B.shape[0]):
               if(a<X.shape[1]):
                    tmp=B[b][a]
                    X[a][b]=tmp
               else:
                    tmp=B[b][a]
                    X[a][b]=tmp
     print(X)
     dot(X,B)      
                 
     

transpose(B)





