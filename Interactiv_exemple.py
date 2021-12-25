m,n = map(int,input().split())
if 2 <= n <= 27 and m == 2 :
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 1 and m == 2:
    print(str(m - 1).rjust(2,'0') + "." + str(31).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 1 and m == 1:
    print(str(12).rjust(2,'0') + "." + str(31).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 31 and m == 12:
    print(str(m).rjust(2,'0') + "." + str(n -1).rjust(2,"0"),str(1).rjust(2,'0') + "." + str(1).rjust(2,"0"), sep=' ')


elif n == 1 and (m == 4 or m == 6 or m == 9 or m == 11 or m == 8):
    print(str(m - 1).rjust(2,'0') + "." + str(31).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 1 and ( m == 5 or m == 7  or m == 10 or m == 12):
    print(str(m - 1).rjust(2,'0') + "." + str(30).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')

elif n == 1 and m == 3 :
    print(str(m - 1).rjust(2,'0') + "." + str(28).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 28 and m == 2:
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m + 1).rjust(2,'0') + "." + str(1).rjust(2,"0"), sep=' ')

elif 2 <= n <= 29 and (m == 4 or m == 6 or m == 9 or m == 11) :
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"), sep=' ')
elif n == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m + 1).rjust(2,'0') + "." + str( 1).rjust(2,"0"), sep=' ')



elif 2 <= n <= 30 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) :
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m).rjust(2,'0') + "." + str(n + 1).rjust(2,"0"),sep=' ')
elif n == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 ):
    print(str(m).rjust(2,'0') + "." + str(n - 1).rjust(2,"0"),str(m + 1).rjust(2,'0') + "." + str(1).rjust(2,"0"), sep=' ')
