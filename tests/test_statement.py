from lib.statement import Statement

class MockTransaction:
    def __init__(self, value, type, current_balance):
        self.value = value
        self.type = type
        self.current_balance = current_balance


class Test_StatementClass:

    def test_set_balance(self):
        statement = Statement()
        assert statement.prepare_header == 'date || credit || debit || balance'




