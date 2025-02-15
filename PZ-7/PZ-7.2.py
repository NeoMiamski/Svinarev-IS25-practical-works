# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2.
try:
    S1 = input("Введите S1: ")
    S = input("Введите S: ")
    Skull = S1 + S
    print(Skull)
    S2 = input("Введите S2: ")
    Skuf = S2 + S
    print(Skuf)
except TypeError:
    print('Вы ввели неверное значение')
