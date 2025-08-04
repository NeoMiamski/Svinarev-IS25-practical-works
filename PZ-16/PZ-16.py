# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

class Computer:

    def __init__(self, Brand, CPU, RAM):
        self.Brand = Brand
        self.CPU = CPU
        self.RAM = RAM

    def display_info(self):
        print(f"Брэнд: {self.Brand},  Процессор: {self.CPU}, Оперативная память: {self.RAM} ГБ")

Asus = Computer("Asus", "AMD Ryzen 5 4600", 16)
HP = Computer("HP", "Intel i9-14900K", 12)
Lenovo = Computer("Lenovo", "Intel i5-12400f", 24)

Asus.display_info()
HP.display_info()
Lenovo.display_info()