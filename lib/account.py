from lib.transaction import Transaction
from lib.statement import Statement

class Account:

    def __init__(self, transaction=Transaction, statement = Statement):
        self.balance = 0
        self.transactions = []
        self.money_event = transaction
        self.statement = statement

    def credit(self, amount):
        self.balance += amount
        self.transactions.append(self.money_event(
            amount, 'credit', self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(
            self.money_event(amount, 'debit', self.balance))

    def produce_statement(self):
        self.statement.printer




