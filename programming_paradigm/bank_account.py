class BankAccount:
    """A class to model an Bank account operations"""
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        """A method to desposit an amount"""
        self.account_balance += amount
        return  self.account_balance
        
    def withdraw(self, amount):
        """A method to withdraw an amount"""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
       print(f"Current Balance: ${self.account_balance}.00")
