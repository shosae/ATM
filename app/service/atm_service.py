from repository.atm_repository_base import ATMRepository 
from service.atm_service_base import ATMService
from exceptions.exceptions import (
    CardNotRegisteredException,
    NoAccountsFoundException
)

class FakeATMService(ATMService):
    def __init__(self, repository: ATMRepository):
        self.atm_repository = repository

    def is_registered_card(self, card_number: str) -> bool:
        card = self.atm_repository.find_card_by_number(card_number)
        if card is None:
            raise CardNotRegisteredException("등록된 카드가 없습니다")
        return True

    def verify_pin(self, card_number: str, pin: str) -> bool:
        card = self.atm_repository.find_card_by_number(card_number)
        return card.verify_pin(pin)
    
    def get_balance(self, acc_number: str) -> int:
        acc = self.atm_repository.find_account_by_number(acc_number)
        return acc.get_balance()
    
    def get_accounts_by_card(self, card_number: str) -> list[str]:
        card = self.atm_repository.find_card_by_number(card_number)
        accounts = card.get_accounts()
        if not accounts:
            raise NoAccountsFoundException("등록된 계좌가 없습니다")
        return accounts

    def deposit(self, acc_number: str, amount: int) -> int:
        acc = self.atm_repository.find_account_by_number(acc_number)
        return acc.deposit(amount)
    
    def withdraw(self, acc_number: str, amount: int) -> int:
        acc = self.atm_repository.find_account_by_number(acc_number)
        return acc.withdraw(amount)
