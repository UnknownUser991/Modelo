suma= 0
contador= -1  #-1 debido a que no se cuenta el numero 0
while True:
  numero = int(input("Num?"))
  contador = contador + 1 
  suma= suma + numero
  if numero==0:
    break
print(contador)
print(suma)


