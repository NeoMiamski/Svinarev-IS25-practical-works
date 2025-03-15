# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2.
try:
    S = input("Введите S: ")
    S1 = input("Введите S1: ")
    S2 = input("Введите S2: ")
    if S1 in S:
        Changed = S.replace(S1, S2, 1)
        print(Changed)
    else:
        print("S1 не входит в строку S!")
except TypeError:
    print('Вы ввели неверное значение')
