s = 70
i = 0
N = 100
while i <= N and s <= 100:
    s +=1
    i +=1
print(s,i)

#Вводятся два целых положительных числа n и m, причем, n < m.
# Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m].
# Программу реализовать при помощи цикла while.
n,m = map(int,input("Введи два целых положительных числа n и m, причем, n < m(например: 2 4)_  ").split())
z = 0
while n <= m:
    z = n * n
    n +=1
    print(z, end=" ")

#  Вводится стоимость одной книги x рублей (вещественное число).
#  Необходимо вывести на экран в строчку через пробел
#  стоимости 2, 3, ... 10 таких книг с точностью до десятых.
#  Программу реализовать при помощи цикла while.

f = float(input("Введи вещественное число_ "))
c = f
d = 1
while d != 10 :
    d +=1
    c = c + f
    print(round(c,2), end=" ")

# На каждой итерации цикла пользователь вводит целое число.
# Цикл продолжается, пока не встретится число 0.
# Необходимо вычислить сумму введенных в цикле чисел и вывести результат на экран.
# Программу реализовать при помощи цикла while.
f = int(input("введи целое число_  "))
d = 0
while f != 0 :
    d += f
    f = int(input())
print(d)

# Вводится строка (слаг). Замените в этой строке все
# подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-).
# Результат преобразования строки выведите на экран.
# Программу реализовать при помощи цикла while.

#f = str(input())
f = "osnovnye---------metody------------------slovarey"
while "--" in f:
    f = f.replace("--", "-")
print(f)

#Вводится натуральное (то есть, целое положительное) число
#(от трехзначного и более). Найти произведение всех его цифр.
#Результат вывести на экран. Программу реализовать при помощи цикла while.

a = list(map(int, input("введи трехзначне и более число_ ")))
b = 0
d = 1
while b != len(a) :
      d = d * a[(b)]
      b += 1
print(d)


# Последовательность Фибоначчи образуется так: первые два числа равны 1 и 1,
# а каждое последующее равно сумме двух предыдущих.
# Имеем такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ...
# Постройте последовательность Фибоначчи длиной n (n вводится с клавиатуры).
# Результат отобразите в виде строки полученных чисел, записанных через пробел.
# Программу реализовать при помощи цикла while.

a = int(input("введи целое число_ "))
v = 1
x = 1
print(v,x, end=" ")
while a > 2:
      v,x = x, v + x
      print(x, end=" ")
      a = a - 1
# Одноклеточная амеба каждые 3 часа делится на 2 клетки.
# Определить, сколько клеток будет через n часов
# (n - целое положительное число, вводимое с клавиатуры).
# Считать, что изначально была одна амеба. Результат вывести на экран.
# Задачу необходимо решить с использованием цикла while.
n = int(input("введи целое число_"))
v = 1
c = 3
while c <= n :
    v = v * 2
    c = c + 3
print(v)

count = int(input("введи целое число_"))//3
i = 1
while count:
  i *= 2
  count -= 1
print(i)