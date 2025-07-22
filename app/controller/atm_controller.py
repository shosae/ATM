from service.atm_service_base import ATMService
from error_handler import api_error_handler
from typing import List

class ATMController():
    def __init__(self, service: ATMService):
        self.atm_service = service
    """error_handler를 사용하여 발생되는 error를 캐치"""
    @api_error_handler
    def insert_card(self, card_number: str) -> None:
        self.atm_service.is_registered_card(card_number)
    
    @api_error_handler
    def verify_pin(self, card_number: str, pin: str) -> None:
        self.atm_service.verify_pin(card_number, pin)
        
    @api_error_handler
    def get_accounts_by_card(self, card_number: str) -> List[str]:
        return self.atm_service.get_accounts_by_card(card_number)

    @api_error_handler
    def deposit(self, acc_number: str, amount: int) -> int:
        return self.atm_service.deposit(acc_number, amount)
        
    @api_error_handler
    def withdraw(self, acc_number: str, amount: int) -> int:
        return self.atm_service.withdraw(acc_number, amount)

    @api_error_handler
    def get_balance(self, acc_number: str) -> int:
        return self.atm_service.get_balance(acc_number)