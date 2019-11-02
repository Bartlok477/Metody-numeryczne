

import math

def dodawanie(a,b):
     print("Dodawanie:",a+b)

def odejmowanie(a,b):
     print("Odejmowanie:",a-b)

def mnozenie(a,b):
     print("Mnozenie:",a*b)

def dzielenie(a,b):
     if(b==0):
          print("Zakaz dzielenia przez zero")
     else:
          print("Dzielenie:",a/b)
def potegowanie(a,b):
     c=pow(a,b)
     print("Potegowanie:",c)

def pierwiastkowanie(a,b):
     if(a<0 and b%2==0):
		a=a*(-1)
          c=pow(a,1/b)
          c=str(c)
          c=c+"j"
          print("Pierwiastkowanie:",c)
     else:
          c=pow(a,1/b)
          print("Pierwiastkowanie:",c)





if __name__=="__main__":
     print("Podaj 2 liczby:")
     a=int(input())
     b=int(input())


     dodawanie(a,b)
     odejmowanie(a,b)
     mnozenie(a,b)
     dzielenie(a,b)
     potegowanie(a,b)
     pierwiastkowanie(a,b)
