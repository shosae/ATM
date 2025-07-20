from abc import ABC, abstractmethod
from typing import Optional, List
from domain.card import Card
from domain.account import Account

class ATMRepository(ABC):
    @abstractmethod
    def find_card_by_number(self, card_number) -> Optional[Card]:
        pass

    @abstractmethod
    def get_card_accounts(self, card_number) -> List[Account]:
        pass
