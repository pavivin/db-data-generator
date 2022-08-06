from datetime import date, datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel

from .constants import OutputTypes


class TableColumn(BaseModel):
    """Модель колонки БД"""

    class Config:
        arbitrary_types_allowed = True

    column_name: str
    column_type: str | int | Decimal | date | datetime


class TableBase(BaseModel):
    """Модель таблицы для генерации данных"""

    table_name: str
    rows_to_generate: int = 100
    primary_key_column_name: Optional[str]

    columns: List[TableColumn]

    output_format: str = OutputTypes.JSON
    # TODO: foreign_keys
