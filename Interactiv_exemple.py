p = [0] * 10
while sum(p) < 5 :
    z = int(input("вводи целые числа по очереди от 0 до 9_"))
    if p[z] == 1:
        continue
    p[z] = 1
print(*p)




