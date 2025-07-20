from domain.card import Card
from domain.account import Account
from controller.atm_controller import ATMController


def test_deposit():
    """입금 테스트"""
    atm_controller = ATMController()
    card = atm_controller.find_card_by_number("1234")

    # 카드 등록 여부 검증
    assert atm_controller.is_registered_card(card)

    # 2. PIN 인증
    assert card.verify_pin("4321") is True
    acc = card.acc_list[0]  # "11-11" 계좌

    # 3. 계좌 연결 확인
    accounts = atm_controller.get_accounts_by_card(card)
    assert acc in accounts

    # 4. 입금
    atm_controller.deposit(card, acc, 40)

    # 5. 입금 후 잔액 검증
    assert acc.balance == 70

    
def test_withdraw():
    """출금 테스트"""
    atm_controller = ATMController()
    card = atm_controller.find_card_by_number("1234")

    # 카드 등록 여부 검증
    assert atm_controller.is_registered_card(card)

    # 2. PIN 인증
    assert card.verify_pin("4321") is True
    acc = card.acc_list[0]  # "11-11" 계좌

    # 3. 계좌 연결 확인
    accounts = atm_controller.get_accounts_by_card(card)
    assert acc in accounts

    # 4. 출금 실행
    atm_controller.withdraw(card, acc, 20)

    # 5. 출금 후 잔액 검증
    assert acc.balance == 10
