try:    
    A = []
    n = int(input("Введите размер списка: "))
    q = int(input("Введите знаменатель: "))
    a1 = int(input("Введите первое число: "))
    for i in range(0, n):
        if i == 0:
            A.append(a1)  
        else:
            A.append(a1+(i*q))
    print(A)
except ValueError:
    print('Вы ввели неправильное значение')