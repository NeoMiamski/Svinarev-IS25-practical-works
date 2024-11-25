
x1 = int(input('¬ведите координаты x1: '))
y1 = int(input('¬ведите координаты y1: '))
x2 = int(input('¬ведите координаты x2: '))
y2 = int(input('¬ведите координаты y2: '))
if (1 <= x2 <= 8 and y1 == y2) or (1 <= y2 <= 8 and x1 == x2):
    print("True")
else:
    print("False")