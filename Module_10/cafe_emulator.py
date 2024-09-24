import random
import time
from queue import Queue
from threading import Thread
from random import randint

from Module_1.strings import example


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.delay = 0

    def run(self):
        self.delay = randint(3, 10)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for i, guest in enumerate(guests):
            if len(self.tables) > i and self.tables[i].guest is None:
                self.tables[i].guest = guests[i].name
                guests[i].start()
                print('Table number ' + str(self.tables[i].number) + ' occupied by ' + guests[i].name)
            else:
                self.queue.put(guests[i].name)
                print(f'The guest ' + guests[i].name + ' is in queue')


    def discuss_guests(self):
        if not self.queue.empty():
            guest_name = self.queue.get()
            print(f'The guest {guest_name} is being served')
            for table in self.tables:
                if table.guest == guest_name:
                    table.guest = None
                    print('Table number ' + str(table.number) + ' vacated by ' + guest_name)
                    break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang',
    'Sergey', 'Darya', 'Arman',
    'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
print(cafe.queue.get)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


# example about cooking =)

class Bulka (Thread) :
    def __init__(self, queue) :
        self. queue = queue
        super().__init__()
    def run (self):
        while True:
            time.sleep (3)
            if random.random() > 0.5:
                self.queue.put ('подгорелая булка')
            else:
                self.queue.put ( 'нормальная булка')

class Kotleta (Thread) :
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run (self):
        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get
            if bulka == 'нормальная булка' :
                time. sleep (0.1)
                self.count -= 1
            print( 'булок к приготовлению осталось ', self.count)
