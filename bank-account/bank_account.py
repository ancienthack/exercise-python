import threading

class BankAccount:
    def __init__(self):
        self.account = False
        self.balance = None
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if self.account == True:
                return self.balance
            else:
                raise ValueError('No account')

    def open(self):
        if self.account == False:
            self.account = True
            self.balance = 0
        else:
            raise ValueError('No account')

    def deposit(self, amount):
        with self.lock:
            if self.account == True:
                if amount < 0:
                    raise ValueError('Negative amount')
                else:
                    self.balance += amount
            else:
                raise ValueError('No account')

    def withdraw(self, amount):
        with self.lock:
            if self.account == True:
                if amount < 0:
                    raise ValueError('Negative amount')
                elif amount > self.balance:
                    raise ValueError('Negative balance')
                else:
                    self.balance -= amount
            else:
                raise ValueError('No account')

    def close(self):
        if self.account == True:
            self.balance -= self.balance
            self.account = False
        else:
            raise ValueError('No account')

