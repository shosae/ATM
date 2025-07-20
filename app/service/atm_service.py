from repository.atm_repository import ATMRepository

class ATMService():
    def __init__(self):
        self.atm_repository = ATMRepository() 
    
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