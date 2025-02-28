# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
try:
    def minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5):
        pearsells = min(A1, A2, A3, A4, A5)
        carrotsells = min(B1, B2, B3, B4, B5)
        return pearsells, carrotsells
    s = ("груши 45 991 63 100 12 морковь 13 47 26 0 16")
    d = s.split()
    goods1, goods2 = d[0], d[6]
    sells1, sells2 = d[1:6], d[7:12]
    A1, A2, A3, A4, A5, B1, B2, B3, B4, B5 = int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]), int(d[7]), int(d[8]), int(d[9]), int(d[10]), int(d[11])
    production = minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5)
    report = {goods1: sells1, goods2: sells2}
    print("Минимальные продажи груш и моркови:", production, 'соответственно')
    print(report)
except TypeError:
    print('Вы ввели неверное значение')
