import pytest
from domain.card import Card
from domain.account import Account
from controller.atm_controller import ATMController

@pytest.fixture
def setUp():
    controller = ATMController()
    card = controller.find_card_by_number("1234")
    acc = card.acc_list[0] 
    return controller, card, acc

def test_deposit(setUp):
    """정상 입금 테스트"""
    controller, card, acc = setUp
    controller.deposit(card, acc, 40)
    assert acc.balance == 70

    
def test_withdraw(setUp):
    """정상 출금 테스트"""
    controller, card, acc = setUp
    controller.withdraw(card, acc, 20)
    assert acc.balance == 10

def test_withdraw_raises_error_when_balance_insufficient(setUp):
    """비정상 출금 테스트"""
    controller, card, acc = setUp
    result = controller.withdraw(card, acc, 40)
    assert result is None  
    assert acc.balance == 30    