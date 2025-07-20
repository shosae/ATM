from abc import ABC, abstractmethod

class ATMService(ABC):
    @abstractmethod
    def find_card_by_number(self, card_number):
        pass

    @abstractmethod
    def is_registered_card(self, card) -> bool:
        pass

    @abstractmethod
    def get_accounts_by_card(self, card) -> list:
        pass

    @abstractmethod
    def deposit(self, acc, amount) -> int:
        pass

    @abstractmethod
    def withdraw(self, acc, amount) -> int:
        pass

    @abstractmethod
    def select_account(self, card, acc_index):
        pass
