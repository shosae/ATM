def test_card_is_registered():
    """카드 등록 여부 테스트"""
    acc = Account("11-11", 30)
    card = Card("1234", "4321", [acc])
    atm_controller = ATMController()
    assert atm_controller.is_registered_card(card)

