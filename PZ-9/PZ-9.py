# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
try:
    def min_sells(sells1, sells2):
        pear_sells = min(sells1)
        carrot_sells = min(sells2)
        return pear_sells, carrot_sells
    report1 = {}
    report2 = {}
    s = "груши 45 991 63 100 12 морковь 13 47 26 0 16"
    s = s.split()
    sells1 = [int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])]
    sells2 = [int(s[7]), int(s[8]), int(s[9]), int(s[10]), int(s[11])]
    production = min_sells(sells1, sells2)
    report1[s[0]] = sells1
    report2[s[6]] = sells2
    print("Минимальные продажи груш:", production[0], "\nМинимальные продажи моркови:", production[1])
    print(report1, report2)
except TypeError:
    print('Вы ввели неверное значение')