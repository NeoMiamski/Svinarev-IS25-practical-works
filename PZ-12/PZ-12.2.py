# Составить список, в который будут включены только согласные буквы и привести их к
# верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
# 'Каир'].
sequence = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
string = ''
string.join(sequence)
string = string.upper()
countdown = {i for i in string if i in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'}
consonants = []
print(countdown)