class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
        self.food = Plant

    def eat(self, food, edible=False, fed=False):
        if edible is False and fed is False:
            print(f'{self.name} отказался есть {food.name}.')
            self.alive = False
            return self.alive
        elif edible is True and fed is False:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif edible is True and fed is True:
            print(f'{self.name} сыт!')


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(a2.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
