from lib.account import Account

class TestClass:

    #Account Class
    
    def test_one(self):
        account = Account()
        assert account.balance == 0, "Account should start with 0 balance"

    def test_two(self):
        account = Account()
        assert account.transactions == [], "Account should start with an empty transacton list"

    def test_three(self):
        account = Account()
        account.credit(100)
        assert account.balance == 100, "Creditting an account should increase balance by amount"

    def test_four(self):
         account = Account()
         account.withdraw(100)
         assert account.balance == -100, "withdrawing from an account should decrease balance by amount"



    #Transaction Class
