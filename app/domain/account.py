from exceptions.exceptions import InSufficientBalanceException 
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
        if self.balance < amount:
            raise InSufficientBalanceException("잔액이 부족합니다")
        self.balance -= amount

    def get_balance(self):
        return self.get_balance