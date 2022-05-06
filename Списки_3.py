marks = [3, 3, 2, 4, 4, 5, 4, 3, 2]
# marks = list(map(int, input().split()))
a = round((sum(marks) / len(marks)), 1)
print(a)

a = "Мастер и Маргарита"
b = "Булгаков"
v = 233
e = 435.45
print(type(e))
book = [a, b, v, e]
book[3] = e * 2
del (book[2])
book[1] = 'Пушкин'
print(book)

lst = [52, 65, 64, 54, 68, 59, 42, 63]
# lst = list(map(int, input().split()))
lst = (sorted(lst, reverse=True))
print(*lst)

# ************** методы списков *****************

lst = [8, 12, 2, -10, 6]
lst.append(lst[0] != lst[-1])
print(*lst)

cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, 'Ульяновск')
print(*cities)

# s = list(input())
s = list('+7(912)123-45-67')
s.remove("-")
s.remove("-")
del (s[0])
del (s[0])
# s[s.index('-',0,-1)]
s.insert(0, '8')
# print(s)
print("".join(s))

a = [8, 11]
# a = list(map(int,input().split()))

lst = [5.4, 6.7, 10.4]

print(lst + [a])

# генератор списка
n = 6
a = [x ** 2 for x in range(n)]
print(a)


#Подвиг 1. Вводятся вещественные числа в строку через пробел.
# Необходимо на их основе сформировать список lst с помощью list
# comprehension (генератора списков) из модулей введенных чисел
# (в списке должны храниться именно числа, а не строки). Результат
# вывести на экран в виде списка командой:
#print(lst)  5.56 -8.7 1.0 3.14 77.845
d = input('Вводи вещественные числа в строку через пробел  ')
c = [abs(float(f)) for f in d.split()]
print(c)