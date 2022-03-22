seq = list('абвгде')
for i, val in enumerate(seq, start=1):
    print(f'№ {i} => {val}')

#Получение списка парных кортежей (number, value)
# (порядковый номер в последовательности, значение последовательности)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# можно указать с какой цифры начинать считать
print(list(enumerate(seasons, start=1)))
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
