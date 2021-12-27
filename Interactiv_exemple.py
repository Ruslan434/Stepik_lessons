
y = int(input())
sum = 1000
c = 0.05
while y:
    sum = sum + (sum * c)
    y = y - 1
    print(round(sum,2))
