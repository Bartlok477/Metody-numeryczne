import numpy as np



a=np.array([[10,40,70,300],
           [20,50,80,360],
           [30,60,80,390]])

b=np.array([300,360,390])

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

               
          
     
