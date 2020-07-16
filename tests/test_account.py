from lib.account import Account

class Test_AccountClass:

    #Account Class
    
    def test_set_balance(self):
        account = Account()
        assert account.balance == 0, "Account should start with 0 balance"

    def test_set_transaction_list(self):
        account = Account()
        assert account.transactions == [], "Account should start with an empty transacton list"

    def test_credit_account(self):
        account = Account()
        account.credit(100)
        assert account.balance == 100, "Creditting an account should increase balance by amount"

    def test_withdraw_account(self):
         account = Account()
         account.withdraw(100)
         assert account.balance == -100, "withdrawing from an account should decrease balance by amount"



    
