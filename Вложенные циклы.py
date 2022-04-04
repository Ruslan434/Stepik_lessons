for i in range (1,4):
    for j in range (1,6):
        print(i, j, end=' ')
    print()


a = [[1,2,3,4,], [2,3,4,5], [3,4,5,6]]
b = [[1,1,1,100],[2,2,2,200],[3,3,3,300]]
c = []
for i,lst in enumerate(a):
    r = []
    for j,x in enumerate(lst):
        r.append(x + b[i][j])
    c.append(r)
print(c)


A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j],A[j][i] = A[j][i],A[i][j]
for r in A:
    for x in r:
        print(x, end='\t')
    print()
