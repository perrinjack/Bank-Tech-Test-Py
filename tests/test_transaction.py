
from lib.transaction import Transaction
class Test_TransactionClass:

    def test_stores_transaction_value(self):
        transaction = Transaction(300)
        assert transaction.value == 300, 'transaction has a transaction value'

    def test_stores_transaction_type(self):
        transaction_cred = Transaction(300, 'credit')
        assert transaction_cred.type == 'credit'


    