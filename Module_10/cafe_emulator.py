import time
from queue import Queue
from threading import Thread, Lock
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest
        self.lock = Lock()  # Блокировка для каждого стола


class Guest(Thread):
    def __init__(self, queue, name, cafe):
        super().__init__()
        self.name = name
        self.queue = queue
        self.cafe = cafe
        self.delay = randint(1, 10)  # Случайная задержка перед прибытием

    def run(self):
        # Гость засыпает на случайное время перед прибытием
        time.sleep(self.delay)
        print(f'{self.name} is arriving at the cafe and waits in line.\n')
        self.queue.put(self.name)  # Гость встаёт в очередь после задержки
        self.cafe.guest_arrived()  # Уведомляем кафе, что гость прибыл


class Cafe:
    def __init__(self, queue, *tables):
        self.tables = tables
        self.queue = queue
        self.total_guests = 0
        self.guests_arrived = 0  # Счетчик прибывших гостей

    def guest_arrival(self, *guests):
        self.total_guests = len(guests)  # Общее количество гостей
        # Стартуем потоки гостей
        for guest in guests:
            guest.start()

    def guest_arrived(self):
         # Увеличивает счетчик прибывших гостей
        self.guests_arrived += 1

    def discuss_guests(self):
        while True:
            # Если все гости прибыли и все обслужены, закрываем кафе
            if self.guests_arrived == self.total_guests and self.queue.empty():
                if all(table.guest is None for table in self.tables):
                    print("All guests are served. Cafe is closing.")
                    break

            if not self.queue.empty():
                guest_name = self.queue.get()
                for table in self.tables:
                    if table.lock.acquire(blocking=False):  # Попытка захватить блокировку стола
                        try:
                            if table.guest is None:  # Если стол свободен
                                table.guest = guest_name
                                print(f'Table number {table.number} occupied by {guest_name}')
                                self.serve_guest(table, guest_name)
                                break
                        finally:
                            table.lock.release()  # Освобождаем блокировку стола
            time.sleep(1)  # Для имитации времени обработки

    def serve_guest(self, table, guest_name):
        # Обслуживаем гостя в отдельном потоке, чтобы освобождать стол через некоторое время
        def serve():
            print(f'Serving {guest_name} at table {table.number}')
            time.sleep(randint(2, 5))  # Имитация времени обслуживания
            print(f'Table number {table.number} vacated by {guest_name}')
            table.guest = None  # Освобождаем стол после обслуживания

        Thread(target=serve).start()


queue1 = Queue()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang',
    'Sergey', 'Darya', 'Arman',
    'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(queue1, name, cafe=None) for name in guests_names]  # Инициализация гостей без кафе
# Заполнение кафе столами
cafe = Cafe(queue1, *tables)

# Указываем каждому гостю кафе
for guest in guests:
    guest.cafe = cafe

# запуск потоков гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей в основном потоке
cafe.discuss_guests()

# Ждём завершения всех потоков гостей
for guest in guests:
    guest.join()