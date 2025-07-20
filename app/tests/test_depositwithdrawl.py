import pytest
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

def test_deposit_zero(setUp):
    """비정상 입금 테스트(0$ 입금)"""
    controller, card, acc = setUp
    result = controller.deposit(card, acc, 0)
    assert result is None  
    assert acc.balance == 30

def test_deposit_negative(setUp):
    """비정상 입금 테스트(음수 입금)"""
    controller, card, acc = setUp
    result = controller.deposit(card, acc, -1)
    assert result is None  
    assert acc.balance == 30

def test_withdraw_balance_insufficient(setUp):
    """비정상 출금 테스트(잔고 부족)"""
    controller, card, acc = setUp
    result = controller.withdraw(card, acc, 40)
    assert result is None  
    assert acc.balance == 30    

def test_withdraw_zero(setUp):
    """비정상 출금 테스트(0$ 출금)"""
    controller, card, acc = setUp
    result = controller.withdraw(card, acc, 0)
    assert result is None  
    assert acc.balance == 30    

def test_withdraw_negative(setUp):
    """비정상 출금 테스트(음수$ 출금)"""
    controller, card, acc = setUp
    result = controller.withdraw(card, acc, -1)
    assert result is None  
    assert acc.balance == 30    