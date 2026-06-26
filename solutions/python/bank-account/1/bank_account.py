""" Module solving the Bank Account exercise for Exercism. """

class BankAccount:
    """
    A class implementing a very simple representation of a bank account.
    """
    
    @staticmethod
    def _positive_values(amount: int):
        """
        Raises an error per tests if you try to deposit or withdraw a negative
        amount of money.
        """
        
        if amount < 0:
            raise ValueError("amount must be greater than 0")
    
    def __init__(self):
        """ Sets up Bank Account object. """
        
        self.is_open = False
        self.balance = 0
        
    def _check_open(self):
        """ 
        Helper method to raise an error if operations are attempted on unopened
        accounts per tests.
        """
        
        if not self.is_open:
            raise ValueError("account not open")

    def get_balance(self):
        """ Supplies the current account balance if the account is open. """
        
        self._check_open()
        
        return self.balance

    def open(self):
        """
        Converts an account from closed to open. Raises error if tried on an
        already open account.
        """
        
        if self.is_open:
            raise ValueError("account already open")
        
        self.is_open = True

    def deposit(self, amount: int):
        """ Adds amount to this account's balance if amount > 0. """
        
        self._check_open()
        
        BankAccount._positive_values(amount)
        
        self.balance += amount

    def withdraw(self, amount: int):
        """
        Removes amount from this account's balance if amount is greater than
        0 and amount is less than the current balance.
        """
        
        self._check_open()
        
        BankAccount._positive_values(amount)
        
        if amount > self.balance:
            raise ValueError("amount must be less than balance")
            
        self.balance -= amount

    def close(self):
        """
        Closes account, which zeroes balance. Note that it raises an error if
        tried on an already closed account.
        """
        
        self._check_open()
            
        self.balance = 0
        self.is_open = False
