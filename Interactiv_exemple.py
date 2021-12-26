a = int(input())
v = 1
x = 1
print(v,x, end=" ")
while a > 2:
      v,x = x, v + x
      print(x, end=" ")
      a = a - 1

