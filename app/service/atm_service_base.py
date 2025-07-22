from abc import ABC, abstractmethod

class ATMService(ABC):
    @abstractmethod
    def is_registered_card(self, card_number: str) -> bool:
        pass

    @abstractmethod
    def verify_pin(self, card_number: str, pin: str)-> bool:
        pass
    
    @abstractmethod
    def get_accounts_by_card(self, card: str) -> list[str]:
        pass

    @abstractmethod
    def deposit(self, account_number: str, amount: int) -> int:
        pass

    @abstractmethod
    def withdraw(self, account_number: str, amount: int) -> int:
        pass
