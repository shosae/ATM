import pytest
from controller.atm_controller import ATMController

@pytest.fixture
def setUp():
    controller = ATMController()
    card = controller.find_card_by_number("2345")
    acc = card.acc_list # [A2, A3]     
    return controller, acc, card

def test_select_multiaccount(setUp):
    controller, acc, card = setUp

    # 첫 번째 계좌 선택
    selected_acc = controller.select_account(card, 1)
    assert selected_acc == acc[0]

    controller.deposit(selected_acc, 200)
    assert selected_acc.balance == acc[0].balance  # 입금 후 잔액 확인

    # 두 번째 계좌 선택
    selected_acc = controller.select_account(card, 2)
    assert selected_acc == acc[1]

    controller.withdraw(selected_acc, 500)
    assert selected_acc.balance == acc[1].balance  # 출금 후 잔액 확인
