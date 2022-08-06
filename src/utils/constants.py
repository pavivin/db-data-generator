from enum import Enum


class StringEnum(str, Enum):
    """Базовый Enum класс для перечислений строк"""

    def __str__(self):
        return self.value


class OutputTypes(StringEnum):
    """Список форматов для генерации"""

    JSON = 'json'
    CSV = 'csv'
