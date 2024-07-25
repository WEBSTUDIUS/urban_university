# PARENTS
class Animal:
    alive = True
    fed = False

    def __init__(self, name=''):
        self.name = name

    def eat(self, food):
        if not food.edible:
            print(f'{self.name} didnt eat {food.name} and stupidly died -_-')
            self.alive = False
        else:
            print(f'{self.name} ate {food.name} and still alive o_o')
            self.alive = True
            self.fed = True


class Plant:
    edible = False

    def __init__(self, name=''):
        self.name = name


# CHILDREN
class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
