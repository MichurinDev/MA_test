class SkypeScr:
    """Класс Skype с возможностью экранирования
    Принимает ссылки типа skype:xxx и \<a href="skype:xxx?call">skype\</a>

    :param link: Ссылка на Skype"""

    def __init__(self, link: str) -> None:
        self.link = link.lstrip()

    def screening(self) -> str:
        """Возвращает экранированную ссылку/HTML-тег Skype
        :return: Строка с экранированной ссылкой/HTML-тегом"""

        if self.link[0] == "<":
            parts = self.link.split('"')
            return parts[0] + '"' + 'skype:xxx?call' + '"' + parts[2]

        return "skype:xxx"
