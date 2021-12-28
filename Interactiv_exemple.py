#a,b = map(int,input().split())
a = 100
b = 1000
while(a <= b):
    if(a % 47 == 43 and a % 3 == 0):
        print(a,end = " ")
    a+=1
print("\n\n231 372 513 654 795 936 - правильный ответ.")