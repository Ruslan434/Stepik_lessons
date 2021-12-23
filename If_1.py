print('Введите числа по одному:_')
a = int(input())
b = int(input())
c = int(input())
s = a + b + c
if s == 15:
    print ('Это пиздец')
elif s != 15:
    print ('Число не равно 15')
elif s > 15:
    print ('Число больше 15')
elif s < 15:
    print ('Число меньше 15')


a,b,c,d,e,f = map(int, input("Введи 6-ти значное число: "))
if a+b+c == d+e+f:
    print("Счастливое число")
else:
    print("Не счастливое число")

#определение наименьшего числа
b,n,m = map(int,input("нужно ввести 3 цифры через пробел_  ").split())
if b < n < m or b < m < n :
    print(b)
elif  n < b < m or n < m < b :
    print(n)
elif m < n < b or m < b < n:
    print(m)
#выбор пункта меню
m = int(input("Введите цифру от 1 до 6 : "))
if m == 1:
    print('Введение в Python')
elif m == 2:
    print("Строки и списки")
elif m == 3:
    print("Условные операторы")
elif m == 4:
    print("Циклы")
elif m == 5:
    print("Словари, кортежи и множества")
elif m == 6:
    print("Выход")
else:
    print(type(m))
#тоже самое только круче
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
print(m.split('\n')[int(input("Введите цифру от 1 до 6 : ")) - 1])


g = int(input("Веди номер месяца от 1 до 12: " ))
if g == 1 or g ==3 or g ==5 or g ==7 or g ==8 or g ==10 or g ==12:
    print(31)
elif g == 2:
    print(28)
else:
    print(30)

month = int(input("Веди номер месяца от 1 до 12: "))-1
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0<=month<13:
    print(days[month])
else:
    print('?')

d = str(input("определяет введенное слово является палиндромом или нет (одинаково читается и вперед и назад)   "))
msg = "палиндром" if d.lower()[:] == d.lower()[::-1] else "не палиндром"
print (msg)

d = int(input(" Вводится целое число 0 или 1   "))
f = ("True" if d <= 1 else "False") if d == 1 or d == 0 else ("False" if d == 0 else "True")
print(f)

f = int(input("Ввести значение в диапазоне [0 : 59]   "))
d = (f + 1 if f <= 58 else 59) if f < 58 else (0 if f == 59 else f + 1 )
print(d)

n = int(input("Ввести значение в диапазоне [0 : 59]   "))
print((n + 1) % 60)