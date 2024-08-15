class Figure:
    sides_count = 0

    def __init__(self, __sides: list, __color: list, filled: bool):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if [r, g, b] == self.__color:
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        pass

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        pass


class Circle:
    sides_count = 1

    def __init__(self, __radius):
        super().__init__()
        self.__radius = __radius

    def get_square(self):
        pass


class Triangle:
    sides_count = 3

    def __init__(self, __height):
        super().__init__()
        self.__height = __height

    def get_square(self):
        pass


class Cube:
    sides_count = 12

    def __init__(self):
        super().__init__()
        self.__sides = self.sides_count  # ???

    def get_volume(self):
        pass
