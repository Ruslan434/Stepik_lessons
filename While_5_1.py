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
    d += 1
    c = c + f
    print(round(c,2), end=" ")
