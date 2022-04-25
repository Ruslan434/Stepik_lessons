print("Hello")
x = "Hello"
print(id(x))
print(type(x))
# Это моя первая программа
# смена id и тип значения
x = 15
print(id(x))
print(type(x))
# каскадное присваивание
x = y = z = 0
print(id(x), id(y), id(z))
# множественное присваивание
x, y, z, d = 1, 2, 3, 4
print(id(x), id(y), id(z))
print(x, y, z, d)

a, b, c, d, e, f = map(int, input())

a, b, c = map.(int, input()).split

# смена значений
x, y = y, x
print(x, y)
# ввод значений
a = int(input("Введите число: "))
print(a)

# пробелы и разделительные знаки

print(1, 2, 3, sep=",")
print(1, 2, 3, sep="-")
print(1, 2, 3, sep="###")
print(1, 2, 3, sep=",", end=': ')
print(1, 2, 3, sep=",", end=' ')
print("sdfgh")

# управляющие символы
print('раз\tдва\tтри\nuno\tdos\ttres')

import math

n = 6
k = 3
d = (math.factorial(n) / (math.factorial(k) * (math.factorial(n - k))))
print(int(d))

a = 3
b = 4
# a, b = map(int, input().split())
c = (pow(a ** 2 + b ** 2, 0.5))
print(round(c, 2))

n = 40
m = 5
c = 20
b = (m + n) // c
v = (m + n) % c
if v > 0:
    b += 1
print(b)

x = 20
gel = x * 0.9
z = 500 // gel

print(int(z))
# f строка
print(f"kjcxkcknbzx {x} jhjhgjgjhjhjkhb {gel}")

a = float(input("Введите значение: "))
b = float(input("Введите значение: "))
print(f"Да !!! периметр пряоугольника равен {a * b}")

s1, s2 = map(str.strip, input().split())
print(f"Word 1: {s1} ", f" Word 2: {s2}", sep='|')

a, b = map(int, input("Введи 2 числа чрез пробел: ").split())
print(a ** b)

print(2 * (float(input()) + float(input())))
