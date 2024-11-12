class MailScr:
    """Класс E-mail с возможностью экранирования

    :param mail: Исходный E-mail
    :param scr_symbol: Символ экранирования (по умолчанию равен "x")"""

    def __init__(self, mail: str, scr_symbol: str = "x") -> None:
        self.mail = mail
        self.scr_symbol = scr_symbol

    def screening(self) -> str:
        """Возвращает экранированный E-mail
        :return: Строка с экранированным E-mail"""

        body, domain = self.mail.split("@")
        new_body = self.scr_symbol * len(body)

        return new_body + "@" + domain
