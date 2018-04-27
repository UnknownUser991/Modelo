def mx(a,b):
  if a > b:
    return a
  else:
    return b
def max3(a,b,c):
  return mx(mx(a,b),c)


print(max3(3,5,4))
  
  
a=int(input("??"))
b=int(input("??"))
print(mx(a,b))