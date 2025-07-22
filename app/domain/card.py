from exceptions.exceptions import InvalidPinException

class Card:
    def __init__(self, number: str, pin: str, acc_list: list[str]):
        self.number = number
        self.__pin = pin
        self.__acc_list = acc_list

    def verify_pin(self, input_pin: str) -> bool:
        if self.__pin != input_pin:
            raise InvalidPinException("비밀번호가 올바르지 않습니다")
        return True
    
    def get_accounts(self) -> list[str]:
        return self.__acc_list