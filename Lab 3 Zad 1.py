import pylab
lista=[]

#definicja funkcji

def f(x):
     return   x ** 2 + x - 1

def bisekcja(delta,a,b,iter):
     # Metoda bisekcji
     
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
     lista.append(a)

def wykres():
     pylab.plot(lista)
     pylab.show()


def main():
     iter = 100
     print("Podaj dokładnosc:")
     delta=float(input())
     #print("Podaj przedział a: ")
     #a=float(input())
     #print("Podaj przedział b: ")
     #b=float(input())
     bisekcja(delta, a,b,iter)
     


if(__name__=="__main__"):
     i=0
     while True:
          main()
          i+=1
          if(i>=5):
               wykres()
               break
               
