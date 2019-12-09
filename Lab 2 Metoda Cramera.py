import numpy as np



a=np.array([[1,1,1],
           [8,6,4],
           [15,5,3]])
print(a)

b=np.array([0,1,2])

c=np.array(a)
x=[]
#if(np.linalg.det(a)!=0):
for i in range(0,len(b)):
          for j in range(0,len(b)):
               c[j][i]=b[j]
               if(i>0):
                    c[j][i-1]=a[j][i-1]
          
          x.append(round(np.linalg.det(c)/np.linalg.det(a),1))
       
print(x)

               
          
     
