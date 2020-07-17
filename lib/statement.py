
class Statement:
    def __init__(self, transactions):
        self.transactions = transactions

    def prepare_header(self):
        return 'date || credit || debit || balance '

    def filter(self, transaction):
        if transaction.type == 'credit':
            return f"|| || {transaction.value} || {transaction.current_balance} \n"
        else:
            return f"|| {transaction.value} || || {transaction.current_balance} \n"

    def prepare_body(self):
        result = [self.filter(t) for t in self.transactions] 
        return result

    


    
