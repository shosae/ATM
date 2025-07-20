import pytest
from controller.atm_controller import ATMController
from exceptions.exceptions import InvalidIndexException
@pytest.fixture
def setUp():
    controller = ATMController()
    card = controller.find_card_by_number("2345")
    acc = card.acc_list # [A2, A3]     
    return controller, acc, card

def test_select_multiaccount(setUp):
    """정상 선택 테스트"""
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

@pytest.mark.parametrize("invalid_idx", [0, -1, 9999])
def test_select_multiaccount_select_out_of_range(setUp, invalid_idx):
    """범위를 벗어난 인덱스 선택 테스트"""
    controller, _, card = setUp
    with pytest.raises(Exception):
        controller.select_account(card, invalid_idx)
