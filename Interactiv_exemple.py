p = [0] * 10
while sum(p) < 5 :
    z = int(input("вводи целые числа по очереди от 0 до 9_"))
    if z > 9:
        continue
    elif p[z] == 1:
        break
    p[z] = 1
else:
    print('так работают операторы continue, break, else')
print(*p)




