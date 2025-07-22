import pytest
from repository.atm_repository import FakeATMRepository
from service.atm_service import FakeATMService
from controller.atm_controller import ATMController

@pytest.fixture
def setUp():
    repo = FakeATMRepository()
    service = FakeATMService(repo)
    controller = ATMController(service)
    return controller

def test_user_flow_insert_card_verify_pin_select_account_deposit_single_account(setUp):
    """계좌가 1개인 카드: 카드 삽입, PIN 인증, 계좌 선택, 입금 통합 테스트"""
    controller = setUp

    # 카드 삽입
    card = controller.insert_card("1234") # [A1]

    # 비밀번호 검증
    assert card.verify_pin("4321")
    
    # 계좌 조회
    accounts = controller.get_accounts_by_card(card)
    assert len(accounts) == 1
    
    # 계좌 선택
    acc = controller.select_account(card, 1)

    # 계좌에 입금
    old_balance = acc.balance
    controller.deposit(acc, 100)
    assert acc.balance == old_balance + 100

def test_user_flow_insert_card_verify_pin_select_account_withdraw_deposit_multi_account(setUp):
    """계좌가 여러 개인 카드: 카드 삽입, PIN 인증, 계좌 선택, 입금 및 출금 통합 테스트"""
    controller = setUp

    # 카드 삽입
    card = controller.insert_card("2345") # [A2, A3]
    
    # 비밀번호 검증
    assert card.verify_pin("5432")
    
    # 계좌 조회
    accounts = controller.get_accounts_by_card(card)
    assert len(accounts) > 1
    
    # 첫 번째 계좌에 입금
    acc1 = controller.select_account(card, 1)
    old_balance1 = acc1.balance
    controller.deposit(acc1, 100)
    assert acc1.balance == old_balance1 + 100

    # 두 번째 계좌에 출금
    acc2 = controller.select_account(card, 2)
    old_balance2 = acc2.balance
    controller.withdraw(acc2, 200)
    assert acc2.balance == old_balance2 - 200
