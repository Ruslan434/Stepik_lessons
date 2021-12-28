p = [0] * 10
while sum(p) < 5 :
    z = int(input("вводи целые числа по очереди_ от 0 до 9"))
    if 0 <= z <= 9:
        if p[z] == 1:
            continue
        p[z] = 1
print(*p)



