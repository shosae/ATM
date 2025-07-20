from domain.card import Card
from domain.account import Account
from controller.atm_controller import ATMController

def test_card_is_registered():
    """카드 등록 여부 테스트"""
    acc = Account("11-11", 30)
    card = Card("1234", "4321", [acc])
    atm_controller = ATMController()
    assert atm_controller.is_registered_card(card)

def test_verify_pin():
    """카드 pin 인증 테스트"""
    card = Card("1234", "4321", [])

    # 정상 비밀번호
    assert card.verify_pin("4321") is True

    # 틀린 비밀번호
    assert card.verify_pin("1234") is False
    
def test_get_accounts_by_registered_card_number():
    """카드가 등록된 계좌와 연결되어 있는지 테스트"""
    card = Card("1234", "4321", [])
    atm_controller = ATMController()

    # 카드 등록 여부 검증
    assert atm_controller.is_registered_card(card)
    
    # 연결된 계좌들이 있는지 확인
    accounts = atm_controller.get_accounts_by_card(card)
    assert len(accounts) > 0
    assert accounts[0].acc_number == "11-11"