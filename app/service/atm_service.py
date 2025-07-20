from repository.atm_repository import ATMRepository
from exceptions.exceptions import CardNotRegisteredException, NoAccountsFoundException


class ATMService():
    def __init__(self):
        self.atm_repository = ATMRepository() 

    def find_card_by_number(self, card_number):
        """카드 번호로 카드 객체 반환"""
        return self.atm_repository.find_card_by_number(card_number)

    def is_registered_card(self, card) -> bool:
        """카드 등록 여부"""
        registered_card = self.atm_repository.find_card_by_number(card.number)
        if registered_card is None:
            raise CardNotRegisteredException("등록된 카드가 없습니다.")
        return True
    
    def get_accounts_by_card(self, card) -> list:
        """카드에 연결된 계좌 확인"""
        accounts = self.atm_repository.get_card_accounts(card.number)
        if not accounts :
            raise NoAccountsFoundException("등록된 계좌가 없습니다.")
        return accounts

    def deposit(self, acc, amount) -> int:
        """입금 기능 구현"""
        acc.deposit(amount)
        return acc.get_balance()

    def withdraw(self, acc, amount) -> int:
        """출금 기능 구현"""
        acc.withdraw(amount)
        return acc.get_balance()
