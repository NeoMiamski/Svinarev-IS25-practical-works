# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import random
from random import randint
quantity = randint (2, 6)
matrix = [[randint(-9, 9) for _ in range(quantity)] for _ in range(quantity)]
avg = []

for i in range(len(matrix)):          # Перебор строк
    for j in range(len(matrix[i])):   # Перебор столбцов\
        print(matrix[i][j], end=" ")
    if i % 2:
        avg.append(sum(matrix[i]) / len(matrix[i]))
    print()
print(avg)
