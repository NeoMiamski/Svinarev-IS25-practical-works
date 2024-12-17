try:
    def RectPS(x1, y1, x2, y2):
        P = abs(x1 - x2) * 2 + abs(y1 - y2) * 2
        S = abs(x1 - x2) * abs(y1 - y2)

        return P, S
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(RectPS(x1, y1, x2, y2))
except ValueError:
    print('Вы ввели неправильное значение')