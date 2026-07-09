"""
    script: account.py
    action: modification of the textbook's Account class to provide read-only properties for the name and balance
    author: Kristin Brooks
    date:   06/25/26
"""

from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance"""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less that 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError("Initial balance must be >= to 0.00.")

        self._name = name
        self._balance = balance

    @property
    def name(self):
        """Return the name on the account"""
        return self._name

    @property
    def balance(self):
        """Return the balance in the account"""
        return self._balance


    def deposit(self, amount):
        """Deposit money to the account"""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError("amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account"""

        # if amount is greater than balance, raise an exception
        if amount > self._balance:
            raise ValueError("amount must be <= to balance")
        elif amount < Decimal('0.00'):
            raise ValueError("amount must be positive")

        self._balance -= amount

# Create an instance of the class
account1 = Account('John Green', Decimal('50.00'))
print(f'account1: {account1.name}, {account1.balance}')

# These assignments will throw errors because there are no setters (i.e. the attributes are read only)
print('About to try reassigning the name on the account to Jane Green.')
try:
    account1.name = 'Jane Green'
    print(account1.name)
except AttributeError:
    print("AttributeError: property 'name' of 'Account' has no setter")
finally:
    print(f'Current name on account: {account1.name}')

print('About to try reassigning the balance on the account to $100.00.')
try:
    account1.balance = Decimal('100.00')
    print(account1.balance)
except AttributeError:
    print("AttributeError: property 'balance' of 'Account' has no setter")
finally:
    print(f'Current balance in account: {account1.balance}')
