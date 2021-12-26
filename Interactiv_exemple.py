a = list(map(int, input()))
b = 0
d = 1
while b != len(a) :
      d = d * a[(b)]
      b += 1
print(d)