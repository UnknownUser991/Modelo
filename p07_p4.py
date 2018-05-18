def fib(n):
  a = 1
  b = 1
  c = 1
  print(a)
  print(b)
  for i in range(3,n+1):
    c = a + b
  #  print(c)
    a = b
    b = c
  return(c)







nn=int(input("n"))
cosa=fib(nn)
print("el "+str(nn)+" numero de Fibbonaci es: " +str(cosa))
