import pytest
from repository.atm_repository import FakeATMRepository
from service.atm_service import FakeATMService
from controller.atm_controller import ATMController

@pytest.fixture
def setUp():
    repo = FakeATMRepository()
    service = FakeATMService(repo)
    controller = ATMController(service)
    acc = repo.db_accounts[0] # Account("11-11", 30)
    return controller, acc.acc_number, acc.balance

def test_deposit(setUp):
    """정상 입금 테스트"""
    controller, acc_num, bal = setUp
    res = controller.deposit(acc_num, 40)
    assert res["success"] is True
    assert res["data"] == bal + 40

def test_withdraw(setUp):
    """정상 출금 테스트"""
    controller, acc_num, bal = setUp
    res = controller.withdraw(acc_num, 20)
    assert res["success"] is True
    assert res["data"] == bal - 20

def test_get_balance(setUp):
    """잔액 확인 테스트"""
    controller, acc_num, _ = setUp
    res = controller.get_balance(acc_num)
    assert res["success"] is True

@pytest.mark.parametrize("amount", [0, -1])
def test_deposit_invalid(setUp, amount):
    """비정상 입금 테스트(0, 음수)"""
    controller, acc_num, _ = setUp
    res = controller.deposit(acc_num, amount)
    assert res["success"] is False
    assert res["error"] == "비정상적인 금액입니다"

@pytest.mark.parametrize("amount", [0, -1])
def test_withdraw_invalid(setUp, amount):
    """비정상 출금 테스트(0, 음수)"""
    controller, acc_num, _ = setUp
    res = controller.withdraw(acc_num, amount)
    assert res["success"] is False
    assert res["error"] == "비정상적인 금액입니다"

def test_withdraw_insufficient(setUp):
    """비정상 출금 테스트(잔고 부족)"""
    controller, acc_num, _ = setUp
    res = controller.withdraw(acc_num, 40)
    assert res["success"] is False
    assert res["error"] == "잔액이 부족합니다"
