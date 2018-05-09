

import math

def exponencial(a,b):
  return pow(a,b)
  
n=int(input("Insert n:"))

for i in range(0,n):
  
  base = (int(input("Defina la base:")))
  exponencial = (int(input("Defina el exponente:")))
  
print (str(base) + "exponencial" + str(exponencial) + "-" + str(exponencial(base,exponencial)))
#Se importan los valores math
#Se define la funcion del exponencial,y se devuelve la potencia
#Se define el valor para N
#Se definen la base y el exponencial
#Se calcula...

