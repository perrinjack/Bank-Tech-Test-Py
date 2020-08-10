# Bank Tech Test for Makers Academy

## How to run

1. Clone this repo.

2. Install dependencies from the command line:

 ```
pip install pytest
```

3. Run tests with:

```
pytest tests/
```

4. Run the Python3 REPl:

```shell
python3
```

5. Import in `Account` with:

```python
from lib.account import Account
```

6. Set up your account with:

 ```python
account = Account()
 ```


## Specification

### Requirements

* You should be able to interact with your code via a REPL like IRB or the JavaScript console.  (You don't need to implement a command line interface that takes input from STDIN.)
* Deposits, withdrawal.
* Account statement (date, amount, balance) printing.
* Data can be kept in memory (it doesn't need to be stored to a database or anything).

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2012  
**And** a deposit of 2000 on 13-01-2012  
**And** a withdrawal of 500 on 14-01-2012  
**When** she prints her bank statement  
**Then** she would see

```
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```

## Approach 

### Doubles & Mocking in Python

Tests in python are done with the Pytest package. 
```
class MockTransaction:
     def __init__(self, value, type, current_balance):
        self.value = value
        self.type = type
        self.current_balance = current_balance
```



