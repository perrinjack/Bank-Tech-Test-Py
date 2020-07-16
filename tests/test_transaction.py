

class Test_TransactionClass:

    def test_stores_transaction_value(self):
        transaction = Transaction(300)
        assert transaction.amount == 300