def mx(a,b):
  if a > b:
    return a
  else:
    return b
def max3(a,b,c):
  return mx(mx(a,b),c)

a=int(input("??"))
b=int(input("??"))
c=int(input("??"))
valor_maximo_a_b=(mx(a,b))
print(valor_maximo_a_b)
valor_maximo_a_c=(mx(a,c))
print(valor_maximo_a_c)
valor_maximo_b_c=(mx(b,c))
print(valor_maximo_b_c)
print(max3(a,b,c))
