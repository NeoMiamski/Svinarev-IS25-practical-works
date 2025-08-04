# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.

import re

years = []
year = []
slice = {}

with open('Dostoevsky.txt', encoding='utf-8') as file:
    for line in file:
        i = (file.readline().split())
        year = re.findall("18..", ' '.join(i), re.IGNORECASE)
        print(' '.join(i))
        if len(year) > 0:
            print(' '.join(year))
            years.append(int((' '.join(year))))
sl = set(years)
print(sl)
print(len(sl))