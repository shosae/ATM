from service.atm_service import ATMService

class ATMController():
    def __init__(self):
        self.atm_service = ATMService()
    
    def is_registered_card(self, card) -> bool:
        """카드 등록 여부"""
        return self.atm_service.is_registered_card(card)
    
    def get_accounts_by_card(self, card) -> list:
        """특정 카드의 계좌 리스트 반환"""
        return self.atm_service.get_accounts_by_card(card)