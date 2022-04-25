age = 26
name = 'Swaroop'
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))
# В строку могут быть включены определённые обозначения, а впоследствии
# может быть вызван метод format для замещения этих обозначений соответствующими аргументами.
# Взгляните на первый случай применения обозначений, где мы пишем {0}, и
# это соответствует переменной name, являющейся первым аргументом метода
# format. Аналогично, второе обозначение {1} соответствует переменной age,
# являющейся вторым аргументом метода format. Заметьте, что Python начинает отсчёт с 0, поэтому первая позиция – номер 0, вторая – номер 1 и т.д.
# Заметьте, мы ведь могли добиться того же самого результата и объединением строк: 'Возраст' + name + ' -- ' + str(age) + ' лет.', однако вы
# сами видите, как это некрасиво, и как легко в таком случае допустить ошибку.

a_point = 'фронт'
b_point = 'Бэк'
c_point = 'SQL'
print(
    'Нужно сначала выучить {0}, а затем разбираться в {1}, если хватит ума то и {2}'.format(c_point, b_point, a_point))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1 / 3))
# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))
# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
s = """'Это многострочная строка.
Это вторая её строчка.
а это третьияяя"""
print(s)

a, b = "hello", "Python"
# или a,b = map(str,input().split())
a = (a + " ") * 2
b = (b + " ") * 3
print(a + b)
# hello hello Python Python Python

a, b = map(int, input().split())
print(not (bool(a % b)))

a, b = map(str, input().split())
print('Переменная a = ' + a, 'переменная b = ' + b, sep=", ")

a, b = map(str, input().split())
z = b + "."
c = str(len(a + z))
print('Строка: ' + a + " " + z, "Длина: " + c)

a = str(input())
print('Строка: ' + a, end=". " + "Длина: " + str(len(a)))

# s = input()
# print('Строка:', s + '. Длина:', len(s))

a, b = map(str, input().split())
print(f"Коды: {a} = {ord(a)}, {b} = {ord(b)}")

s = input()
d = input()
print(s[0::2] + " " + d[1::2])

s = "Hello"
d = 'Balakirev'
print(d[0:len(s)])

s = "Hello"
d = "Hell"
print(d[1::2] == s[1:len(d):2])

s = "HELLO"
print((s[0].upper() + s[1:].lower()))

g = "-".join(input().split("---"))
print("-".join(g.split("--")))

# вводим 3 числа, сделать все трехзначными по левому краю
a, b, c = map(str, input().split())
print(a.rjust(3, "0"))
print(b.rjust(3, "0"))
print(c.rjust(3, "0"))

# Посчитать количество слов
s = "I love Python"
print(s.count(' ') + 1)
print(len(input().split()))

qq = "My best friend is Python!"
aa = qq.replace(" ", "'", 1)
print(aa.replace(" ", '"'))

marks = 3
3
2
4
4
5
4
3
2
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
