y = [[2, 3, 4, 5, 6], [4, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
f = 0
for i in range(len(y)):
    for g in range(i + 1, len(y)):
        if y[i][g] == y[g][i]:
            f = 1
        else:
            f = -1
            print( "НЕТ")
            break
        print("ДА")
