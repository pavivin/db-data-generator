from datetime import date, datetime
from decimal import Decimal
from typing import Any, List

from pydantic import BaseModel

from utils.base_types import BaseDateType, BaseDecimalType, BaseIntType, BaseStrType, BaseTimestampType

from .constants import OutputTypes

AVAILABLE_TYPES_HINTING = str | int | Decimal | date | datetime
AVAILABLE_TYPES_CLASSES = BaseStrType | BaseIntType | BaseDecimalType | BaseDateType | BaseTimestampType


class TableColumn(BaseModel):
    """Модель колонки БД"""

    class Config:
        arbitrary_types_allowed = True

    column_name: str
    column_config: Any
    values: list[AVAILABLE_TYPES_HINTING] | None


class TableBase(BaseModel):
    """Модель таблицы для генерации данных"""

    table_name: str
    rows_to_generate: int = 100
    primary_key_column_name: str | None

    columns: List[TableColumn]

    output_format: str = OutputTypes.JSON
    # TODO: foreign_keys
