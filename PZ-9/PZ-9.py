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
    A1, A2, A3, A4, A5, B1, B2, B3, B4, B5 = int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]), int(d[7]), int(d[8]), int(d[9]), int(d[10]), int(d[11])
    goods1 = d[0]
    goods2 = d[6]
    production = minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5)
    report = {goods1: A1, goods2: B1}
    report[goods1] = A2
    report[goods1] = A3
    report[goods1] = A4
    report[goods1] = A5
    report[goods1] = B2
    report[goods1] = B3
    report[goods1] = B4
    report[goods1] = B5
    print("Минимальные продажи груш и моркови:", production, 'соответственно')
    print(report)
except TypeError:
    print('Вы ввели неверное значение')