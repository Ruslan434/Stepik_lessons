f = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for f in "samsung":
    print(f)

# Подвиг 1. С помощью функции range() сформируйте следующую последовательность чисел:
# 0, 1, 2, ..., 10
# Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.
# print(*(list(range(0,11))))


# Вводятся целые числа в одну строчку через пробел.
# Необходимо преобразовать эти данные в список целых чисел.
# Затем, перебрать этот список в цикле for и просуммировать
# все нечетные значения. Результат вывести на экран.
# f = list(map(int,input().split()))
f = [8, 17.1, -2, 4, 0, 13.6, 19, 12, 7]
g = 0
y = 0
c = 0
for i in f:
    f[c] = int(f[c])
    c += 1
for i in f:
    if f[g] % 2 == 1:
        y = y + f[g]
    g += 1
print(y)
print(*f)

# Вводятся названия городов в одну строчку через пробел.
# Необходимо преобразовать входные данные в список.
# Затем, перебрать его циклом for и заменить значения элементов
# на длину названия соответствующего города. Результат вывести
# на экран в виде последовательности чисел через пробел в одну строчку.
f = [Москва, Уфа, Караганда, Тверь, Минск, Казань]
# f = list(map(str,input().split()))
c = 0
for i in f:
    f[c] = len(f[c])
    c += 1

print(*f)

# Вводится натуральное число n. С помощью цикла
# for найти все делители этого числа.
# Найденные делители выводить сразу в столбик
# без формирования списка.
f = 12
# f = int(input())
for i in range(1, (f + 1)):
    if f % i == 0:
        print(i)

# Вводится натуральное число n.
# С помощью цикла for определить,
# является ли оно простым
# (то есть, делится нацело только
# на само себя и на 1). Вывести на экран ДА,
# если n простое и НЕТ - в противном случае.
#
f = int(input("Введи обычное число \n"))
d = []
for i in range(1, f + 1):
    if f % i == 0:
        d.append(i)
print('ДА' if len(d) == 2 else 'НЕТ')

# ЗАДАЧА 6
# Вводится натуральное число n.
# Вычислить сумму всех натуральных чисел
# меньше n, которые кратны или 3 или 5.
# Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9.
# Их сумма равна 23.

f = int(input())
k = 0
for i in range(1, f):
    if i % 5 == 0 or i % 3 == 0:
        k += i
print(k)

words = ["Пайтон", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ' '
fl_first = True
for w in words:
    s += (' ' if fl_first else " ") + w
    fl_first = False
print(s)

# Вводится строка. Необходимо найти все индексы фрагмента "ра"
# во введенной строке. Вывести в строку через пробелы
# найденные индексы. Если этот фрагмент ни разу не будет
# найден, то вывести значение -1.

d = input().lower()
g = []
for x, i in enumerate(d):
    if d[x:x + 2] == 'ра':
        g += [x]

print(*g if len(g) > 0 else {-1})

# Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
#  +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным
# (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
# Необходимо проверить, что введенная строка соответствует этому формату.
# Вывести ДА, если соответствует и НЕТ - в противном случае.

# pf = list(input())
pf = ['+', '7', '(', '1', 'F', '3', ')', '4', '5', '6', '-', '7', '8', '-', '9', '9']
d = []
v = [3, 4, 5, 7, 8, 9, 11, 12, 14, 15]
if len(pf) == 16:
    if pf[0] == "+" and int(pf[1]) == 7 and pf[2] == "(" and pf[6] == ")" and pf[10] == "-" and pf[13] == "-":
        for i in v:
            if pf[i].isdigit() and 0 <= int(pf[i]) <= 9:
                d += ['ДА']
            else:
                break
    else:
        d += ['ДА']
else:
    d += ['ДА']
print("ДА" if len(d) == 10 else "НЕТ")

# Итератор и итерируемые объекты
# введи в строку через пробел Москва Лондон Берлин Пекин
lst = list(map(str, input().split()))
f = iter(lst)
print(next(f))
print(next(f))
