
# Вводится натуральное число n.
# Вывести первое найденное натуральное число
# (то есть, перебирать числа, начиная с 1),
# квадрат которого больше значения n.
# Реализовать программу с использованием цикла while.

c = int(input(":  "))
x = int(1)
while x*x <= c:
    if x*x == c:
        x += 1
        break
    x += 1
print(x)
