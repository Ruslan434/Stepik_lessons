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
