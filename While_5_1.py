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