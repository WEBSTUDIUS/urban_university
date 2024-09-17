from random import randint
from time import sleep
from threading import Thread, Lock

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def run(self):
        ...

    def deposit(self):
        print(self.lock.locked())
        for i in range(100):
            intake = randint(50, 500)
            if self.balance >= 500 & self.lock.locked():
                # self.lock.acquire()
                self.balance += intake
                print(f"Balance top up: {intake}. Balance: {self.balance}", end='\n')
                self.lock.release()
                sleep(0.001)



    def take(self):
        for i in range(100):
            withdraw = randint(50, 500)
            print(f"You wanna take: {withdraw}", end='\n')
            if self.balance > withdraw:
                self.balance -= withdraw
                print(f"Withdraw successful: {withdraw}. New balance: {self.balance}", end='\n')
            else:
                print(f"Withdraw was declined : {withdraw}. Balance: {self.balance}", end='\n')
                self.lock.acquire()

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Total balance: {bk.balance}')
