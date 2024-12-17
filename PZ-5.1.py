# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.
try:
    def LF(t):
        l = len(t)
        
        return l
    t = str(input())
    s = LF(t)
    print(s)
except ValueError:
    print('Вы ввели неправильное значение')