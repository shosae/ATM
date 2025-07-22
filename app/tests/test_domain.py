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

def test_card_is_registered(setUp):
    """정상적인 카드가 등록되어 있는지 테스트"""
    controller = setUp
    
    #given, when
    res = controller.insert_card("1234")
    
    #then
    assert res['success'] is True

def test_card_is_unregistered(setUp):
    """등록이 안된 카드가 등록되어 있는지 테스트"""
    controller = setUp
     
    #given, when
    res = controller.insert_card("9999")
    
    #then
    assert res['success'] is False
    assert res['error'] == "등록된 카드가 없습니다"


def test_verify_pin_with_correct_pin(setUp):
    """올바른 pin 인증 테스트"""
    controller = setUp

    #given, when
    res = controller.verify_pin("1234", "4321") 

    #then
    assert res['success'] is True

def test_verify_pin_with_incorrect_pin(setUp):
    """틀린 pin 인증 테스트"""
    controller = setUp
    
    #given, when
    res = controller.verify_pin("1234", "9999")

    #then
    assert res['success'] is False
    assert res['error'] == "비밀번호가 올바르지 않습니다"


def test_get_accounts_by_registered_card_number(setUp):
    """카드가 등록된 계좌와 연결되어 있는지 테스트"""
    controller = setUp
        
    #given, when
    res = controller.get_accounts_by_card("1234") # Account("11-11", 30)

    #then
    assert res["success"] is True 
    assert res["data"] == ["11-11"]
