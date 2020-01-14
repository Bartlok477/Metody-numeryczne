import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

x = np.arange(0, 10)
y = np.cos(x)


a=np.arange(0,4*np.pi-1,0.1)
b=np.cos(a)



f = interpolate.interp1d(x, y)



xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)

plt.plot(x, y, 'o', xnew, ynew, '-',a,b,':' )
plt.legend(['cos[x]','interpolate cos(x)','real cos(x)'])
plt.show()
