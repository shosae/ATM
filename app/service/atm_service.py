from repository.atm_repository import ATMRepository

class ATMService():
    def __init__(self):
        self.atm_repository = ATMRepository() 
    
    def is_registered_card(self, card) -> bool:
        """카드 등록 여부"""
        registered_card = self.atm_repository.find_card_by_number(card.number)
        return registered_card is not None
    
    def get_accounts_by_card(self, card) -> list:
        """카드에 연결된 계좌 확인"""
        return self.atm_repository.get_card_accounts(card.number)