from lib.transaction import Transaction
class Account:

    def __init__(self,transaction = Transaction ):
        self.balance = 0
        self.transactions = []


    def credit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount