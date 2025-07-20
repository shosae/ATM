from repository.atm_repository_base import ATMRepository
from domain.card import Card
from domain.account import Account
from typing import Optional, List

class FakeATMRepository(ATMRepository):
    def __init__(self):
        """임시 계좌 생성"""
        A1 = Account("11-11", 30)      
        A2 = Account("22-22", 500)
        A3 = Account("33-33", 1000)

        self.accounts = [A1, A2, A3]
        self.registered_cards = [
            Card("1234", "4321", [A1]),
            Card("2345", "5432", [A2, A3])
        ]
    
    def find_card_by_number(self, card_number) -> Optional[Card]:
        """카드 번호로 카드 찾기"""
        for card in self.registered_cards:
            if card.number == card_number:
                return card
        return None
    
    def get_card_accounts(self, card_number) -> List[Account]:
        """특정 카드의 계좌 리스트 반환"""
        card = self.find_card_by_number(card_number)
        if card:
            return card.acc_list
        return []