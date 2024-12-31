#Дан список ненулевых целых чисел размера N. Проверить, образуют ли его
#элементы геометрическую прогрессию. Если образуют, то вывести знаменатель
#прогрессии, если нет — вывести  0.
try:
    A = []
    i = 0
    n = int(input("Введите размер списка: "))
    while i < n:
        A.append(int(input('Введи значение списка:  ')))
        i += 1
    def GeoProgress(A):
        if n < 2:
            return 0
        r = A[1] / A[0]
        for i in range(2, n):
            if A[i] / A[i-1] != r:
                return 0
        return r
    result = GeoProgress(A)
    if result == 0:
        print(0)
    else:
        print("Массив образует геометрическую прогрессию")
except ValueError:
    print('Вы ввели неправильное значение')