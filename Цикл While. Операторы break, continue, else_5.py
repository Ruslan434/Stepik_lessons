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

#Гражданин 1 января открыл счет в банке, вложив 1000 руб.
# Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
# Определить сумму вклада через n лет (n - целое положительное число,
# вводимое с клавиатуры). Результат округлить до сотых и вывести на экран.
# Программу реализовать при помощи цикла while.
y = int(input("введи целое число_"))
sum = 1000
c = 0.05
while y:
    sum = sum + (sum * c)
    y = y - 1
    print(round(sum,2))

#Вводятся два натуральных четных числа n и m в одну строчку через пробел,
# причем n < m. Напечатать все нечетные числа из интервала [n, m].
# Задачу решить без применения условного оператора.
# Результат вывести на экран в виде строки чисел, записанных через пробел.
# Программу реализовать при помощи цикла while.
n,m = map(int,input("введи 2 натуральных числа_").split())
c = 0
while m >= n:
    while n % 2 == 1:
        print(n, end=" ")
        n = n + 1
    n += 1

#Составить программу поиска всех трехзначных чисел, которые при делении
#на 47 дают в остатке 43 и кратны 3.
#Вывести найденные числа в строчку через пробел.
#Программу реализовать при помощи цикла while.
q = 100
w = 1000
while w >= q:
    if q % 47 == 43 and q % 3 == 0:
        print(q, end=" ")
    q += 1
print("\n")

#Подвиг 2. Имеется одномерный список длиной 10 элементов, состоящий из нулей:
#p = [0] * 10
#На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p,
#по которому записывается значение 1,
#если ее там еще нет. Если же 1 уже проставлена, то список не менять и снова запросить у
#пользователя очередное число. Необходимо расставить так пять единиц в список.
#(После этого цикл прерывается).
#Программу реализовать с помощью цикла while и с использованием оператора continue,
# когда 1 не может быть добавлена в список. Результат вывести на экран в виде последовательности чисел,
# записанных через пробел.

p = [0] * 10
while sum(p) < 5:
    z = int(input("вводи целые числа по очереди от 0 до 9_"))
    if p[z] == 1:
        continue
    p[z] = 1
print(*p)

#Пример работы операторов цикла

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

#Подвиг 3. На каждой итерации цикла вводится целое число.
# Необходимо подсчитать произведение только положительных чисел,
# до тех пор, пока не будет введено значение 0.
# Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while.
# Результат произведения вывести на экран.
p = 1
z = 1
while z :
    z = int(input())
    if z == 0:
        break
    elif z < 0:
        continue
    p = p * z
print(p)

#АПГРЕЙД

p = 1
z = 1
while z :
    z = int(input())
    if  z <= 0:
        continue
    p = p * z
print(p)


#Вводится список названий городов в одну строчку через пробел.
# Определить, что в этом списке все города имеют длину более 5 символов.
# Реализовать программу с использованием цикла while и оператора break.
# Вывести ДА, если условие выполняется и НЕТ - в противном случае.

#p = list(map(str,input().split()))
p = ["Самара", "Ульяновск", 'Новгород', 'Воронеж']
x = 0
c = len(p)
m = "НЕТ"
while c:
    if len(p[x]) >= 5:
        m = "ДА"
        break
    x += 1
    c -= 1
print(m)

#Вводится список имен студентов в одну строчку через пробел.
# Определить, что хотя бы одно имя в этом списке начинается и заканчивается
# на ту же самую букву (без учета регистра).
# Реализовать программу с использованием цикла while и
# оператора break. Вывести ДА, если условие выполняется и
# НЕТ - в противном случае.

#p = list(map(str,input().split()))
p = ['Петр', 'Анна', 'Иван', 'Сергей', 'Михаил', 'Федор']
x = 0
c = len(p)
m = "НЕТ"
while c:
    if p[x][0].lower() == p[x][-1].lower():
        m = "ДА"
        break
    x += 1
    c -= 1
print(m)

#Вводится натуральное число n (то есть, целое положительное).
# В цикле перебрать все целые числа в интервале [1; n] и
# сформировать список из чисел, кратных 3 и 5 одновременно.
# Вывести полученную последовательность чисел в виде строки через пробел,
# если значение n меньше 100. Иначе вывести на экран
# сообщение "слишком большое значение n" (без кавычек).
# Использовать в программе оператор else после цикла while.
#c = int(input())
c = 49
x = int(1)
if c < 100:
    while x <= c:
        if x % 3 == 0 and x % 5 == 0:
            print(x, end=" ")
        x += 1
else:
    print("слишком большое значение n")

#еще один вариант
#c = int(input())
c = 49
x = int(1)
l = []
if c < 100:
    while x <= c:
        if x % 3 == 0 and x % 5 == 0 :
            l.append(x)
        x += 1
    else:
        print(*l)
else:
    print("слишком большое значение n")

# Вводится натуральное число n.
# Вывести первое найденное натуральное число
# (то есть, перебирать числа, начиная с 1),
# квадрат которого больше значения n.
# Реализовать программу с использованием цикла while.

c = 25
#c = int(input("Веди любое число "))
x = int(1)
while x*x <= c:
    if x*x == c:
        x += 1
        break
    x += 1
print(x)

# Каждый следующий день он увеличивал пробег
# на 10 % от пробега предыдущего дня.
# Определить в какой день он пробежит больше x км
# (натуральное число x вводится с клавиатуры).
# Результат (искомый день) вывести на экран.
c = 20
#c = int(input())
b = 1
n = 10
while n < c :
    n = n + (n * 0.1)
    b += 1
print(b)

#(На использование цикла while). Вводятся названия книг
# (каждое с новой строки). Удалить из введенного списка
# все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
# Результат вывести на экран в виде строки из оставшихся названий через пробел.
# считывание списка из входного потока

#lst_in = list(map(str.strip, sys.stdin.readlines()))
#import sys
lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
i = 0
while i < len(lst_in):
    if ' ' in lst_in[i]:
        del lst_in[i]
        continue
    i += 1
print(*lst_in)

# Вводится список названий городов в одну строчку через пробел.
# Перебрать все эти названия с помощью цикла for и определить,
# начинается ли название следующего города на последнюю букву
# предыдущего города в списке. Если последними встречаются
# буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
# Вывести на экран ДА, если последовательность удовлетворяет
# этому правилу и НЕТ - в противном случае.

#d = list(map(str, input().lower().split()))
s = ['москва', 'астрахань', 'новгород', 'димитровград', 'душанбе']
h = []
for i in range(len(s)-1) :
    if s[i][-1] == s[i+1][0]:
        h.append('Да')
    else:
        if s[i][-1] == 'ь' or s[i][-1] == 'ъ' or s[i][-1] == 'ы' and s[i][-2] == s[i+1][0]:
            h.append("Да")
        else:
            h.append("Нет")
print('ДА' if h.count("Да") == len(s)-1 else 'НЕТ')

