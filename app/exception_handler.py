from exceptions.exceptions import *

def global_exception_handler(exc: Exception) -> dict:
    """
    발생한 예외에 따라 일관적인 응답을 생성
    """
    if isinstance(exc, CardNotRegisteredException):
        error_message = str(exc)
    elif isinstance(exc, InvalidPinException):
        error_message = str(exc)
    elif isinstance(exc, InsufficientBalanceException):
        error_message = str(exc)
    elif isinstance(exc, (NoAccountsFoundException, InvalidAmountException)):
        error_message = str(exc)
    else:
        # 예상치 못한 기타 모든 예외 처리
        error_message = "알 수 없는 오류가 발생했습니다"

    return {
        "success": False,
        "error": error_message
    }
