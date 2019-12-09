
import pylab

def f(x):
     return   x ** 2 + x - 1
# Metoda bisekcji
iter = 100
delta = 0.00001
a = 0.05
b = 0.95
for k in range(1, iter):
     x = (a + b) / 2
     if (abs(f(x)) < delta):
          break
     else:
          if(f(x) * f(a) < 0):
               b = x
          else:
               a = x
     


print(round(x,6))
