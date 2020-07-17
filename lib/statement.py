
class Statement:
    def __init__(self, transactions):
        self.transactions = transactions

    def prepare_header(self):
        return 'date || credit || debit || balance\n'

    def filter(self, transaction):
        if transaction.type == 'credit':
            return f'|| || {transaction.value} || {transaction.current_balance}'
        else:
            return f'|| {transaction.value} || || {transaction.current_balance}'

    def prepare_body(self):
        result = "\n".join([self.filter(t) for t in self.transactions])
        return result

    def printer(self):
        print(self.prepare_header())
        print(self.prepare_body())
