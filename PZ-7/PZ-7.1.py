# Дана строка, состоящая из русских слов, набранных заглавными буквами и 
# разделенных пробелами (одним или несколькими). Найти количество слов, которые 
# содержат ровно три буквы «А».
try: Генерал майонез???
    Text = input("Введите строку на русском: ")
    Text = Text.upper()
    Division = Text.split()
    Quantity = 0
    for i in range(0, len(Division)):
        if Division[i].count('А') == 3:
            Quantity += 1
    print('Слов с тремя А в вашей строке:', Quantity)
except TypeError:
    print('Вы ввели неверное значение')
