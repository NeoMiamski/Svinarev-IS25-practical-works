# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2.
try:
    S1 = input("Введите S1: ")
    S = input("Введите S: ")
    skull = S1 + S
    print(skull)
    lenS1 = len(S1)
    lenSkull = len(skull)
    RS = []
    for i in range(lenS1, lenSkull + 1):
        RS.append(skull[i])
    print(RS)
except TypeError:
    print('Вы ввели неверное значение')
