from lib.transaction import Transaction
class Account:

    def __init__(self,transaction = Transaction ):
        self.balance = 0
        self.transactions = []
        self.money_event = transaction

    def credit(self,amount):
        self.balance += amount
        self.transactions.append(self.money_event( amount, 'credit', self.balance))
        

    def withdraw(self,amount):
        self.balance -= amount
        self.transactions.append(self.money_event( amount, 'debit', self.balance))