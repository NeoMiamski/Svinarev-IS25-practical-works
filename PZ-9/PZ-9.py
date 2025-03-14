# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
try:
    def minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5):
        pear_sells = min(A1, A2, A3, A4, A5)
        carrot_sells = min(B1, B2, B3, B4, B5)
        return pear_sells, carrot_sells
    d = "груши 45 991 63 100 12 морковь 13 47 26 0 16"
    d = d.split()
    goods1, goods2 = d[0], d[6]
    A1, A2, A3, A4, A5, B1, B2, B3, B4, B5 = int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]), int(d[7]), int(d[8]), int(d[9]), int(d[10]), int(d[11])
    production = minsells(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5)
    sells1, sells2 = [A1, A2, A3, A4, A5], [B1, B2, B3, B4, B5]
    report1 = {goods1: sells1}
    report2 = {goods2: sells2}
    C1, C2 = production[0], production[1]
    print("Минимальные продажи груш:", C1, "\nМинимальные продажи и моркови:", C2)
    print(report1, report2)
except TypeError:
    print('Вы ввели неверное значение')