
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

