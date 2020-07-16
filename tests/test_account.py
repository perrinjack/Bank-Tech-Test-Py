from lib.account import Account

class MockTransaction:
    def __init__(self, value, type, current_balance):
        self.value = value
        self.type = type
        self.current_balance = current_balance

class Test_AccountClass:

    #Account Class
    def test_set_balance(self):
        account = Account(transaction = MockTransaction)
        assert account.balance == 0, "Account should start with 0 balance"

    def test_set_transaction_list(self):
        account = Account(transaction = MockTransaction)
        assert account.transactions == [], "Account should start with an empty transacton list"

    def test_credit_account(self):
        account = Account(transaction = MockTransaction)
        account.credit(100)
        assert account.balance == 100, "Creditting an account should increase balance by amount"

    def test_withdraw_account(self):
        account = Account(transaction = MockTransaction)
        account.withdraw(100)
        assert account.balance == -100, "withdrawing from an account should decrease balance by amount"



    
