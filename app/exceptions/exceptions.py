class CardNotRegisteredException(Exception):
    """등록된 카드가 없을 때 발생하는 예외"""
    pass

class NoAccountsFoundException(Exception):
    """등록된 계좌가 없을 때 발생하는 예외"""
    pass

class InsufficientBalanceException(Exception):
    """잔고가 부족할 때 발생하는 예외"""
    pass

class InvalidAmountException(Exception):
    """금액이 0보다 작거나 같을 때 발생하는 예외"""
    pass

class InvalidIndexException(Exception):
    """계좌 다중 선택 시에 잘못된 입력이 있을 때 발생하는 예외(index <=0)"""
    pass