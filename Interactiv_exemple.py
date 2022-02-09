#d = list(map(str, input().lower().split()))
s = ['москва', 'астрахань', 'новгород', 'димитровград', 'душанбе']
h = []

for i in range(len(s)) :
    if s[i][-1] == s[i+1][0]:
        h.append('Да')
    else:
        if s[i][-1] == 'ь' or s[i][-1] == 'ъ' or s[i][-1] == 'ы':
            if s[i][-2] == s[i+1][0]:
                h.append("Да")
        else:
            h.append("Нет")
print(h)