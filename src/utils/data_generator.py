import random

from datetime import date, datetime
from decimal import Decimal

from . import base_types
from . import models


import base_types
from typing import Callable
from data_generator import TableDataGeneratorService as TDGS

generate_type = {
    "str": TDGS._generate_fake_str_data,
    "datetime": TDGS._generate_fake_timestamp_data,
    "date": TDGS._generate_fake_date_data,
    "float": TDGS._generate_fake_decimal_data,
    "int": TDGS._generate_fake_int_data,
}


class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(self, config: models.TableBase, generate_type: dict[str, Callable]) -> None:
        self._config = config
        self._generate_type = generate_type

    def generate_table_data(self) -> None:
        """Генерация данных для таблицы"""
        result_data = ""

        for _ in range(self._config.rows_to_generate):  # TODO: потоки
            result_data += self._generate_row() + "\n"

        print(result_data)

    def _generate_row(self) -> str:
        for col in self._config.columns:
            self._generate_type[col.column_type]

    @staticmethod
    def _generate_fake_str_data(row_config: base_types.BaseStrTypeConfig) -> str:
        """Генерация строки по конфигурации"""
        if row_config.faker_type:
            print("faker")
            ...  # TODO: генерация с помощью faker
            return

        if row_config.values_select:
            selected_value = random.choice(row_config.values_select)
            return selected_value.value

    @staticmethod
    def _generate_fake_int_data(row_config: base_types.BaseIntTypeConfig) -> int:
        """Генерация целочисленного значения по конфигурации"""
        pass  # TODO

    @staticmethod
    def _generate_fake_decimal_data(row_config: base_types.BaseDecimalTypeConfig) -> Decimal:
        """Генерация дробного значения по конфигурации"""
        pass  # TODO

    @staticmethod
    def _generate_fake_date_data(row_config: base_types.BaseDateTypeConfig) -> date:
        """Генерация даты по конфигурации"""
        pass  # TODO

    @staticmethod
    def _generate_fake_timestamp_data(row_config: base_types.BaseTimestampTypeConfig) -> datetime:
        """Генерация даты/времени по конфигурации"""
        pass  # TODO
