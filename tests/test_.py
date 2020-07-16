from lib.account import Account

class TestClass:
    def test_one(self):
        x = Account()
        assert x.balance == 0 