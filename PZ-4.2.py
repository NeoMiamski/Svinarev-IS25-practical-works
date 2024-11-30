N = int(input("Введите делимое: "))
K = int(input("Введите делитель: "))
Quotient = 0
while N >= K: #Деление в формате цикла
    N = N - K
    Quotient += 1
Remainder = N
print("Частное: ", Quotient)
print("Остаток: ", Remainder)
