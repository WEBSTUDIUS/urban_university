from random import randint
from time import sleep
from threading import Thread, Lock

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            intake = randint(50, 500)
            # Захватываем блокировку перед изменением баланса
            with self.lock:
                self.balance += intake
                print(f"Balance top up: {intake}. Balance: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdraw = randint(50, 500)
            print(f"You wanna take: {withdraw}")
            # Захватываем блокировку перед попыткой снять деньги
            with self.lock:
                if self.balance >= withdraw:
                    self.balance -= withdraw
                    print(f"Withdraw successful: {withdraw}. New balance: {self.balance}")
                else:
                    print(f"Withdraw was declined: {withdraw}. Balance: {self.balance}")
            sleep(0.001)

# Создание объекта банка
bk = Bank()

# Запуск потоков для пополнения и снятия средств
th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

# Вывод итогового баланса
print(f'Total balance: {bk.balance}')