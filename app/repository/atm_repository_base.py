from abc import ABC, abstractmethod
from typing import Optional
from domain.card import Card
from domain.account import Account

class ATMRepository(ABC):
    @abstractmethod
    def find_card_by_number(self, card_number: str) -> Optional[Card]:
        """카드 번호로 카드 객체 반환, 없으면 None 반환"""
        pass

    @abstractmethod
    def find_account_by_number(self, account_number: str) -> Optional[Account]:
        """계좌 번호로 계좌 객체 반환, 없으면 None 반환"""
        pass
