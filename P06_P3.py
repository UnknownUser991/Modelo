x = int(input("Km 1er día?"))
y = int(input("Longitud carrera?"))
d = 0
while y >= x:
  d = d + 1
  x = x + x * 0.1
  
print(d)