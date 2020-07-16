
from lib.transaction import Transaction
class Test_TransactionClass:

    def test_stores_transaction_value(self):
        transaction = Transaction(300,'credit')
        assert transaction.value == 300, 'transaction has a transaction value'

    def test_stores_transaction_type(self):
        transaction_cred = Transaction(300, 'credit')
        transaction_deb = Transaction(300, 'debit')
        assert transaction_cred.type == 'credit'
        assert transaction_deb.type == 'debit'

    def test_stores_current_balance(self):
        transaction = Transaction(300,'credit', 500)
        assert transaction.current_balance == 500, 'transaction has the balance of account after settlement'
    