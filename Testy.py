import matplotlib.pyplot as plt
import numpy as np

##a=np.array([[6,7,8],[5,5,6]])
a=np.array([6,7,8,9,10])

print(a)



t=np.transpose(a)
print(t)
print("*****")
print(a)
t=np.shape(a)
print("t=",t)
a=np.squeeze(a).shape
print(a)
