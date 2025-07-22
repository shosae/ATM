from service.atm_service_base import ATMService
from exceptions.exceptions import *

class ATMController():
    
    def __init__(self, service: ATMService):
        self.atm_service = service
    
    def insert_card(self, card_number):
        """카드 삽입, 유효한 카드인지 검증 후 반환"""
        card = self.find_card_by_number(card_number)
        return card
    
    def find_card_by_number(self, card_number):
        """카드 번호로 카드 객체 반환"""
        return self.atm_service.find_card_by_number(card_number)
    
    def is_registered_card(self, card) -> bool:
        """카드 등록 여부"""
        return self.atm_service.is_registered_card(card)

    def get_accounts_by_card(self, card) -> list:
        """특정 카드의 계좌 리스트 반환"""
        return self.atm_service.get_accounts_by_card(card)

    def deposit(self, acc, amount) -> int:
        """입금 기능 구현"""
        return self.atm_service.deposit(acc, amount)

    def withdraw(self, acc, amount) -> int:
        """출금 기능 구현"""
        return self.atm_service.withdraw(acc, amount)
        
    def select_account(self, card, acc_index):
        """계좌 선택 기능 구현"""
        return self.atm_service.select_account(card, acc_index)
