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
    
    #given
    card_number = "1234"
    pin = "4321"
    acc = "11-11"
    acc_bal = 30

    # 카드 삽입, 등록된 카드인지 검증
    assert controller.insert_card(card_number)

    # PIN 검증
    assert controller.verify_pin(card_number, pin)
    
    # 계좌 조회
    res = controller.get_accounts_by_card(card_number)
    assert res["success"] is True 
    assert res["data"] == ["11-11"]
    
    # 사용자가 UI에서 조회된 계좌("11-11")를 선택했다고 가정하고 잔액 조회 진행
    res = controller.get_balance(acc)
    assert res["success"] is True
    assert res["data"] == acc_bal

    # 입금 진행
    res = controller.deposit(acc, 100)
    assert res["success"] is True 
    assert res["data"] == acc_bal + 100
    

def test_user_flow_insert_card_verify_pin_select_account_withdraw_deposit_multi_account(setUp):
    """계좌가 여러 개인 카드: 카드 삽입, PIN 인증, 계좌 선택, 입금 및 출금 통합 테스트"""
    controller = setUp

    #given
    card = "2345"
    pin = "5432"
    acc1 = "22-22"
    acc2 = "33-33"
    acc1_bal = 500
    acc2_bal = 1000

    # 카드 삽입, 등록 검증
    assert controller.insert_card(card)
    
    # PIN 검증
    assert controller.verify_pin(card, pin)
    
    # 계좌 조회
    res = controller.get_accounts_by_card(card)
    assert res["success"] is True
    assert len(res["data"]) == 2

    # 사용자가 UI에서 첫 번째 계좌("22-22")를 선택해 입금,
    # 두 번째 계좌("33-33")를 선택해 출금하는 상황을 가정

    # 첫 번째 계좌("22-22")에 입금
    res = controller.deposit(acc1, 100)
    assert res["success"] is True
    assert res["data"] == acc1_bal + 100

    # 두 번째 계좌("33-33")에 출금
    res = controller.withdraw(acc2, 200)
    assert res["success"] is True
    assert res["data"] == acc2_bal - 200
