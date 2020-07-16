from lib.account import Account

class TestClass:
    
    def test_one(self):
        account = Account()
        assert account.balance == 0

    def test_two(self):
        account = Account()
        assert account.transactions == []

    def test_three(self):
        account = Account().credit(100)
        assert account.balance == 100
