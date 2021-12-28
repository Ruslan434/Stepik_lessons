p = 1
z = 1
while z :
    z = int(input("вводи целые числа по очереди "))
    if z == 0:
        break
    elif z < 0:
        continue

    p = p * z
else:
    print('так работают операторы continue, break, else')
print(p)




