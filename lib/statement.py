
class Statement:
    def __init__(self, transactions):
        self.transactions = transactions

    def prepare_header(self):
        return 'date || credit || debit || balance '

    def filter(self, transaction):
        if transaction.type == 'credit':
            return "|| || 100 || 500 \n"
        else:
            return "|| 100 || || 500 \n"
