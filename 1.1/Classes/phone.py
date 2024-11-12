class PhoneScr:
    """Класс номера телефон с возможностью экранирования

    :param phone: Исходный номер телефона
    :param count: Количество экранируемых последних символов (по умолчанию равен 3)"""

    def __init__(self, phone: str, count: int = 3) -> None:
        self.phone = phone
        self.count = count

    def screening(self) -> str:
        """Возвращает экранированный номер телефона
        :return: Строка с экранированным номером телефона"""

        phone_with_normalised_whitespace = " ".join(self.phone.split())
        screeing_phone = ""

        count = 0
        
        for symbol in phone_with_normalised_whitespace[::-1]:
            if symbol != " ":
                if count < self.count:
                    screeing_phone = "x" + screeing_phone
                    count += 1
                else:
                    screeing_phone = symbol + screeing_phone
            else:
                screeing_phone = symbol + screeing_phone

        return screeing_phone
