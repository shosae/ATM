class Account:
    def __init__(self, acc_number: str, balance: int):
        self.acc_number = acc_number
        self.balance = balance
    
    def __eq__(self, other):
        if isinstance(other, Account):
            return self.acc_number == other.acc_number
        return False
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.get_balance