# Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
#  +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным
# (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
# Необходимо проверить, что введенная строка соответствует этому формату.
# Вывести ДА, если соответствует и НЕТ - в противном случае.

#pf = list(input())
pf = ['+', '7', '(', '1', 'F', '3', ')', '4', '5', '6', '-', '7', '8', '-', '9', '9']
d = []
v = [3,4,5,7,8,9,11,12,14,15]
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
