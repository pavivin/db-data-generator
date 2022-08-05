from typing import Any, Optional, List

from pydantic import BaseModel, Field


class ValuesFrequencyConfig(BaseModel):
    """Модель конфигурации частоты встречаемых значений"""
    value: Any
    frequency: Optional[int] # = Field(..., gt=0, le=10)


class BaseStrTypeConfig(BaseModel):
    """Конфиг для базового типа строки"""
    faker_type: Optional[str]

    values_select: List[ValuesFrequencyConfig]
    
    allowed_symbols: Optional[str]
    mask: Optional[str]

    unique: bool = False

    min_length: Optional[int] = 1
    max_length: Optional[int] = 1000



class BaseIntTypeConfig(BaseModel):
    """Конфиг для базового типа целочисленного значения"""
    # TODO


class BaseDecimalTypeConfig(BaseModel):
    """Конфиг для базового типа дробного значения"""
    # TODO


class BaseDateTypeConfig(BaseModel):
    """Конфиг для базового типа дата"""
    # TODO


class BaseTimestampTypeConfig(BaseModel):
    """Конфиг для базового типа дада/время"""
    # TODO


class BaseStrType:
    """Базовый класс str для генерации данных"""
    def __init__(self, config: BaseStrTypeConfig) -> None:
        self.config = config


class BaseIntType:
    """Базовый класс int для генерации данных"""
    def __init__(self, ) -> None:
        pass


class BaseDecimalType:
    """Базовый класс decimal для генерации данных"""
    def __init__(self, ) -> None:
        pass
    
    
class BaseDateType:
    """Базовый класс date для генерации данных"""
    def __init__(self, ) -> None:
        pass


class BaseTimestampType:
    """Базовый класс timestamp для генерации данных"""
    def __init__(self, ) -> None:
        pass
