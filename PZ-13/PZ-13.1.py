# В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.
import random
from random import randint
quantity = randint (2, 6)
matrix = [[randint(-9, 9) for _ in range(quantity)] for _ in range(quantity)]
new_array = []

for i in range(len(matrix)):          # Перебор строк
    for j in range(len(matrix[i])):   # Перебор столбцов\
        if matrix[i][j] < 0:
            new_array.append(matrix[i][j])
        print(matrix[i][j], end=" ")
    print()
print(len(new_array))