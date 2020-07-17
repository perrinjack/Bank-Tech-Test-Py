from lib.statement import Statement


class MockTransaction:
    def __init__(self, value, type, current_balance):
        self.value = value
        self.type = type
        self.current_balance = current_balance


class Test_StatementClass:

    def test_prepare_header(self):
        statement = Statement(transactions=[MockTransaction(
            100, 'debit', 500), MockTransaction(100, 'credit', 500)])

        assert statement.prepare_header() == 'date || credit || debit || balance '

    def test_statement_class_transaction_list(self):

        statement = Statement(transactions=[MockTransaction(
            100, 'debit', 500), MockTransaction(100, 'credit', 500)])
        assert isinstance(statement.transactions[0], MockTransaction)

    def test_statement_filters_debit_transaction(self):
        statement = Statement(transactions=[MockTransaction(
            100, 'debit', 500), MockTransaction(300, 'credit', 400)])
        assert statement.filter(MockTransaction(
            300, 'debit', 400)) == "|| 300 || || 400 \n"

    def test_statement_filters_credit_transaction(self):
        statement = Statement(transactions=[MockTransaction(
            100, 'debit', 500), MockTransaction(100, 'credit', 500)])
        assert statement.filter(MockTransaction(
            100, 'credit', 500)) == "|| || 100 || 500 \n"
    
    def test_prepare_body(self):
        statement = Statement(transactions=[MockTransaction(
            100, 'debit', 500), MockTransaction(100, 'credit', 500)])
        assert statement.prepare_body == "|| 300 || || 400 \n|| || 100 || 500 \n"
    
    

