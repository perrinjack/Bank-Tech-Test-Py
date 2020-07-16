class Account:

    def __init__(self):
        self.balance = 0
        self.transactions = []


    def credit(self,amount):
        self.balance += amount
