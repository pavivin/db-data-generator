import random

from datetime import date, datetime
from decimal import Decimal

from . import base_types
from . import models


class TableDataGeneratorService:
    """Сервис для генерации данных"""
    def __init__(self, config: models.TableBase) -> None:
        self._config = config

    def generate_table_data(self) -> None:
        """Генерация данных для таблицы"""
        result_data = ''

        for _ in range(self._config.rows_to_generate): # TODO: потоки
            result_data += self._generate_row() + '\n'

        print(result_data)

    def _generate_row(self) -> str:
        for col in self._config.columns:
            match type(col.column_config):
                case base_types.BaseStrType:
                    return self._generate_fake_str_data(row_config=col.column_config)

                case base_types.BaseIntType:
                    return self._generate_fake_int_data(row_config=col.column_config)

                case base_types.BaseDecimalType:
                    return self._generate_fake_decimal_data(row_config=col.column_config)

                case base_types.BaseDateType:
                    return self._generate_fake_date_data(row_config=col.column_config)

                case base_types.BaseTimestampType:
                    return self._generate_fake_timestamp_data(row_config=col.column_config)

    @staticmethod
    def _generate_fake_str_data(row_config: base_types.BaseStrTypeConfig) -> str:
        """Генерация строки по конфигурации"""
        if row_config.config.faker_type:
            print('faker')
            pass # TODO: генерация с помощью faker
            return

        if row_config.config.values_select:
            selected_value = random.choice(row_config.config.values_select)
            return selected_value.value

    @staticmethod
    def _generate_fake_int_data(row_config: base_types.BaseIntTypeConfig) -> int:
        """Генерация целочисленного значения по конфигурации"""
        pass # TODO

    @staticmethod
    def _generate_fake_decimal_data(row_config: base_types.BaseDecimalTypeConfig) -> Decimal:
        """Генерация дробного значения по конфигурации"""
        pass # TODO

    @staticmethod
    def _generate_fake_date_data(row_config: base_types.BaseDateTypeConfig) -> date:
        """Генерация даты по конфигурации"""
        pass # TODO

    @staticmethod
    def _generate_fake_timestamp_data(row_config: base_types.BaseTimestampTypeConfig) -> datetime:
        """Генерация даты/времени по конфигурации"""
        pass # TODO
