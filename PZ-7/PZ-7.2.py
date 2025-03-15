# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2.
try:
    S1 = input("Введите S1: ")
    S = input("Введите S: ")
    S_S1 = S1 + S
    print("Вы ввели:", S_S1)
    S2 = input("Введите S2: ")
    lenS1 = len(S1)
    len_S_S1 = len(S_S1)
    S_in_list = []
    for i in range(lenS1, len_S_S1):
        S_in_list.append(S_S1[i])
    print("Вы ввели:", S2 + ''.join(S_in_list))

except TypeError:
    print('Вы ввели неверное значение')
