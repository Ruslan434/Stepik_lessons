for i in range (1,4):
    for j in range (1,6):
        print(i, j, end=' ')
    print()


a = [[1,2,3,4,],[2,3,4,5],[3,4,5,6]]

for lst in a:
    for x in lst:
        print(x, type(x), end=' ')
    print()
