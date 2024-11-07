import threading
from time import sleep
from random import randint

class Bank:

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        transaction = 100
        while transaction:
            if self.balance >= 500 and self.lock.locked() == 1:
                self.lock.release()
            transaction -= 1
            plus = randint(50, 500)
            self.balance += plus
            print(f"Пополнение: {plus}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        transactio = 100
        while transactio:
            transactio -= 1
            minus = randint(50, 500)
            print(f"Запрос на {minus}")
            if minus <= self.balance:
                self.balance -= minus
                print(f"Снятие: {minus}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
