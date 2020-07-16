
from lib.transaction import Transaction
class Test_TransactionClass:

    def test_stores_transaction_value(self):
        transaction = Transaction(300)
        assert transaction.value == 300