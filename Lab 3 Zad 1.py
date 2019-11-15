


def f(x):
     return 0.5 * x ** 2 + 0.5 * x - 0.5
# Metoda bisekcji
iter = 100
delta = 0.00001
a = -2.25
b = 1.5
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
