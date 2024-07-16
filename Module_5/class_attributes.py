# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.


class House:
    def __init__(self, name, floor_numbers):
        self.name = name
        self.floor_numbers = floor_numbers

    def go_to(self, new_floor):
        if new_floor < 0 or new_floor > self.floor_numbers:
            print('Такого этажа не существует')
            return
        for key in range(1, new_floor + 1):
            print(key)


# this is for magic_tasks.py
if __name__ == '__main__':
    def print_house():
        h1 = House('ЖК Горский', 18)
        h2 = House('Домик в деревне', 2)
        h1.go_to(5)
        h2.go_to(10)


    print_house()
