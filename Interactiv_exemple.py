lst_in = [[2, 2, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
c = "ДА"
for i in range(len(lst_in)):
    for t in range(i + 1, len(lst_in)):
        if lst_in[i][t] != lst_in[t][i]:
            c = "НЕТ"
            break

print(c)
