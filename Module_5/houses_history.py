from operators_reload import House3

class House4(House3):
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    # def __init__(self, name, floor_numbers):
    #     super().__init__(name, floor_numbers)
    #     self.houses_history.append(self.name)

    def __del__(self):
        print(f" {self.name} снесён, но он останется в истории")


h1 = House4('ЖК Эльбрус', 10)
print(House4.houses_history)
h2 = House4('ЖК Акация', 20)
print(House4.houses_history)
h3 = House4('ЖК Матрёшки', 20)
print(House4.houses_history)

# Удаление объектов
del h2
del h3

print(House4.houses_history)



