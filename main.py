# MASTER CLASSES
class Animal:
    alive = True
    fed = False
    name = ''

    def __init__(self, alive, fed, name):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    edible = False
    name = ''

    def __init__(self, edible, name):
        self.edible = edible
        self.name = name


# SUBMISSIVE CLASSES

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Fruit):
            return super().alive(True)
        if isinstance(food, Plant):
            return super().alive(False)
        return food


class Predator(Animal):
    def eat(self, food):
        return food


class Flower(Plant):
    def __init__(self):
        super().__init__(edible=False, name='')


class Fruit(Plant):
    def __init__(self):
        super().__init__(edible=True, name='')
