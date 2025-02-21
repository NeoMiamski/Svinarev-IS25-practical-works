# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
try:
    def minsells(minsells1, minsells2):
        if workmode == 1:
            minsells1 = min(A1, A2, A3, A4, A5)
            return minsells1
        if workmode == 2:
            minsells2 = min(B1, B2, B3, B4, B5)
            return minsells2
    s = ("груши 45 991 63 100 12 морковь 13 47 26 0 16")
    d = s.split()
    A1, A2, A3, A4, A5, B1, B2, B3, B4, B5 = int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]), int(d[7]), int(d[8]), int(d[9]), int(d[10]), int(d[11])
    goods1 = d[0]
    goods2 = d[6]
    workmode = 1
    pearsells = minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5)
    workmode = 2
    carrotsells = minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5)
    report = {goods1: A1, goods2: B1}
    print("Минимальные продажи груш:", pearsells)
    print("Минимальные продажи моркови:", carrotsells)
    print(report)
except TypeError:
    print('Вы ввели неверное значение')