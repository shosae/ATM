import pytest
from controller.atm_controller import ATMController

@pytest.fixture
def setUp():
    controller = ATMController()
    card = controller.find_card_by_number("1234")
    acc = card.acc_list[0] # Account("11-11", 30)      
    return controller, acc

def test_deposit(setUp):
    """정상 입금 테스트"""
    controller, acc = setUp
    controller.deposit(acc, 40)
    assert acc.balance == 70

def test_withdraw(setUp):
    """정상 출금 테스트"""
    controller, acc = setUp
    controller.withdraw(acc, 20)
    assert acc.balance == 10

def test_deposit_zero(setUp):
    """비정상 입금 테스트(0$ 입금)"""
    controller, acc = setUp
    with pytest.raises(Exception):
        controller.deposit(acc, 0)
    assert acc.balance == 30

def test_deposit_negative(setUp):
    """비정상 입금 테스트(음수 입금)"""
    controller, acc = setUp
    with pytest.raises(Exception):
        controller.deposit(acc, -1)
    assert acc.balance == 30

@pytest.mark.parametrize("amount", [40, 0, -1])
def test_withdraw_invalid(setUp, amount):
    """비정상 출금 테스트(잔고 부족, 0, 음수)"""
    controller, acc = setUp
    with pytest.raises(Exception):
        controller.withdraw(acc, amount)
    assert acc.balance == 30