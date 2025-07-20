class CardNotRegisteredException(Exception):
    """등록된 카드가 없을 때 발생하는 예외"""
    pass

class NoAccountsFoundException(Exception):
    """등록된 계좌가 없을 때 발생하는 예외"""
    pass
