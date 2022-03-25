lst = list(map(float,input().split()))
c = 0
for i, value in enumerate(lst):
    if value < lst[i+1]:
        c = value
    if i == (len(lst) - 2):
        continue
print(c)










