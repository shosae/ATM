class Card:
    def __init__(self, number: str, pin: str, acc_list: list[str]):
        self.number = number
        self.pin = pin
        self.acc_list = acc_list
    def verify_pin(self, input_pin: str) -> bool:
        return self.pin == input_pin