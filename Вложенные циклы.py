for i in range(1, 4):
    for j in range(1, 6):
        print(i, j, end=' ')
    print()

a = [[1, 2, 3, 4, ], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 100], [2, 2, 2, 200], [3, 3, 3, 300]]
c = []
for i, lst in enumerate(a):
    r = []
    for j, x in enumerate(lst):
        r.append(x + b[i][j])
    c.append(r)
print(c)

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]
for r in A:
    for x in r:
        print(x, end='\t')
    print()

# Подвиг 1. Вводится натуральное число N (то есть, положительное, целое).
# Требуется создать двумерный (вложенный) список размером N x N элементов,
# состоящий из всех единиц, а затем, в последний столбец записать пятерки.
# Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
# P.S. Будьте внимательны в конце строк пробелов быть не должно!
# n = int(input())
n = 4
r = []
for i in range(0, n):
    c = []
    for t in range(0, n):
        c.append(1)
    c[-1] = 5
    r.append(c)
for t in r:
    print(*t)

# Подвиг 2. Вводится список из URL-адресов (каждый с новой строки).
# Требуется в них заменить все пробелы на символ дефиса (-).
# Следует учесть, что может быть несколько подряд идущих пробелов.
# Результат преобразования вывести на экран в виде строк из URL-адресов.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

# import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список lst_in)
lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya',
          'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for i, probel in enumerate(lst_in):
    while probel.count("   ") or probel.count("  "):
        probel = probel.replace("   ", " ")
        probel = probel.replace("  ", " ")
    while probel.count(" "):
        probel = probel.replace(" ", "-")
    lst_in[i] = probel
for y in lst_in:
    print(y)

# Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа,
# которые меньше этого числа n, то есть, в диапазоне [2; n).
# Результат вывести на экран в строчку через пробел.

y = 11
# y = int(input())
v = []
for a in range(2, y):  # формируем первое число кторое будем проверять
    k = 0  # создаем счетчик
    for r in range(2, i // 2 + 1):  # подбираем делитель
        if (a % r == 0):
            k = k + 1
    if k <= 0:
        v.append(a)
print(v)

a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2 + 1):
    if (a % i == 0):
        k = k + 1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")

# Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов,
# состоящий из нулей и, в некоторых позициях, единиц (см. пример ввода ниже).
# Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали.
# То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.

# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# import sys
# считывание списка из входного потока
# s = sys.stdin.readlines()
# y = [list(map(int, x.strip().split())) for x in s]
# здесь продолжайте программу (используйте список lst_in)
y = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
p = 0
for i in range(len(y) - 1):
    for s in range(len(y) - 1):
        if y[i][s] + y[i][s + 1] + y[i + 1][s] + y[i + 1][s + 1] >= 2:
            p += 1
            continue
print("ДА" if p <= 0 else "НЕТ")

# Подвиг 5. Вводится двумерный список размерностью 5 х 5 элементов,
# состоящий из целых чисел (пример ввода см. ниже).
# Проверьте, является ли этот двумерный список симметричным относительно главной диагонали.
# Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
# Выведите на экран ДА, если матрица симметрична и НЕТ - в противном случае.

lst_in = [[2, 2, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
c = "ДА"
for i in range(len(lst_in)):
    for t in range(i + 1, len(lst_in)):
        if lst_in[i][t] != lst_in[t][i]:
            c = "НЕТ"
            break
print(c)

# Сколько шеститибуквенных слов, начинающихся и заканчивающихся,
# согласной буквой и содержащей ровно 2 гласные можно стоставить из букв
# Т,Ы,К,В,А ? Каждая из допустимых букв может входить в слово несколько раз
t = 0
for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        slovo = b1 + b2 + b3 + b4 + b5 + b6
                        if slovo[0] in 'tkv' and slovo[-1] in 'tkv':
                            if slovo.count("u") + slovo.count("a") == 2:
                                t += 1
                                print(slovo)
print(t)

# Большой подвиг 6.
# Вводится список целых чисел в одну строку через пробел.
# Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).
# Идея алгоритма очень проста и проиллюстрирована на рисунке ниже.
# Вначале мы рассматриваем первый элемент списка и ищем второй минимальный
# относительно первого элемента (включая и его). На рисунке - это последний элемент со значением -1.
# Затем, меняем местами первый и последний элементы. Переходим ко второму элементу списка и повторяем
# эту же процедуру, но относительно второго элемента (то есть, первый уже не рассматриваем).
# На рисунке минимальный элемент - это 2, поэтому менять местами здесь ничего не нужно.
# Переходим к 3-му элементы со значением 6. Относительно него находим минимальный элемент - это 3.
# Меняем их местами.
# Вот идея алгоритма сортировки выбором. Реализуйте его для вводимого списка целых чисел. Результат выведите в виде списка чисел одну строку через пробел.

y = [8, 11, -53, 2, 10, 11]

for i in range(len(y)):
    for u in range(i, len(y)):
        if y[i] < y[u]:
            y[i], y[u] = y[u], y[i]
y.reverse()
print(*y)

# Большой подвиг 7. Вводится список целых чисел в одну строку через пробел.
# Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька.
# Идея алгоритма проста и показана на рисунке ниже.
# При первом проходе перебираем все соседние пары элементов и если значение предыдущего элемента
# (слева) больше значения следующего (справа), то они меняются местами.
# (На рисунке 3 и 2 меняются местами). Следующая пара - это 3 и 6. Они уже выстроены по возрастанию,
# поэтому ничего не делаем и переходим к следующей паре 6 и -1. Меняем значения местами и видим,
# что на последнем месте находится максимальное значение 6, что нам и нужно.При втором проходе
# делаем все то же самое, но доходим до предпоследнего элемента, так как последнее значение 6
# уже отсортировано. На третьем проходе исключаем уже последние два элемента и так далее.
# То есть, в этом алгоритме достаточно сделать N-1 проходов, где N - длина списка.
# Вот идея алгоритма сортировки всплывающего пузырька. Реализуйте его для вводимого списка
# целых чисел. Результат выведите в виде списка чисел одну строку через пробел.
# y = list(map(int,input().split()))
y = [4, 5, 2, 0, 6, 3, -56, 3, -1]
for i in range(len(y)):
    for u in range(i, len(y)):
        if y[i] > y[u]:
            y[i], y[u] = y[u], y[i]
print(*y)
