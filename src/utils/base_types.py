from datetime import date, datetime
from decimal import Decimal
from string import digits, ascii_letters
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ValuesFrequency(BaseModel):
    """Модель конфигурации частоты встречаемых значений"""

    value: Any
    frequency: Optional[int] = Field(default=None, gt=0, le=10)


class BaseStrType(BaseModel):
    """Конфиг для базового типа строки"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequency]]

    allowed_symbols: Optional[str]
    mask: Optional[str]

    unique: bool = False

    min_length: Optional[int] = 1
    max_length: Optional[int] = 100
    alphabet: str = ascii_letters + digits


class BaseIntType(BaseModel):
    """Конфиг для базового типа целочисленного значения"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequency]]

    mask: Optional[str]

    unique: bool = False

    min_value: Optional[int] = -1000
    max_value: Optional[int] = 1000
    alphabet: str = digits


class BaseDecimalType(BaseModel):
    """Конфиг для базового типа дробного значения"""

    faker_type: Optional[str]

    values_select: Optional[List[ValuesFrequency]]

    mask: Optional[str]

    unique: bool = False

    min_value: Optional[Decimal] = Decimal(-1000)
    max_value: Optional[Decimal] = Decimal(1000)

    min_fraction_numbers: Optional[int] = 0
    max_fraction_numbers: Optional[int] = 5
    alphabet: str = digits


class BaseDateType(BaseModel):
    """Конфиг для базового типа дата"""

    DEFAULT_TYPE: str = 'date_between'
    faker_type: str = DEFAULT_TYPE

    start_date: Optional[date]
    end_date: Optional[date]


class BaseTimestampType(BaseModel):
    """Конфиг для базового типа дата/время"""

    DEFAULT_TYPE: str = 'date_time_between'
    faker_type: str = DEFAULT_TYPE

    start_date: Optional[datetime]
    end_date: Optional[datetime]
