from re import X
from tarfile import XGLTYPE


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
P = 0
S = 0
x = 0
y = 0
def RectPS(x1, y1, x2, y2, P, S, x, y):
    if x1 > x2:
        x = x1 - x2
    else:
        x = x2 - x1
    if y1 > y2:
        y = y1 - y2
    else:
        y = y2 - y1
    P = x * 2 + y * 2
    S = x * y
print(P, S)