from datetime import date
from decimal import Decimal
from string import digits, printable
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ValuesFrequencyConfig(BaseModel):
    """Модель конфигурации частоты встречаемых значений"""

    value: Any
    frequency: Optional[int] = Field(default=None, gt=0, le=10)


class BaseStrTypeConfig(BaseModel):
    """Конфиг для базового типа строки"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequencyConfig]]

    allowed_symbols: Optional[str]
    mask: Optional[str]

    unique: bool = False

    min_length: Optional[int] = 1
    max_length: Optional[int] = 100


class BaseIntTypeConfig(BaseModel):
    """Конфиг для базового типа целочисленного значения"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequencyConfig]]

    mask: Optional[str]

    unique: bool = False

    min_value: Optional[int] = -1000
    max_value: Optional[int] = 1000


class BaseDecimalTypeConfig(BaseModel):
    """Конфиг для базового типа дробного значения"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequencyConfig]]

    mask: Optional[str]

    unique: bool = False

    min_value: Optional[Decimal] = Decimal(-1000)
    max_value: Optional[Decimal] = Decimal(1000)

    min_fraction_numbers: Optional[int] = 0
    max_fraction_numbers: Optional[int] = 5


class BaseDateTypeConfig(BaseModel):
    """Конфиг для базового типа дата"""

    DEFAULT_TYPE: str = 'date_between'
    faker_type: str = DEFAULT_TYPE

    start_date: Optional[date]
    end_date: Optional[date]


class BaseTimestampTypeConfig(BaseModel):
    """Конфиг для базового типа дата/время"""

    DEFAULT_TYPE: str = 'date_time_between'
    faker_type: str = DEFAULT_TYPE

    start_date: Optional[date]
    end_date: Optional[date]


class BaseStrType:
    """Базовый класс str для генерации данных"""

    def __init__(self, config: BaseStrTypeConfig) -> None:
        self.config = config
        self.alphabet = printable


class BaseIntType:
    """Базовый класс int для генерации данных"""

    def __init__(self, config: BaseIntTypeConfig) -> None:
        self.config = config
        self.alphabet = digits


class BaseDecimalType:
    """Базовый класс decimal для генерации данных"""

    def __init__(self, config: BaseDecimalTypeConfig) -> None:
        self.config = config
        self.alphabet = digits


class BaseDateType:
    """Базовый класс date для генерации данных"""

    def __init__(self, config: BaseDateTypeConfig) -> None:
        self.config = config


class BaseTimestampType:
    """Базовый класс timestamp для генерации данных"""

    def __init__(self, config: BaseTimestampTypeConfig) -> None:
        self.config = config
