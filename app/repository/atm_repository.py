from repository.atm_repository_base import ATMRepository
from domain.card import Card
from domain.account import Account
from typing import Optional

class FakeATMRepository(ATMRepository):
    def __init__(self):
        """임시 계좌 생성"""
        A1 = Account("11-11", 30)      
        A2 = Account("22-22", 500)
        A3 = Account("33-33", 1000)

        self.db_accounts = [A1, A2, A3]
        self.db_cards = [
            Card("1234", "4321", ["11-11"]),
            Card("2345", "5432", ["22-22", "33-33"])
        ]
    
    def find_card_by_number(self, card_number: str) -> Optional[Card]:
        for db_card in self.db_cards:
            if db_card.number == card_number:
                return db_card
        return None
    
    def find_account_by_number(self, acc_number: str) -> Optional[Account]:
        for db_acc in self.db_accounts:
            if db_acc.acc_number == acc_number:
                return db_acc
        return None
