from service.atm_service import ATMService
from exceptions.exceptions import *

class ATMController():
    
    def __init__(self):
        self.atm_service = ATMService()
    
    def find_card_by_number(self, card_number):
        """카드 번호로 카드 객체 반환"""
        return self.atm_service.find_card_by_number(card_number)
    
    def is_registered_card(self, card) -> bool:
        """카드 등록 여부"""
        try: 
            return self.atm_service.is_registered_card(card)
        except CardNotRegisteredException as e:
            print(f"ValueError: {e}")
            return False
         
    
    def get_accounts_by_card(self, card) -> list:
        """특정 카드의 계좌 리스트 반환"""
        try:
            return self.atm_service.get_accounts_by_card(card)
        except InvalidAmountException as e:
            print(f"Withdraw failed {e}")
            return None
        except NoAccountsFoundException as e:
            print(f"ValueError: {e}")
            return []

    def deposit(self, acc, amount) -> int:
        """입금 기능 구현"""
        try:
            return self.atm_service.deposit(acc, amount)
        except InvalidAmountException as e:
            print(f"Withdraw failed {e}")
            return None


    def withdraw(self, acc, amount) -> int:
        """출금 기능 구현"""
        try:
            return self.atm_service.withdraw(acc, amount)
        except InvalidAmountException as e:
            print(f"Withdraw failed {e}")
            return None
        except InSufficientBalanceException as e:
            print(f"Withdraw failed {e}")
            return None