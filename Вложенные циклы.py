for i in range (1,4):
    for j in range (1,6):
        print(i, j, end=' ')
    print()


a = [[1,2,3,4,], [2,3,4,5], [3,4,5,6]]
b = [[1,1,1,100],[2,2,2,200],[3,3,3,300]]
c = []
for i,lst in enumerate(a):
    r = []
    for j,x in enumerate(lst):
        r.append(x + b[i][j])
    c.append(r)
print(c)


A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j],A[j][i] = A[j][i],A[i][j]
for r in A:
    for x in r:
        print(x, end='\t')
    print()

#Подвиг 1. Вводится натуральное число N (то есть, положительное, целое).
# Требуется создать двумерный (вложенный) список размером N x N элементов,
# состоящий из всех единиц, а затем, в последний столбец записать пятерки.
# Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
#P.S. Будьте внимательны в конце строк пробелов быть не должно!
#n = int(input())
n = 4
r = []
for i in range(0,n):
    c = []
    for t in range(0,n):
        c.append(1)
    c[-1] = 5
    r.append(c)
for t in r:
    print(*t)

#Подвиг 2. Вводится список из URL-адресов (каждый с новой строки).
# Требуется в них заменить все пробелы на символ дефиса (-).
# Следует учесть, что может быть несколько подряд идущих пробелов.
# Результат преобразования вывести на экран в виде строк из URL-адресов.
#P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

#import sys
# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список lst_in)
lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for i, probel  in enumerate(lst_in):
    while probel.count("   ") or probel.count("  "):
        probel = probel.replace("   "," ")
        probel = probel.replace("  ", " ")
    while probel.count(" "):
        probel = probel.replace(" ", "-")
    lst_in[i] = probel
for y in lst_in:
    print(y)

#Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа,
# которые меньше этого числа n, то есть, в диапазоне [2; n).
# Результат вывести на экран в строчку через пробел.

y = 11
#y = int(input())
v= []
for a in range(2,y): # формируем первое число кторое будем проверять
    k = 0            #создаем счетчик
    for r in range(2,i//2+1): #подбираем делитель
        if (a % r == 0):
            k = k + 1
    if k <=0:
        v.append(a)
print(v)

a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")