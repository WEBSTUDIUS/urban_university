# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам.
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

from magic_tasks import House2


class House3(House2):
    def __eq__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers == other.floor_numbers

    def __lt__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers < other.floor_numbers

    def __le__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers <= other.floor_numbers

    def __gt__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers > other.floor_numbers

    def __ge__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers >= other.floor_numbers

    def __ne__(self, other):
        if not isinstance(other, House3):
            raise SyntaxError(f"{other} must me an Object")
        return self.floor_numbers != other.floor_numbers

    def __add__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError(f"{value} must me int")
        self.floor_numbers = self.floor_numbers + value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError(f"{value} must me int")
        self.floor_numbers = value + self.floor_numbers
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError(f"{value} must me int")
        self.floor_numbers += value
        return self


if __name__ == '__main__':
    def print_house():
        h1 = House3('ЖК Эльбрус', 10)
        h2 = House3('ЖК Акация', 20)

        print(h1)
        print(h2)

        print(h1 == h2)  # __eq__

        h1 = h1 + 10  # __add__
        print(h1)
        print(h1 == h2)

        h1 += 10  # __iadd__
        print(h1)

        h2 = 10 + h2  # __radd__
        print(h2)

        print(h1 > h2)  # __gt__
        print(h1 >= h2)  # __ge__
        print(h1 < h2)  # __lt__
        print(h1 <= h2)  # __le__
        print(h1 != h2)  # __ne__


    print_house()
